# Usage Guide

This guide explains how to use the Self-Optimizing ANPR system after installation.

---

# Step 1: Launch the Project

Open a terminal in the project directory and run:

```bash
python src/main.py
```

---

# Step 2: Provide an Input Image

Place the vehicle image inside the `sample_images` folder.

Example:

```
sample_images/
    car-1.jpg
```

The system automatically loads the image for processing.

---

# Step 3: Vehicle Detection

The YOLOv8 model detects the vehicle and locates the license plate.

---

# Step 4: License Plate Cropping

The detected license plate is cropped from the vehicle image for further processing.

---

# Step 5: Self-Optimizing Preprocessing

The cropped plate is processed using four enhancement strategies:

- Static (Grayscale + OTSU + Morphology)
- CLAHE + Thresholding
- Gamma Correction
- Resolution Enhancement + Sharpening

---

# Step 6: OCR Recognition

EasyOCR reads text from all four processed images.

The OCR confidence score for each result is calculated automatically.

---

# Step 7: Best Result Selection

The system compares all OCR confidence scores.

The result with the highest confidence is selected automatically.

---

# Step 8: Character Validation

Common OCR mistakes are corrected automatically.

Example:

```
O → 0
I → 1
S → 5
B → 8
```

The final license plate is validated according to the Indian license plate format.

---

# Step 9: Output

The system displays:

- Original vehicle image
- Cropped license plate
- Selected preprocessing result
- Final recognized license plate
- OCR confidence score

---

# Example Output

```
Vehicle Detected

License Plate:
KA01AB1234

OCR Confidence:
96.42%
```