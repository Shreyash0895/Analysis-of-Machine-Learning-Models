-------------------------------------------------------------------------

🌱 Green AI Model Comparison Framework Accuracy vs Energy Consumption

-------------------------------------------------------------------------

📌 Project Overview

This project implements a dataset-agnostic Green AI framework that evaluates and compares multiple machine learning models based on both prediction accuracy and computational energy consumption.
Unlike traditional ML projects that focus only on accuracy, this system emphasizes sustainability by measuring training time, inference time, CPU usage, and memory consumption.

The framework allows users to upload any CSV dataset through a Streamlit-based user interface, automatically preprocess the data, detect the task type (regression or classification), train multiple machine learning models, and visualize comparative results.
-------------------------------------------------------------------------

🎯 Objectives

-Enable users to upload any structured dataset
-Automatically identify regression or classification problems
-Compare multiple ML models on:
-Accuracy metrics
-Energy and resource usage
-Promote Green AI principles through energy-aware model selection
-Provide a clean, interactive visualization dashboard
-------------------------------------------------------------------------

🧠 Machine Learning Models Used

-Linear Regression / Logistic Regression
-Decision Tree
-Random Forest
-Support Vector Machine (SVR / SVM)
-------------------------------------------------------------------------

📊 Evaluation Metrics

-Performance Metrics
-Regression: R² Score, RMSE, MAE
-Classification: Accuracy, F1 Score
-Energy & Resource Metrics
-Training Time
-Inference Time
-CPU Usage
-Memory Usage
-------------------------------------------------------------------------

🗂️ Project Directory Structure

Your current structure:

GREENAI_Model/
│
├── __pycache__/
│
├── data/
│   ├── raw/
│   │   └── user_dataset.csv
│   └── processed/
│       └── cleaned_data.csv
│
├── notebooks/
│   └── experiments.ipynb
│
├── report/
│   └── PPT/
│
├── results/
│   ├── graphs/
│   └── metrics.csv
│
├── src/
│   ├── __init__.py
│   ├── data_validation.py
│   ├── energy_metrics.py
│   ├── estimation.py
│   ├── model_training.py
│   ├── preprocessing.py
│   ├── recommendation.py
│   └── task_detection.py
│
├── ui/
│   ├── __init__.py
│   ├── app.py
│   └── ui_helpers.py
│
├── main.py
├── README.md
└── requirements.txt
-------------------------------------------------------------------------

⚙️ System Requirements

OS: Windows 10 / Windows 11

Python: 3.8 or above

RAM: Minimum 8 GB recommended
-------------------------------------------------------------------------

📦 Installation

Install all required dependencies using:

pip install -r requirements.txt

Or manually:

pip install pandas numpy scikit-learn psutil streamlit
-------------------------------------------------------------------------

🚀 How to Run the Project (Final Method)
🔹 Step 1: Open Project Folder

Open the project root folder (GreenAI_Model) in VS Code.

🔹 Step 2: Run the Application

From the project root directory, run:

streamlit run ui/app.py

🔹 Step 3: Use the Application

Upload a CSV dataset

Preview the dataset

Select the target column

Click Run Analysis

View model comparison results and energy metrics
-------------------------------------------------------------------------

🧠 Execution Flow
User → Streamlit UI → Dataset Upload
     → Validation → Preprocessing
     → Task Detection
     → Model Training
     → Accuracy & Energy Evaluation
     → Visualization & Comparison
-------------------------------------------------------------------------

🌱 Green AI Principles Applied

Reduced computation through efficient preprocessing

Comparison beyond accuracy to include energy consumption

Promotion of simpler, energy-efficient models when suitable

Dataset-agnostic design to avoid overfitting to a single use case
-------------------------------------------------------------------------

🧪 Notes

The project is executed through app.py

main.py acts as the backend processing engine

Text-based datasets may require additional preprocessing (future enhancement)

Always run the UI from the project root directory
-------------------------------------------------------------------------

🗣️ One-Line Project Summary

A dataset-agnostic Green AI framework that compares machine learning models based on accuracy and energy efficiency using an interactive user interface.
-------------------------------------------------------------------------

📄 License

This project is intended for educational and internship purposes only.