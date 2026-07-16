# Installation Guide

This guide explains how to set up and run the ANPR Self-Optimizing Preprocessing project on your local machine.

---

## Prerequisites

Before running the project, install the following:

- Python 3.10 or above
- Git
- Visual Studio Code (recommended)
- pip (Python package manager)

---

## Clone the Repository

```bash
git clone https://github.com/sejal13-dev/ANPR-Self-Optimizing-Preprocessing.git
```

Go to the project folder:

```bash
cd ANPR-Self-Optimizing-Preprocessing
```

---

## Install Dependencies

Install all required Python libraries:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
ANPR-Self-Optimizing-Preprocessing/
│
├── docs/
├── models/
├── sample_images/
├── src/
├── requirements.txt
├── README.md
```

---

## Download Required Models

Place the following model files inside the `models` folder:

- yolov8n.pt
- plates_model_v1.pt

---

## Run the Project

Execute:

```bash
python src/main.py
```

---

## Expected Output

The system will:

- Detect the vehicle
- Detect the license plate
- Crop the plate
- Apply four preprocessing strategies
- Run EasyOCR
- Compare OCR confidence
- Select the best result
- Display the final recognized license plate

---

## Troubleshooting

If dependencies are missing:

```bash
pip install -r requirements.txt
```

If the model files are missing, place them in the `models` directory before running the project.