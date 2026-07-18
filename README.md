# 🚗 ANPR – Self-Optimizing Preprocessing Module

![Python](https://img.shields.io/badge/Python-3.10-blue)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-red)
![EasyOCR](https://img.shields.io/badge/OCR-EasyOCR-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **This repository contains my individual contribution to a team-based Automatic Number Plate Recognition (ANPR) project.**
>
> My contribution focuses on designing and implementing a **Self-Optimizing Preprocessing Pipeline** that improves OCR accuracy by automatically evaluating multiple preprocessing strategies and selecting the best result based on OCR confidence.

---

# 📌 Project Overview

Automatic Number Plate Recognition (ANPR) systems often experience reduced OCR accuracy due to challenging environmental conditions such as poor lighting, motion blur, shadows, rain, fog, and low-resolution license plates.

Traditional ANPR pipelines generally rely on a single preprocessing technique before OCR. However, a single technique rarely performs well across all real-world scenarios.

This project introduces a **Self-Optimizing Preprocessing Framework** that automatically evaluates multiple preprocessing strategies for every detected license plate, performs OCR on each processed image, compares OCR confidence scores, and selects the most reliable recognition result.

The module also performs character correction and Indian license plate format validation to further improve recognition accuracy.

The preprocessing module has been designed as an independent component that can be integrated into larger ANPR systems.

---

# 🎯 Objectives

- Improve OCR accuracy using adaptive preprocessing.
- Evaluate multiple preprocessing strategies automatically.
- Select the best OCR result using confidence comparison.
- Correct common OCR character mismatches.
- Improve recognition under challenging environmental conditions.
- Build a modular preprocessing pipeline that integrates with larger ANPR systems.

---

# ✨ Key Features

- 🚘 License Plate Processing Module
- 🖼️ Multiple Image Preprocessing Strategies
- ⚡ Self-Optimizing Strategy Selection
- 🔍 OCR using EasyOCR
- 📈 Confidence-Based Decision Making
- 🔄 Character Correction
- 🇮🇳 Indian License Plate Validation
- 🧩 Modular Design for Easy Integration
- 📂 Queue-Based Image Processing
- 📊 OCR Confidence Evaluation

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| OpenCV | Image Processing |
| YOLOv8 | License Plate Detection |
| EasyOCR | Optical Character Recognition |
| NumPy | Numerical Operations |
| PyTorch | Deep Learning Backend |

## 📂 Project Structure

```text
ANPR-Self-Optimizing-Preprocessing/
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── workflows/
│   │   └── python-ci.yml
│   └── PULL_REQUEST_TEMPLATE.md
│
├── docs/
│   ├── architecture.md
│   ├── contribution.md
│   ├── future-work.md
│   ├── installation.md
│   ├── project-structure.md
│   ├── usage.md
│   └── images/
│       ├── architecture.png
│       ├── comparison.png
│       ├── evaluation.png
│       ├── ocr-selection.png
│       ├── preprocessing.png
│       ├── queue-system.png
│       └── workflow.png
│
├── incoming_images/
│   ├── car-1.jpg
│   ├── car-3.jpeg
│   ├── car-4.jpg
│   ├── car-5.jpg
│   ├── car-6.jpg
│   ├── car-7.jpeg
│   └── car-9.jpg
│
├── models/
│   ├── plates_model_v1.pt
│   └── yolov8n.pt
│
├── processed_output/
│   └── .gitkeep
│
├── src/
│   ├── demo.py
│   └── main.py
│
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 📑 Table of Contents

- Project Overview
- Objectives
- Key Features
- Technologies Used
- Project Structure
- System Architecture
- Complete Workflow
- Self-Optimizing Preprocessing
- OCR Confidence Selection
- Queue-Based Processing
- Performance Evaluation
- Comparison with Conventional Approach
- Installation
- Usage
- Output
- Additional Documentation
- Future Improvements
- My Contribution
- References
- License
- Author

---

# 🏗️ System Architecture

The architecture below illustrates the overall preprocessing pipeline implemented in this project.

The module receives a detected license plate image, applies multiple preprocessing strategies, performs OCR on every processed image, compares OCR confidence scores, and automatically selects the most reliable recognition result.

![System Architecture](docs/images/architecture.png)

---

# 🔄 Complete Workflow

The complete processing workflow is shown below.

1. Vehicle image is received.
2. YOLOv8 detects the license plate.
3. The detected plate is cropped.
4. Multiple preprocessing strategies are applied.
5. EasyOCR extracts text from every processed image.
6. OCR confidence scores are evaluated.
7. The best preprocessing strategy is selected automatically.
8. Character correction is performed.
9. Indian license plate validation is applied.
10. Final license plate text is returned.

![Workflow](docs/images/workflow.png)

---

# 🖼️ Self-Optimizing Preprocessing

Unlike conventional ANPR systems that depend on a single preprocessing technique, this module evaluates multiple preprocessing methods before OCR.

Implemented preprocessing strategies include:

- Static Preprocessing (Grayscale + OTSU + Morphology)
- CLAHE-Based Enhancement
- Adaptive Thresholding
- Resolution Enhancement & Sharpening

Each processed image is independently evaluated using OCR.

The preprocessing result producing the highest confidence score is selected automatically.

![Preprocessing Pipeline](docs/images/preprocessing.png)

---

# 🎯 OCR Confidence-Based Selection

Each preprocessed image is passed to EasyOCR.

Instead of accepting the first OCR result, the module evaluates every OCR output based on confidence score and structural validation.

The preprocessing strategy with the highest overall score is automatically selected.

This adaptive approach significantly improves OCR robustness under varying environmental conditions.

![OCR Confidence Selection](docs/images/ocr-selection.png)

---

# ⚙️ Queue-Based Processing

The preprocessing module follows a Producer–Consumer architecture.

- The Producer monitors the `incoming_images/` directory.
- Newly detected vehicle images are pushed into the processing queue.
- The Worker thread performs preprocessing and OCR.
- The Output thread stores processed results inside `processed_output/`.

This architecture makes the preprocessing module independent and suitable for integration with larger ANPR systems.

![Queue Processing](docs/images/queue-system.png)

---

# 📈 Performance Evaluation

The preprocessing module is evaluated using:

- OCR Confidence
- Character Recognition Accuracy
- Plate Recognition Accuracy
- Processing Time
- Strategy Selection Performance

These metrics demonstrate the effectiveness of the adaptive preprocessing framework.

![Performance Evaluation](docs/images/evaluation.png)

---

# 🔍 Comparison with Conventional Approach

Traditional ANPR systems generally rely on a single preprocessing method.

The proposed framework evaluates multiple preprocessing strategies and dynamically selects the most suitable result based on OCR confidence.

This improves robustness and recognition accuracy under challenging real-world conditions.

![Comparison](docs/images/comparison.png)

---

# 💡 Key Innovation

The core contribution of this work is the **Self-Optimizing Preprocessing Framework**, which:

- Applies multiple preprocessing strategies to the same license plate.
- Performs OCR on every processed image.
- Compares OCR confidence scores.
- Selects the best preprocessing strategy automatically.
- Applies character correction.
- Validates Indian license plate format.
- Produces the final recognition result with improved reliability.

This adaptive approach eliminates manual preprocessing selection and improves OCR performance across different environmental conditions.
# ⚙️ Installation

Follow the steps below to set up the project on your local machine.

## Prerequisites

Make sure the following software is installed:

- Python 3.10 or later
- Git
- pip (Python Package Manager)
- Visual Studio Code (Recommended)

---

## Clone the Repository

```bash
git clone https://github.com/sejal13-dev/ANPR-Self-Optimizing-Preprocessing.git
```

Move into the project directory.

```bash
cd ANPR-Self-Optimizing-Preprocessing
```

---

## Install Dependencies

Install all required Python libraries.

```bash
pip install -r requirements.txt
```

---

## Required Models

Place the trained YOLO models inside the `models/` directory.

```text
models/
│
├── yolov8n.pt
└── plates_model_v1.pt
```

---

## Sample Images

The repository already includes sample vehicle images inside the `incoming_images/` folder.

You can replace these images with your own test images at any time.

---

## Run the Application

Start the preprocessing service using:

```bash
python src/main.py
```

Once the application starts, it continuously monitors the `incoming_images/` folder for new vehicle images.

---

# ▶️ Usage

## Input

The application automatically watches the `incoming_images/` folder.

- Images already present in the folder are processed automatically.
- Any new image copied into the folder while the application is running is also processed automatically.

Supported image formats include:

- JPG
- JPEG
- PNG

---

## Processing Pipeline

For every input image, the following operations are performed:

1. Vehicle Detection
2. License Plate Detection
3. License Plate Cropping
4. Skew Correction
5. Multiple Image Preprocessing
6. OCR using EasyOCR
7. Confidence-Based Strategy Selection
8. Character Correction
9. Indian License Plate Validation
10. Final License Plate Recognition

---

## Output

The system automatically generates:

- Processed vehicle image
- Cropped license plate image
- Selected preprocessing strategy
- Recognized license plate text
- OCR confidence information (console output)

Processed images are saved inside:

```text
processed_output/
```

Example:

```text
processed_output/
├── vehicle_0.jpg
├── plate_0.jpg
├── vehicle_1.jpg
├── plate_1.jpg
└── ...
```

---

## Console Output

A typical execution looks similar to:

```text
Using CPU. Note: This module is much faster with a GPU.

Waiting for incoming images...

ANPR System Started Successfully

New image received: car-1.jpg

Worker processing image...

Strategy: clahe

Detected Plate: HR26DQ5551

Saved vehicle: processed_output/vehicle_0.jpg

Plate text: HR26DQ5551

--------------------------------
```

---

## Notes

- The application follows a Producer–Consumer queue architecture.
- Images are processed sequentially as they arrive.
- The service continues running until it is stopped manually.
- Processed images are written to the `processed_output/` directory.

# 📂 Additional Documentation

Detailed project documentation is available inside the `docs/` directory.

| Document | Description |
|----------|-------------|
| architecture.md | System Architecture |
| installation.md | Installation Guide |
| usage.md | Usage Guide |
| project-structure.md | Project Folder Structure |
| future-work.md | Planned Enhancements |
| contribution.md | Individual Contribution |

---

# 📈 Performance Highlights

The proposed preprocessing framework provides the following advantages:

- Improved OCR Accuracy
- Automatic Preprocessing Strategy Selection
- Better Performance under Challenging Lighting Conditions
- Reduced Manual Parameter Tuning
- Confidence-Based OCR Decision Making
- Modular Integration with Larger ANPR Systems

---

# 🧩 Design Philosophy

This preprocessing module has been designed as an independent component of an Automatic Number Plate Recognition (ANPR) pipeline.

Instead of tightly coupling preprocessing with detection or backend services, the module operates independently using a queue-based architecture. This design makes it reusable, scalable, and easy to integrate into larger intelligent transportation systems.

---

# 🚀 Future Improvements

Planned enhancements include:

- 🎥 Real-time webcam support
- 📹 Live video stream processing
- 🚗 Multi-vehicle simultaneous processing
- 🌙 Enhanced low-light preprocessing
- ☁️ Cloud deployment (AWS / Azure / GCP)
- 🌐 REST API using FastAPI
- 🖥️ Interactive Web Dashboard
- 🐳 Docker containerization
- ⚡ GPU acceleration using CUDA
- 🌍 Multi-country license plate recognition
- 🤖 AI-based image enhancement models

---

# 🤝 My Contribution

This repository represents **my individual contribution** to a team-based Automatic Number Plate Recognition (ANPR) project.

### Responsibilities

- Designed the Self-Optimizing Preprocessing Framework.
- Implemented multiple OpenCV preprocessing strategies.
- Integrated EasyOCR for license plate recognition.
- Developed OCR confidence-based strategy selection.
- Implemented character correction and validation.
- Designed the queue-based preprocessing workflow.
- Prepared project documentation and GitHub repository.

> **Note:** This repository focuses exclusively on the preprocessing and OCR enhancement module. Other ANPR components, including backend services, APIs, and database modules, were developed separately as part of the overall team project.

---

# 📚 References

This project uses the following open-source technologies:

- Python
- OpenCV
- EasyOCR
- NumPy
- PyTorch
- Ultralytics YOLOv8

Special thanks to the developers and maintainers of these excellent open-source projects.

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

# 👩‍💻 Author

**Sejal Priya**

MCA Student

Aspiring Software Engineer | AI & Java Full Stack Developer

**GitHub:**  
https://github.com/sejal13-dev

---

# 🙏 Acknowledgements

I would like to thank:

- The open-source community for providing outstanding libraries and tools.
- The Ultralytics team for YOLOv8.
- The EasyOCR development team.
- OpenCV contributors.
- My faculty members and project guide for their valuable guidance.
- My teammates for their collaboration on the overall ANPR project.

---

# ⭐ Repository Information

If you found this project useful:

- ⭐ Star this repository.
- 🍴 Fork it for your own experiments.
- 📝 Explore the documentation.
- 🤝 Suggestions and feedback are always welcome.

---

# 📌 Final Note

This repository demonstrates the implementation of a **Self-Optimizing Preprocessing Framework** for Automatic Number Plate Recognition (ANPR).

The framework improves OCR accuracy by evaluating multiple preprocessing strategies, comparing OCR confidence scores, and automatically selecting the most reliable recognition result.

The module has been designed as an independent and reusable component that can be integrated into larger ANPR systems, intelligent transportation applications, or future research projects.