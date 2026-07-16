# ==========================================================
# IMPORT REQUIRED LIBRARIES
# ==========================================================
# These libraries are used for image processing, threading,
# queue management, machine learning models and OCR.
# ==========================================================

import cv2                 # OpenCV for image processing
import numpy as np         # Numerical operations on images
import os                  # File and folder operations
import time                # Used for delays and timing
import re                  # Regular expressions for text cleaning
import threading           # For running parallel threads
from queue import Queue    # Queue for producer-consumer pipeline

from ultralytics import YOLO   # YOLO object detection model
import easyocr                 # OCR library for reading plate text
import torch                   # Used by EasyOCR backend


# ==========================================================
# LOAD YOLO DETECTION MODELS
# ==========================================================
# YOLOv8 Nano is used because it is lightweight and suitable
# for Raspberry Pi deployment.
# ==========================================================

# Pretrained vehicle detection model
vehicle_model = YOLO("yolov8n")

# Custom trained license plate detection model
plate_model = YOLO("plates_model_v1.pt")


# ==========================================================
# DETECTION CONFIDENCE THRESHOLDS
# ==========================================================

# Minimum confidence for vehicle detection
VEHICLE_CONF = 0.3

# Minimum confidence for license plate detection
PLATE_CONF = 0.3


# ==========================================================
# CREATE PIPELINE QUEUES
# ==========================================================
# input_queue  → stores incoming images
# output_queue → stores final processed results
# ==========================================================

input_queue = Queue(maxsize=300)
output_queue = Queue(maxsize=300)

# ==========================================================
# STEP 5: OCR CHARACTER CORRECTION MAP
# ==========================================================
# These maps fix OCR mistakes like:
# O → 0, B → 8, Z → 2 etc.
# ==========================================================

letter_corrections = {
    '0': 'O',   # Zero misread instead of letter O
    '2': 'Z',   # Two misread instead of letter Z
    '5': 'S',   # Five misread instead of letter S
    '6': 'G',   # Six misread instead of letter G
    '8': 'B',
    'E': 'N',   # Added: E misread instead of N
    'O': 'Q',   # Added: O misread instead of Q
    
}

# ---------------------------------------------------
# Corrections when OCR mistakenly reads a LETTER
# instead of a DIGIT (for numeric positions)
# ---------------------------------------------------
digit_corrections = {
    'O': '0',   # Letter O misread instead of digit 0
    'D': '0',   # Letter D misread instead of digit 0
    'I': '1',   # Letter I misread instead of digit 1
    'L': '4',   # Updated: Letter L misread instead of digit 4
    'Z': '2',   # Letter Z misread instead of digit 2
    'B': '8',   # Letter B misread instead of digit 8
    'G': '0',   # Keep existing 'G': '0'
    'A': '4',   # Letter A misread instead of digit 4
    'T': '7',
    'E': '6',   # Keep existing 'E': '6'
    'W': '4',   # Updated: Letter W misread as digit 4
    'P': '9',
}

# Remove the entry 'S': '5'
if 'S' in digit_corrections and digit_corrections['S'] == '5':
    del digit_corrections['S']



# ==========================================================
# STEP 6: VALID INDIAN STATE CODES
# ==========================================================

valid_states = [
    "AP","AR","AS","BR","CG","CH","DD","DL","GA",
    "GJ","HR","HP","JH","JK","KA","KL","LA","LD",
    "MH","ML","MN","MP","MZ","NL","OD","PB","PY",
    "RJ","SK","TN","TR","TS","UK","UP","WB"
]

def correct_state_code(text):

    if len(text) < 2:
        return text

    state_part = text[:2]

    if state_part in valid_states:
        return text

    confusion_map = {
        'H': ['H', 'M', 'N'],
        'M': ['M', 'H', 'N'],
        'N': ['N', 'M', 'H'],
        'A': ['A', 'H'],
        'K': ['K', 'X'],
        'T': ['T', 'I'],
    }

    for c1 in confusion_map.get(state_part[0], [state_part[0]]):
        for c2 in confusion_map.get(state_part[1], [state_part[1]]):
            candidate = c1 + c2
            if candidate in valid_states:
                return candidate + text[2:]

    return text

# ==========================================================
# INITIALIZE OCR READER
# ==========================================================
# GPU is disabled because Raspberry Pi does not support CUDA.
# ==========================================================

reader = easyocr.Reader(['en'], gpu=False)

# ==========================================================
# VEHICLE FILTER FUNCTION
# ==========================================================

def is_vehicle(image):

    results = vehicle_model(image)

    vehicle_classes = [2, 3, 5, 7]  # car, bike, bus, truck

    for result in results:

        if result.boxes is None:
            continue

        boxes = result.boxes

        for cls, conf in zip(
            boxes.cls.cpu().numpy(),
            boxes.conf.cpu().numpy()
        ):

            cls = int(cls)

            print("Detected class:", cls, "Conf:", conf)

            if cls in vehicle_classes and conf > 0.3:
                return True

    return False
# ==========================================================
# LICENSE PLATE DETECTION FUNCTION
# ==========================================================

def detect_plate(image):
    """
    Detects license plate using the trained YOLO model.

    Returns:
        Cropped plate image if detected
        None if no plate detected
    """

    results = plate_model(image)

    best_plate = None
    best_conf = 0

    for result in results:

        if result.boxes is None:
            continue

        boxes = result.boxes
        xyxy = boxes.xyxy.cpu().numpy()
        confs = boxes.conf.cpu().numpy()

        for i in range(len(xyxy)):

            if confs[i] < PLATE_CONF:
                continue

            if confs[i] > best_conf:
                x1, y1, x2, y2 = map(int, xyxy[i])
                best_plate = image[y1:y2, x1:x2]
                best_conf = confs[i]

    return best_plate

# ==========================================================
# SKEW CORRECTION
# ==========================================================

def correct_skew(plate):

    gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)

    lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

    if lines is None:
        return plate

    angles = []

    for i in range(min(len(lines),10)):

        rho, theta = lines[i][0]

        angle = (theta - np.pi/2) * 180 / np.pi

        angles.append(angle)

    median_angle = np.median(angles)

    h, w = plate.shape[:2]

    center = (w//2 , h//2)

    M = cv2.getRotationMatrix2D(center, median_angle, 1.0)

    rotated = cv2.warpAffine(
        plate,
        M,
        (w,h),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_REPLICATE
    )

    return rotated

# -----------------------------
# Define Preprocessing Strategies
# -----------------------------


# Strategy 1 – Static Preprocessing (Traditional Approach)
def preprocess_static(img):
    """
    This function applies traditional image preprocessing
    techniques to enhance license plate characters before OCR.


    Steps:
    1. Convert to grayscale
    2. Apply Gaussian blur (noise reduction)
    3. Apply OTSU thresholding (automatic binarization)
    4. Apply morphological closing (fill small gaps)


    Returns:
        Processed binary image suitable for OCR
    """


    # Convert image to grayscale
    # OCR works better on single-channel images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # Apply Gaussian Blur to reduce noise
    # (5x5) kernel smooths minor variations in lighting
    blur = cv2.GaussianBlur(gray, (5,5), 0)


    # Apply OTSU thresholding
    # Automatically determines optimal threshold value
    # Converts image into binary (black & white)
    _, thresh = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )


    # Create 3x3 kernel for morphological operation
    kernel = np.ones((3,3), np.uint8)


    # Apply Morphological Closing
    # Helps fill small gaps inside characters
    # Improves OCR readability
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)


    # Return final processed image
    return morph

# -----------------------------
# Strategy 2 – CLAHE + OTSU
# -----------------------------


def preprocess_clahe(img):
    """
    This preprocessing strategy enhances contrast
    using CLAHE before applying OTSU thresholding.


    It is especially useful for:
    - Low contrast plates
    - Shadowed regions
    - Uneven lighting conditions


    Returns:
        Enhanced binary image suitable for OCR
    """


    # Convert image to grayscale
    # CLAHE works on single-channel images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # Create CLAHE object (Contrast Limited Adaptive Histogram Equalization)
    # clipLimit controls contrast amplification
    # tileGridSize defines local region size for contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))


    # Apply CLAHE to improve local contrast
    enhanced = clahe.apply(gray)


    # Apply OTSU thresholding after contrast enhancement
    # Converts image into binary form for better OCR detection
    _, thresh = cv2.threshold(
        enhanced,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )


    # Return processed image
    return thresh

# -----------------------------
# Strategy 3 – Adaptive Thresholding
# -----------------------------


def preprocess_adaptive(img):
    """
    This preprocessing strategy applies adaptive thresholding.

    Unlike global thresholding (like OTSU),
    adaptive thresholding calculates threshold values
    for small local regions of the image.


    This is highly effective when:
    - Lighting conditions vary across the plate
    - Some parts of the plate are bright and others are dark


    Returns:
        Locally binarized image suitable for OCR
    """


    # Convert image to grayscale
    # Required before applying thresholding techniques
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # Apply Gaussian blur to reduce noise
    # Helps produce smoother thresholding results
    blur = cv2.GaussianBlur(gray, (5,5), 0)


    # Apply Adaptive Gaussian Thresholding
    # 255 → Maximum pixel value
    # ADAPTIVE_THRESH_GAUSSIAN_C → Weighted sum of neighborhood values
    # THRESH_BINARY → Output is binary image
    # 11 → Size of local neighborhood block
    # 2 → Constant subtracted from computed threshold
    thresh = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )


    # Return processed image
    return thresh

# -----------------------------
# Strategy 4 – Resolution Enhancement + Sharpening
# -----------------------------


def preprocess_resolution(img):
    """
    This preprocessing strategy improves character clarity
    by increasing image resolution and enhancing edges.


    It is particularly useful when:
    - The detected plate is small
    - Characters appear blurred
    - Fine details are lost


    Returns:
        Upscaled and sharpened grayscale image
    """


    # Convert image to grayscale
    # OCR performs better on single-channel images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # -----------------------------
    # Step 1: Resolution Enhancement
    # -----------------------------


    # Upscale image by 2x using cubic interpolation
    # Cubic interpolation preserves smoothness and detail better
    # than nearest-neighbor or linear interpolation
    upscaled = cv2.resize(
        gray,
        None,
        fx=2,                 # Scale width by 2
        fy=2,                 # Scale height by 2
        interpolation=cv2.INTER_CUBIC
    )


    # -----------------------------
    # Step 2: Edge Sharpening
    # -----------------------------


    # Define sharpening kernel
    # Enhances edges by emphasizing intensity differences
    # Center value (4) controls sharpening strength
    kernel = np.array([
        [0, -1,  0],
        [-1,  4, -1],
        [0, -1,  0]
    ])


    # Apply sharpening filter to enhanced image
    sharpened = cv2.filter2D(upscaled, -1, kernel)


    # Return final processed image
    return sharpened


# ==========================================================
# OCR FUNCTION
# ==========================================================

def run_ocr(image):
    """
    Performs OCR on the processed license plate.

    Returns:
        detected_text
        average_confidence
    """

    results = reader.readtext(
        image,
        allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    )

    text = ""
    confidence = 0

    for item in results:

        _, detected_text, prob = item

        text += detected_text
        confidence += prob

    if len(results) > 0:
        confidence = confidence / len(results)

    return text.strip(), confidence

# ==========================================================
# STEP 10: FORMAT CORRECTION
# ==========================================================

def format_correct_plate(text):

    text = text.replace(" ","").upper()
    text = re.sub(r'[^A-Z0-9]','',text)
    text = text.replace("IND","")

    best_candidate = ""

    for i in range(len(text)):

        candidate = text[i:i+10]

        if len(candidate) != 10:
            continue

        corrected = list(candidate)

        for pos in range(10):

            # LETTER POSITIONS (state + series)
            if pos in [0,1]:

                if corrected[pos] in letter_corrections:
                    corrected[pos] = letter_corrections[corrected[pos]]

                if not corrected[pos].isalpha():
                    corrected[pos] = ''
            
             # SERIES positions (DO NOT MODIFY)
            elif pos in [4,5]:

                if not corrected[pos].isalpha():
                    corrected[pos] = ''

            # DIGIT POSITIONS
            else:

                if corrected[pos] in digit_corrections:
                    corrected[pos] = digit_corrections[corrected[pos]]

                if not corrected[pos].isdigit():
                    corrected[pos] = ''

        final = "".join(corrected)

        if len(final) == 10:

            # ✅ APPLY STATE CORRECTION HERE
            final = correct_state_code(final)

            best_candidate = final
            break

    return best_candidate

# ==========================================================
# STEP 11: INDIAN LICENSE PLATE VALIDATION
# ==========================================================

def is_valid_indian_plate(text):

    if len(text) != 10:
        return False

    if text[:2] not in valid_states:
        return False

    pattern = r'^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$'

    return re.match(pattern, text) is not None

# ---------------------------------------------------------
# Self-Optimizing Preprocessing Framework (Novelty Core)
# ---------------------------------------------------------


def self_optimizing_preprocess(img):
    """
    This function implements the adaptive preprocessing framework.


    Steps:
    1. Apply multiple preprocessing strategies
    2. Run OCR on each processed version
    3. Apply structural correction
    4. Compute weighted structural score
    5. Select best-performing strategy
    """


    # Dictionary of all preprocessing strategies
    strategies = {
        "static": preprocess_static,
        "clahe": preprocess_clahe,
        "adaptive": preprocess_adaptive,
        "resolution": preprocess_resolution
    }


    # Initialize best selection variables
    best_score = -999
    best_text = ""
    best_conf = 0
    best_strategy = ""
    best_img = img


    # Evaluate each preprocessing strategy
    for name, func in strategies.items():


        # Apply preprocessing
        processed = func(img)


        # Run OCR
        raw_text, conf = run_ocr(processed)


        # Apply structural format correction
        corrected = format_correct_plate(raw_text)


        score = 0


        # ---------------------------------------------
        # Structural Scoring Logic
        # ---------------------------------------------


        # Length validation
        if len(corrected) == 10:
            score += 10
        else:
            score -= 5  # Reverted penalty

        # State code validation
        if len(corrected) >= 2 and corrected[:2] in valid_states:
            score += 20
        else:
            score -= 10  # Reverted penalty

        # Position-wise validation (LLDDLLDDDD)
        if len(corrected) == 10:
            for i in range(10):


                # Letter positions
                if i in [0, 1, 4, 5]:
                    if corrected[i].isalpha():
                        score += 3
                    else:
                        score -= 2  # Reverted penalty


                # Digit positions
                else:
                    if corrected[i].isdigit():
                        score += 3
                    else:
                        score -= 2  # Reverted penalty


        # Penalize excessive length (garbage text)
        if len(corrected) > 10:
            score -= 5  # Reverted penalty


        # Add small weight for OCR confidence
        score += conf * 2

        # Update best strategy if current score is higher
        if score > best_score:
            best_score = score
            best_text = corrected
            best_conf = conf
            best_strategy = name
            best_img = processed


    # Return best processed image and OCR result
    return best_img, best_text, best_conf, best_strategy


# ==========================================================
# WORKER FUNCTION
# ==========================================================

def worker():
    """
    Worker continuously processes images from the input queue.

    Steps:
    1. Receive image
    2. Detect plate
    3. Run OCR
    4. Send result to output queue
    """

    while True:

        # Get image from queue
        image = input_queue.get()
        # Step 0: Vehicle Filtering
        if not is_vehicle(image):
           print("❌ Not a vehicle. Skipping...")
           input_queue.task_done()
           continue

        print("Worker processing image...")

        # Detect plate
        plate = detect_plate(image)

        if plate is None:
            print("No plate detected")
            input_queue.task_done()
            continue

        plate=correct_skew(plate)

        processed_plate,text,conf,strategy=self_optimizing_preprocess(plate)

        if not text:
            print("No valid OCR")
            input_queue.task_done()
            continue

        print("Strategy:",strategy)
        print("Detected Plate:", text)

        # Send result to output queue
        output_queue.put((image,processed_plate,text,conf))

        input_queue.task_done()


# ==========================================================
# FOLDER READER (PRODUCER)
# ==========================================================

def folder_reader(folder):

    processed = set()

    print("Waiting for incoming images...")

    while True:

        files = os.listdir(folder)

        for file in files:

            if file in processed:
                continue

            path = os.path.join(folder, file)

            image = cv2.imread(path)

            if image is not None:

                input_queue.put(image)

                processed.add(file)

                print("New image received:", file)

        time.sleep(2)


# ==========================================================
# OUTPUT SAVER
# ==========================================================

def output_saver():

    os.makedirs("processed_output", exist_ok=True)

    count = 0

    while True:

        vehicle_img, plate_img, text, conf = output_queue.get()

        vehicle_path = f"processed_output/vehicle_{count}.jpg"
        plate_path = f"processed_output/plate_{count}.jpg"

        cv2.imwrite(vehicle_path, vehicle_img)
        cv2.imwrite(plate_path, plate_img)

        print("Saved vehicle:", vehicle_path)
        print("Plate text:", text)

        print("--------------------------------")

        count += 1

        output_queue.task_done()


# ==========================================================
# START THE ANPR SYSTEM
# ==========================================================

# Create input folder if not present
os.makedirs("incoming_images", exist_ok=True)


# Start folder reader thread
reader_thread = threading.Thread(
    target=folder_reader,
    args=("incoming_images",),
    daemon=True
)

reader_thread.start()


# Start worker thread
worker_thread = threading.Thread(
    target=worker,
    daemon=True
)

worker_thread.start()


# Start output saver thread
saver_thread = threading.Thread(
    target=output_saver,
    daemon=True
)

saver_thread.start()


print("ANPR System Started Successfully")


# Keep program running
while True:
    time.sleep(5)
