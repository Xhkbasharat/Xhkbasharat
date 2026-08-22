# Explainable AI for Pneumonia Detection Using Chest X-Ray Images

An AI-powered web-based medical image analysis system designed to assist in the detection of pneumonia from chest X-ray images. The project combines deep learning, lung segmentation, ensemble classification, and Explainable Artificial Intelligence (XAI) to provide predictions together with visual explanations using Grad-CAM.

> **Note:** This project is intended for academic/research purposes and is not a replacement for professional medical diagnosis.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Objectives](#objectives)
4. [Key Features](#key-features)
5. [System Architecture](#system-architecture)
6. [Project Workflow](#project-workflow)
7. [Technologies Used](#technologies-used)
8. [Datasets](#datasets)
9. [Data Preprocessing](#data-preprocessing)
10. [Lung Segmentation](#lung-segmentation)
11. [Pneumonia Classification](#pneumonia-classification)
12. [Ensemble Prediction](#ensemble-prediction)
13. [Explainable AI with Grad-CAM](#explainable-ai-with-grad-cam)
14. [Confidence and Severity](#confidence-and-severity)
15. [AI Challenge Mode](#ai-challenge-mode)
16. [Web Application](#web-application)
17. [Patient Management](#patient-management)
18. [PDF Report Generation](#pdf-report-generation)
19. [Dashboard](#dashboard)
20. [Database](#database)
21. [Project Structure](#project-structure)
22. [Installation](#installation)
23. [Running the Application](#running-the-application)
24. [Example Workflow](#example-workflow)
25. [Advantages](#advantages)
26. [Limitations](#limitations)
27. [Future Enhancements](#future-enhancements)
28. [Academic Contribution](#academic-contribution)
29. [Conclusion](#conclusion)

---

## Project Overview

**Explainable AI for Pneumonia Detection Using Chest X-Ray Images** is a deep-learning-based medical image analysis project developed to detect pneumonia from chest X-ray images.

Traditional deep-learning systems can provide highly accurate predictions but may behave like a "black box", making it difficult for users to understand why a particular prediction was produced. This project addresses that limitation by integrating **Explainable Artificial Intelligence (XAI)** into the pneumonia detection pipeline.

The system processes a chest X-ray, identifies the lung region using a **U-Net segmentation model**, passes the processed image through multiple deep-learning classification models, combines their predictions using an ensemble strategy, and generates a **Grad-CAM heatmap** showing the image regions that contributed most strongly to the prediction.

The complete system is deployed through a **Flask-based web application** with patient management, prediction history, dashboard analytics, report generation, image quality validation, webcam capture, and an AI Challenge Mode for robustness testing.

---

## Problem Statement

Pneumonia is a respiratory infection that can affect one or both lungs. Chest X-ray imaging is commonly used as part of the clinical assessment of pneumonia.

Manual interpretation of X-ray images requires expertise and can be time-consuming. Deep learning can assist in image classification, but a prediction without an explanation may be difficult for users to interpret or trust.

The project therefore focuses on developing a system that:

- Detects pneumonia from chest X-ray images.
- Focuses analysis on the lung region.
- Combines multiple deep-learning models.
- Provides confidence information.
- Generates visual explanations using Grad-CAM.
- Evaluates prediction robustness under controlled image variations.
- Maintains patient and prediction history.
- Provides a web-based interface for practical use.

---

## Objectives

The major objectives of the project are:

1. Develop an AI-based pneumonia detection system using chest X-ray images.
2. Apply lung segmentation before classification.
3. Use multiple deep-learning models for classification.
4. Combine model predictions using ensemble learning.
5. Integrate Grad-CAM for visual explainability.
6. Display prediction confidence and severity information.
7. Evaluate model robustness using AI Challenge Mode.
8. Develop a Flask-based web application.
9. Maintain patient and prediction history using SQLite.
10. Generate professional PDF reports.
11. Provide dashboard analytics for system usage.
12. Create a user-friendly interface for uploading and analysing X-ray images.

---

## Key Features

### 1. AI-Based Pneumonia Detection

The system analyses chest X-ray images and classifies them into:

- NORMAL
- PNEUMONIA

### 2. Lung Segmentation

A U-Net model is used to identify the lung region before classification.

### 3. Ensemble Deep Learning

Multiple classification models are used and their predictions are averaged to produce the final prediction.

### 4. Explainable AI

Grad-CAM generates a heatmap that highlights regions of the X-ray that contributed to the model's decision.

### 5. Confidence Score

The system displays a percentage-based confidence value associated with the predicted class.

### 6. Severity Classification

For pneumonia predictions, the application provides an application-level severity category based on the confidence threshold configured in the project.

### 7. AI Challenge Mode

The system creates controlled image variations such as brightness changes, contrast changes, rotation, blur, and noise and checks whether the prediction remains consistent.

### 8. Patient Management

Patient details and prediction history can be stored and managed through the web application.

### 9. Dashboard

The dashboard provides information such as:

- Total patients
- Total scans
- Pneumonia detections
- Normal detections
- Recent uploads
- Model usage statistics
- System status

### 10. PDF Reports

A professional report can contain:

- Patient details
- Prediction
- Confidence score
- Severity
- Original X-ray
- Grad-CAM visualization

### 11. Webcam Capture

The application can support capturing an image through a webcam before analysis.

### 12. Image Quality Validation

The system can validate uploaded images before sending them through the prediction pipeline.

---

## System Architecture

The overall system can be represented as:

```text
                +----------------------+
                |      User / Admin    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Flask Web Interface |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Image Upload/Capture |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Image Preprocessing   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  U-Net Lung          |
                |  Segmentation        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Segmented X-Ray      |
                +----------+-----------+
                           |
                           v
        +------------------+------------------+
        |                  |                  |
        v                  v                  v
   DenseNet121        DenseNet201          Xception
        |                  |                  |
        +------------------+------------------+
                           |
             +-------------+-------------+
             |                           |
             v                           v
      EfficientNetB3              MobileNetV2
             |                           |
             +-------------+-------------+
                           |
                           v
                +----------------------+
                | Ensemble Prediction  |
                +----------+-----------+
                           |
              +------------+------------+
              |                         |
              v                         v
      Prediction/Confidence       Grad-CAM XAI
              |                         |
              +------------+------------+
                           |
                           v
                +----------------------+
                | Result & Explanation |
                +----------+-----------+
                           |
             +-------------+-------------+
             |                           |
             v                           v
       Patient History             PDF Report
             |
             v
          SQLite
```

---

## Project Workflow

The main workflow is:

```text
User Login
    ↓
Dashboard
    ↓
Upload / Capture X-Ray
    ↓
Image Quality Validation
    ↓
Image Preprocessing
    ↓
Lung Segmentation using U-Net
    ↓
Segmented Lung Image
    ↓
Multiple Deep Learning Models
    ↓
Ensemble Prediction
    ↓
Pneumonia / Normal Result
    ↓
Confidence Calculation
    ↓
Severity Classification
    ↓
Grad-CAM Heatmap
    ↓
Robustness Testing
    ↓
Save Patient History
    ↓
Generate PDF Report
```

---

## Technologies Used

### Programming Language

- Python

### Backend

- Flask

### Machine Learning / Deep Learning

- TensorFlow
- Keras
- Convolutional Neural Networks
- Transfer Learning
- Ensemble Learning

### Computer Vision

- OpenCV
- Image preprocessing
- Image augmentation
- Grad-CAM visualization

### Frontend

- HTML5
- CSS3
- JavaScript

### Database

- SQLite

### Additional Components

- PDF report generation
- QR code generation
- Webcam capture
- Dashboard analytics
- Medical awareness module
- Weather integration
- Medical news feed
- AI chatbot interface

---

## Datasets

The project uses chest X-ray and lung segmentation datasets.

### Kaggle Chest X-Ray Dataset

The pneumonia classification dataset used during development contains chest X-ray images belonging to:

- Normal
- Pneumonia

A commonly referenced dataset split contains:

- Total images: 5,216
- Normal images: 1,341
- Pneumonia images: 3,875

Dataset organization and counts should be verified against the exact dataset version used in the final experiment.

### Shenzhen Lung Segmentation Dataset

A lung segmentation dataset is used to support training/evaluation of lung-region segmentation.

The segmentation data includes X-ray images and corresponding lung masks/annotations.

---

## Data Preprocessing

Before classification, X-ray images undergo preprocessing.

Typical preprocessing steps include:

1. Loading the X-ray image.
2. Converting the image into the required format.
3. Resizing the image to the model input size.
4. Normalizing pixel values.
5. Applying lung segmentation.
6. Applying the lung mask to focus analysis on the relevant region.
7. Preparing the processed image for classification.

The classification pipeline uses a target image size of **224 × 224 pixels** for the configured models.

---

## Lung Segmentation

Lung segmentation is performed using a **U-Net-based segmentation model**.

The purpose of segmentation is to isolate the lung region from surrounding areas.

### Segmentation Process

```text
Original X-Ray
      ↓
Preprocessing
      ↓
U-Net Model
      ↓
Predicted Lung Mask
      ↓
Mask Processing
      ↓
Lung Region Extraction
      ↓
Segmented X-Ray
```

The segmentation model used in the project can be stored as:

```text
lung_segmentation_unet.h5
```

The resulting mask is also used to restrict explainability analysis to the lung region.

---

## Pneumonia Classification

The project uses multiple deep-learning classification models.

The model ensemble configured in the project includes:

- DenseNet121
- DenseNet201
- Xception
- EfficientNetB3
- MobileNetV2

Example model files include:

```text
model.h5
densenet201_model.h5
xception_model.h5
efficientnetb3_model.h5
mobilenetv2_model.h5
```

The models analyse the segmented X-ray and produce prediction scores.

---

## Ensemble Prediction

Instead of relying on a single classifier, the project combines predictions from five models.

The configured ensemble prediction is conceptually:

```text
Final Score =
(DenseNet121 + DenseNet201 + Xception +
 EfficientNetB3 + MobileNetV2) / 5
```

The resulting score is compared with the configured classification threshold.

For example:

```text
If score >= 0.5
        → PNEUMONIA

If score < 0.5
        → NORMAL
```

This ensemble approach is intended to reduce dependence on the behaviour of a single model.

---

## Explainable AI with Grad-CAM

One of the main contributions of this project is the integration of **Explainable Artificial Intelligence**.

### Why Grad-CAM?

Deep neural networks can make predictions based on complex internal feature representations. Grad-CAM helps visualize the image regions that had a strong influence on the prediction.

### Grad-CAM Workflow

```text
Input X-Ray
    ↓
Classification Model
    ↓
Target Convolutional Layer
    ↓
Gradient Calculation
    ↓
Feature Map Weighting
    ↓
Grad-CAM Heatmap
    ↓
Heatmap + X-Ray
    ↓
Visual Explanation
```

The heatmap is superimposed on the original X-ray to create an interpretable visualization.

### Lung-Restricted Explainability

The project additionally uses the lung segmentation mask to restrict the Grad-CAM analysis to the relevant lung region.

This helps reduce attention to irrelevant areas outside the lungs.

---

## Confidence and Severity

The system calculates a confidence percentage from the ensemble prediction.

Conceptually:

```text
PNEUMONIA:
Confidence = prediction × 100

NORMAL:
Confidence = (1 - prediction) × 100
```

The application also categorizes pneumonia predictions into configured severity levels.

Example threshold logic used in the application:

```text
Confidence >= 90%
    → High

Confidence >= 70%
    → Medium

Otherwise
    → Low
```

These categories represent the application's confidence-based classification and should not be interpreted as a clinical assessment of disease severity.

---

## AI Challenge Mode

The project includes an **AI Challenge Mode** designed to evaluate prediction consistency.

The system generates controlled variations of the input image.

Examples include:

- Brightness increase
- Brightness decrease
- Contrast increase
- Contrast decrease
- Small image rotation
- Blur
- Noise

The original image and challenge variants are passed through the prediction pipeline.

### Robustness Score

The robustness score represents the percentage of challenge images that produce the same prediction as the original image.

Conceptually:

```text
Robustness Score =
(Number of consistent predictions /
 Total challenge images) × 100
```

This provides an additional experimental measure of prediction stability.

---

## Web Application

The system is implemented as a Flask-based web application.

### Main Modules

#### Login Module

Provides secure access to the application.

#### Welcome Page

Provides an introduction to the system.

#### AI Dashboard

Displays system statistics and recent activity.

#### X-Ray Upload

Allows users to upload chest X-ray images.

#### Webcam Capture

Provides an interface for capturing an image through a connected webcam.

#### Prediction Module

Processes the image through segmentation and classification.

#### Result Display

Shows:

- Prediction
- Confidence
- Severity category
- Grad-CAM visualization
- Robustness information

#### Patient History

Stores and displays previous patient scans.

#### Medical News

Provides a medical news feed where configured.

#### Weather Module

Provides live weather information where configured.

#### AI Chatbot

Provides an interface for AI-based assistance where configured.

#### Pneumonia Awareness

Displays educational information about pneumonia.

#### Feedback

Allows users to submit feedback.

#### Settings

Provides configurable application options.

#### Logout

Ends the user session.

---

## Patient Management

The system includes a patient management module.

Patient records can include:

- Patient ID
- Name
- Age
- Gender
- Contact details
- Upload date
- Prediction
- Confidence
- Severity
- Prediction history
- Generated reports

Administrative operations can include:

- Add
- View
- Search
- Edit
- Delete

This allows the system to maintain an organized record of previous analyses.

---

## PDF Report Generation

The application can generate a professional PDF report after analysis.

The report may include:

```text
Patient Information
        ↓
Prediction Result
        ↓
Confidence Score
        ↓
Severity Category
        ↓
Original X-Ray
        ↓
Grad-CAM Heatmap
        ↓
Analysis Information
```

The report provides a convenient record of the AI analysis.

> The report should clearly state that the output is an AI-assisted prediction for academic/research use and is not a medical diagnosis.

---

## Dashboard

The dashboard provides an overview of system activity.

Possible dashboard statistics include:

- Total Patients
- Total Scans
- Pneumonia Detections
- Normal Detections
- Recent Uploads
- Model Usage
- System Health

The dashboard is designed to provide a centralized view of application activity.

---

## Database

The application uses **SQLite** for local data management.

A patient history table can contain fields such as:

```text
id
name
age
gender
prediction
confidence
severity
scan_date
image
```

Additional tables can be added for:

- Users
- Patients
- Applications/records
- Feedback
- Reports
- System settings

The exact schema should match the database implementation in the submitted source code.

---

## Project Structure

A suggested project structure is:

```text
Explainable-AI-Pneumonia-Detection/
│
├── app.py
├── model.h5
├── densenet201_model.h5
├── xception_model.h5
├── efficientnetb3_model.h5
├── mobilenetv2_model.h5
├── lung_segmentation_unet.h5
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── result.html
│   ├── patient_history.html
│   └── report.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   ├── heatmaps/
│   ├── reports/
│   └── qrcodes/
│
├── uploads/
│
├── models/
│
├── database/
│   └── patients.db
│
├── requirements.txt
│
└── README.md
```

The actual structure may vary depending on the final source code.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Explainable-AI-Pneumonia-Detection.git
cd Explainable-AI-Pneumonia-Detection
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If a requirements file is not available, install the dependencies required by the final source code, such as:

```bash
pip install flask tensorflow keras opencv-python numpy pillow matplotlib
```

Additional packages may be required depending on the implemented modules.

---

## Running the Application

Start the Flask application:

```bash
python app.py
```

The terminal will display the local development address.

Open the displayed address in a web browser.

For example:

```text
http://127.0.0.1:5000/
```

The exact URL and port depend on the Flask configuration.

---

## Example Prediction Workflow

### Step 1 — Login

The user logs into the application.

### Step 2 — Upload X-Ray

The user uploads a chest X-ray image.

### Step 3 — Image Validation

The system checks whether the uploaded image meets the required image conditions.

### Step 4 — Lung Segmentation

The U-Net model extracts the lung region.

### Step 5 — Classification

The segmented image is processed by the classification models.

### Step 6 — Ensemble

The individual model predictions are averaged.

### Step 7 — Result

The system displays:

```text
Prediction: PNEUMONIA / NORMAL
Confidence: XX%
Severity: LOW / MEDIUM / HIGH
```

### Step 8 — Explainability

Grad-CAM generates a heatmap showing important regions.

### Step 9 — Robustness

AI Challenge Mode evaluates prediction consistency under controlled variations.

### Step 10 — Save Record

The patient and prediction information can be stored in the database.

### Step 11 — Generate Report

A PDF report can be generated containing the analysis results and visualizations.

---

## Advantages

### Explainability

Grad-CAM provides a visual explanation rather than displaying only a classification label.

### Ensemble Learning

Multiple models are combined to reduce reliance on a single classifier.

### Lung-Focused Analysis

Segmentation helps focus the classification and explainability pipeline on the lung region.

### Robustness Evaluation

AI Challenge Mode provides an additional method for evaluating prediction consistency.

### Web-Based Interface

Users can interact with the system through a web application rather than a command-line interface.

### Patient History

Previous analyses can be stored and reviewed.

### Automated Reports

Results can be compiled into a structured PDF report.

### Modular Architecture

The application can be extended with additional models, datasets, and modules.

---

## Limitations

This project has several limitations that should be considered.

1. The system is an academic/research prototype and should not be used as a standalone clinical diagnostic tool.
2. Model performance depends on the quality and diversity of the training dataset.
3. Dataset bias may affect predictions on images from different hospitals, devices, populations, or acquisition protocols.
4. Grad-CAM provides an interpretation of model attention and does not prove that a highlighted region is the actual disease location.
5. Confidence scores should not be interpreted as clinical probabilities without proper calibration and validation.
6. The confidence-based severity category is an application-defined category, not a clinical severity assessment.
7. Real-world deployment requires extensive external validation and clinical evaluation.
8. Model files can be large and may require significant storage and computational resources.
9. GPU acceleration may be beneficial for faster inference and training.
10. Privacy, security, regulatory compliance, and clinical workflow integration would require additional work for real-world deployment.

---

## Future Enhancements

Possible future improvements include:

### Advanced Deep Learning Models

Integrate newer architectures such as:

- EfficientNetV2
- ConvNeXt
- Swin Transformer
- Vision Transformer

### Advanced Ensemble Learning

Experiment with weighted ensemble methods instead of simple averaging.

### Self-Supervised Learning

Use self-supervised pretraining to improve feature representation when labelled medical images are limited.

### Improved Lung Segmentation

Explore advanced segmentation architectures and stronger segmentation datasets.

### Multi-Class Classification

Extend the system beyond binary Normal/Pneumonia classification to identify additional lung conditions.

### Better Explainability

Integrate additional XAI methods such as:

- Integrated Gradients
- SHAP
- LIME
- Occlusion-based analysis

### Model Calibration

Add calibration methods so confidence values better represent prediction probabilities.

### External Validation

Evaluate the model on independent datasets from different sources.

### Security Improvements

Add stronger:

- Password hashing
- Role-based access control
- Session security
- File validation
- Data encryption
- Audit logging

### Cloud Deployment

Deploy the application using a cloud platform for controlled testing and collaboration.

### Mobile Application

Develop a mobile interface for authorized users.

---

## Academic Contribution

The project combines several concepts into a single end-to-end application:

```text
Medical Image Processing
          +
Deep Learning
          +
Lung Segmentation
          +
Ensemble Learning
          +
Explainable AI
          +
Robustness Evaluation
          +
Flask Web Development
          +
Database Management
          +
Automated Reporting
```

This makes the project suitable as an academic demonstration of how artificial intelligence, computer vision, explainability, and web application development can be integrated into a medical image analysis workflow.

---

## Conclusion

The **Explainable AI for Pneumonia Detection Using Chest X-Ray Images** project demonstrates an end-to-end approach to AI-assisted medical image analysis.

The system combines lung segmentation, multiple deep-learning classifiers, ensemble prediction, Grad-CAM explainability, confidence analysis, robustness testing, patient management, dashboard analytics, and PDF report generation within a Flask-based web application.

The primary focus of the project is not only to produce a pneumonia prediction but also to make the prediction more interpretable by showing the image regions that contributed to the model's decision.

The project provides a foundation for further research into reliable, explainable, and robust AI systems for medical image analysis.

---

## Disclaimer

This project is developed for **academic and research purposes**. It is not intended to replace qualified medical professionals, radiologists, or clinical diagnostic procedures. AI predictions and visual explanations should not be used as the sole basis for medical decisions.

---

## Author

**Sheikh Basharat Akbar**

Master of Computer Applications (MCA)

Islamic University of Science & Technology (IUST), Kashmir

Project: **Explainable AI for Pneumonia Detection Using Chest X-Ray Images**

