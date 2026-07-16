# 🚗 ANPR Self-Optimizing Preprocessing

An AI-based preprocessing module for Automatic Number Plate Recognition (ANPR) that improves OCR accuracy by applying multiple preprocessing techniques and selecting the best result automatically.

## 📌 Project Overview

This project is a preprocessing module of an Automatic Number Plate Recognition (ANPR) system.

The system detects vehicle number plates using YOLOv8 and improves character recognition by applying multiple image preprocessing techniques before performing OCR with EasyOCR.

Unlike traditional approaches that use only one preprocessing method, this project evaluates multiple preprocessing strategies and selects the best one based on OCR confidence.

## ✨ Features

- Vehicle Detection using YOLOv8
- License Plate Detection
- Self-Optimizing Image Preprocessing
- OCR using EasyOCR
- Character Correction
- Indian License Plate Validation
- Noise Reduction
- Image Enhancement

## 🛠 Technologies Used

- Python
- OpenCV
- YOLOv8
- EasyOCR
- NumPy
- PyTorch

## 📂 Project Structure

```
## 📂 Project Structure

```text
ANPR-Self-Optimizing-Preprocessing/
│
├── docs/
│   ├── architecture.md
│   └── images/
│       ├── workflow.png
│       ├── architecture.png
│       ├── preprocessing_pipeline.png
│       ├── preprocessing_strategies.png
│       ├── confidence_selection.png
│       ├── character_correction.png
│       └── complete_pipeline.png
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
└── README.md
```

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/sejal13-dev/ANPR-Self-Optimizing-Preprocessing.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python src/main.py
```

## 📊 Output

The system

- Detects vehicles
- Detects license plates
- Applies multiple preprocessing techniques
- Performs OCR
- Corrects common character mismatches
- Produces improved recognition results

## 🚀 Future Improvements

- Real-time camera support
- REST API integration
- Docker deployment
- Multi-threaded processing
- Web interface

## 👩‍💻 Author

Sejal Priya

MCA Student | AI & Java Full Stack Developer