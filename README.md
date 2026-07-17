# 🚗 ANPR – Self-Optimizing Preprocessing Module

![Python](https://img.shields.io/badge/Python-3.10-blue)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-red)
![EasyOCR](https://img.shields.io/badge/OCR-EasyOCR-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **This repository contains my individual contribution to a team-based Automatic Number Plate Recognition (ANPR) project.**
>
> My contribution focuses on designing and implementing a **Self-Optimizing Preprocessing Pipeline** that enhances OCR accuracy by automatically evaluating multiple preprocessing strategies and selecting the best result based on OCR confidence.

---

# 📌 Project Overview

Automatic Number Plate Recognition (ANPR) systems often experience reduced OCR accuracy due to varying environmental conditions such as poor lighting, shadows, blur, rain, fog, and low-resolution license plates.

Instead of relying on a single preprocessing technique, this project introduces a **Self-Optimizing Preprocessing Framework** that applies multiple preprocessing strategies to each detected license plate image, performs OCR on every processed result, compares the OCR confidence scores, and automatically selects the best output.

The module also performs character correction and Indian license plate format validation to further improve recognition accuracy.

This repository demonstrates the preprocessing and OCR enhancement module independently, making it reusable in any ANPR pipeline.

---

# 🎯 Objectives

- Improve OCR accuracy using adaptive preprocessing.
- Automatically evaluate multiple preprocessing strategies.
- Select the best OCR output using confidence comparison.
- Correct common OCR character mismatches.
- Improve recognition under challenging environmental conditions.
- Build a modular preprocessing pipeline that can integrate with any ANPR system.

---

# ✨ Key Features

- 🚘 License Plate Processing Module
- 🖼️ Multiple Image Preprocessing Strategies
- ⚡ Self-Optimizing Strategy Selection
- 🔍 OCR using EasyOCR
- 📈 Confidence-Based Decision Making
- 🔄 Character Replacement & Correction
- 🇮🇳 Indian License Plate Validation
- 🧩 Modular Design for Easy Integration

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| OpenCV | Image Processing |
| YOLOv8 | License Plate Detection Integration |
| EasyOCR | Optical Character Recognition |
| NumPy | Numerical Operations |
| PyTorch | Deep Learning Backend |

---

# 📂 Project Structure

```text
ANPR-Self-Optimizing-Preprocessing/
│
├── docs/
│   ├── architecture.md
│   ├── installation.md
│   ├── usage.md
│   ├── project-structure.md
│   ├── future-work.md
│   ├── contribution.md
│   └── images/
│       ├── architecture.png
│       ├── workflow.png
│       ├── preprocessing.png
│       ├── ocr-selection.png
│       ├── queue-system.png
│       ├── comparison.png
│       └── evaluation.png
│
├── models/
│   ├── yolov8n.pt
│   └── plates_model_v1.pt
│
├── sample_images/
│
├── output/
│
├── src/
│   └── main.py
│
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
```

---

# 📑 Table of Contents

- Project Overview
- Objectives
- Key Features
- Technologies Used
- Project Structure
- System Architecture
- Project Workflow
- Self-Optimizing Preprocessing
- OCR Confidence Selection
- Queue Processing
- Performance Evaluation
- Installation
- Usage
- Future Improvements
- Contribution
- License
- Author
- Acknowledgements

---

# 🏗️ System Architecture

The following architecture illustrates the overall processing pipeline of the self-optimizing preprocessing module. The module receives a detected license plate image, applies multiple preprocessing strategies, performs OCR on each processed image, compares confidence scores, and returns the best recognized license plate.

![System Architecture](docs/images/architecture.png)

---

# 🔄 Complete Workflow

The workflow below describes how the preprocessing module fits into an ANPR pipeline.

1. Vehicle image is captured.
2. YOLOv8 detects the license plate.
3. The detected plate is cropped.
4. Multiple preprocessing strategies are applied.
5. EasyOCR extracts text from every processed image.
6. OCR confidence scores are compared.
7. The best preprocessing strategy is selected automatically.
8. Character correction and validation are performed.
9. The final license plate is returned.

![Workflow](docs/images/workflow.png)

---

# 🖼️ Self-Optimizing Preprocessing Pipeline

Unlike traditional ANPR systems that rely on a single preprocessing technique, this module evaluates several preprocessing methods before OCR.

The implemented preprocessing strategies include:

- Static Preprocessing (Grayscale + OTSU + Morphology)
- CLAHE-Based Enhancement
- Gamma Correction
- Resolution Enhancement & Sharpening

Each strategy generates a different processed image. OCR is performed on every output independently.

![Preprocessing Pipeline](docs/images/preprocessing.png)

---

# 🎯 OCR Confidence-Based Selection

Each preprocessed image is passed to EasyOCR.

Instead of accepting the first OCR result, the module compares the confidence score of every recognized plate and automatically selects the result with the highest confidence.

This adaptive selection significantly improves recognition accuracy under varying environmental conditions.

![OCR Confidence Selection](docs/images/ocr-selection.png)

---

# ⚙️ Queue-Based Processing

To support scalable processing, the module follows a queue-based workflow.

The queue architecture allows multiple vehicle images to be processed sequentially while keeping the preprocessing module independent from other ANPR components such as APIs and databases.

This modular design simplifies future integration with real-time systems.

![Queue Processing](docs/images/queue-system.png)

---

# 📈 Performance Evaluation

The preprocessing module is evaluated using several metrics:

- OCR Confidence
- Character Recognition Accuracy
- Plate Recognition Accuracy
- Processing Time
- Strategy Selection Performance

These metrics help compare preprocessing strategies and demonstrate the effectiveness of the self-optimizing framework.

![Performance Evaluation](docs/images/evaluation.png)

---

# 🔍 Comparison with Conventional Approach

Traditional ANPR systems usually depend on a single preprocessing method, which may perform poorly under different lighting and environmental conditions.

The proposed framework evaluates multiple preprocessing strategies automatically and selects the most suitable result based on OCR confidence, improving robustness and recognition performance.

![Comparison](docs/images/comparison.png)

---

# 💡 Key Innovation

The core contribution of this project is the **Self-Optimizing Preprocessing Framework**, which:

- Applies multiple preprocessing strategies to the same license plate.
- Executes OCR on every processed image.
- Compares OCR confidence scores automatically.
- Selects the best preprocessing strategy dynamically.
- Performs character correction and license plate validation before producing the final result.

This approach removes the need to manually choose a preprocessing technique and makes the recognition pipeline more adaptive to real-world conditions.

---

# ⚙️ Installation

Follow these steps to set up the project on your local machine.

## Prerequisites

Ensure the following software is installed:

- Python 3.10 or later
- Git
- Visual Studio Code (Recommended)
- pip (Python Package Manager)

---

## Clone the Repository

```bash
git clone https://github.com/sejal13-dev/ANPR-Self-Optimizing-Preprocessing.git
```

Move into the project directory:

```bash
cd ANPR-Self-Optimizing-Preprocessing
```

---

## Install Required Libraries

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Required Models

Place the following YOLO models inside the **models/** directory.

```
models/
│
├── yolov8n.pt
└── plates_model_v1.pt
```

---

## Run the Project

Execute the following command:

```bash
python src/main.py
```

---

# ▶️ Usage

The complete execution flow is shown below.

### Step 1

Place one or more vehicle images inside:

```
sample_images/
```

---

### Step 2

Run

```bash
python src/main.py
```

---

### Step 3

The application performs the following sequence automatically:

- Load Vehicle Image
- Detect License Plate
- Crop License Plate
- Apply Four Preprocessing Strategies
- Execute EasyOCR
- Compare OCR Confidence
- Select Best Strategy
- Apply Character Correction
- Validate Indian License Plate
- Display Final Result

---

### Step 4

Generated results are saved inside

```
output/
```

---

# 📸 Sample Processing Flow

The preprocessing module follows the pipeline below.

```
Vehicle Image
        │
        ▼
YOLO Plate Detection
        │
        ▼
Crop License Plate
        │
        ▼
Apply 4 Preprocessing Strategies
        │
        ▼
EasyOCR
        │
        ▼
Confidence Comparison
        │
        ▼
Character Correction
        │
        ▼
Final License Plate
```

---

# 📊 Expected Output

The application displays:

- Original Vehicle Image
- Cropped License Plate
- Selected Preprocessed Image
- OCR Confidence Score
- Final Recognized License Plate

Example:

```
Vehicle Detected

Detected Plate

KA01AB1234

OCR Confidence : 96.42%

Selected Strategy :

CLAHE + Adaptive Threshold
```

---

# 📂 Additional Documentation

Detailed project documentation is available inside the **docs/** directory.

| Document | Description |
|----------|-------------|
| architecture.md | System Architecture |
| installation.md | Installation Guide |
| usage.md | Usage Guide |
| project-structure.md | Folder Structure |
| future-work.md | Planned Enhancements |
| contribution.md | Individual Contribution |

---

# 📈 Performance Highlights

The proposed preprocessing module provides the following advantages:

- Improved OCR Accuracy
- Automatic Strategy Selection
- Reduced Manual Parameter Tuning
- Better Performance under Different Lighting Conditions
- Modular Integration with Existing ANPR Systems
- Confidence-Based OCR Decision Making

---

# 🧩 Design Philosophy

The preprocessing module has been designed as an independent component that can be integrated into any Automatic Number Plate Recognition (ANPR) pipeline.

By separating preprocessing from detection, APIs, and backend services, the module becomes reusable, maintainable, and easier to extend in future applications.

---

# 🚀 Future Improvements

Although the current preprocessing module achieves strong OCR performance, several enhancements can further improve the project.

## Planned Enhancements

- 🎥 Real-time webcam and CCTV support
- 📹 Video stream processing
- 🚗 Multi-vehicle simultaneous processing
- 🌙 Better low-light and night-time enhancement
- ☁️ Cloud deployment (AWS / Azure / GCP)
- 🌐 REST API using FastAPI
- 🖥️ Interactive Web Dashboard
- 🐳 Docker containerization
- ⚡ GPU optimization using CUDA
- 🌍 Multi-country license plate recognition
- 🤖 Deep Learning-based image enhancement models

---

# 🤝 My Contribution

This repository contains **my individual contribution** to a team-based Automatic Number Plate Recognition (ANPR) project.

### My Responsibilities

- Designed and implemented the Self-Optimizing Preprocessing Pipeline.
- Developed multiple OpenCV preprocessing strategies.
- Integrated EasyOCR for character recognition.
- Implemented OCR confidence comparison.
- Automatically selected the best preprocessing strategy.
- Applied character correction for common OCR errors.
- Performed Indian license plate validation.
- Prepared project documentation and GitHub repository.

### Note

Vehicle detection, API integration, backend services, and database-related modules were developed by other team members.

This repository focuses exclusively on the preprocessing and OCR enhancement module developed by me.

---

# 📚 References

This project uses the following open-source libraries and frameworks:

- Python
- OpenCV
- EasyOCR
- NumPy
- PyTorch
- Ultralytics YOLOv8

Special thanks to the developers and maintainers of these open-source projects.

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more details.

---

# 👩‍💻 Author

**Sejal Priya**

MCA Student

Aspiring AI Engineer | Java Full Stack Developer

🔗 GitHub: https://github.com/sejal13-dev

---

# 🙏 Acknowledgements

I would like to express my gratitude to:

- The open-source community for providing excellent tools and libraries.
- The Ultralytics team for YOLOv8.
- The EasyOCR development team.
- OpenCV contributors.
- My project guide and faculty members for their valuable guidance.
- My teammates for their collaboration on the overall ANPR project.

---

# ⭐ Repository Information

If you found this project useful or interesting:

- ⭐ Star this repository.
- 🍴 Fork it for your own experiments.
- 💡 Feel free to explore the documentation.
- 🤝 Suggestions and constructive feedback are always welcome.

---

# 📌 Final Note

This repository demonstrates the implementation of a **Self-Optimizing Preprocessing Framework** for Automatic Number Plate Recognition (ANPR).

The primary objective of this work is to improve OCR accuracy by dynamically selecting the most suitable preprocessing strategy using OCR confidence scores.

The project has been designed as a modular component so that it can be integrated into larger ANPR systems, research projects, or intelligent transportation applications.