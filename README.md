💓 Heart Disease Prediction Using Machine Learning
This project is a machine learning-based heart disease prediction system developed using Python. The application takes various health-related inputs from the user and predicts the likelihood of heart disease using a trained classification model.

🔍 Objective
To build a reliable and user-friendly machine learning model that predicts whether a patient is likely to develop heart disease based on various medical parameters.

📊 Features
Trained using real-world heart disease data

Predicts risk of heart disease (Low/High)

Simple web interface using Streamlit

Machine learning pipeline using Scikit-learn

Model saved using joblib/pickle for reusability

 Model Details
Algorithm Used: Logistic Regression (or similar classifier)

Dataset Source: UCI Heart Disease dataset

Evaluation Metrics: Accuracy, Confusion Matrix, etc.

🛠️ How to Run the Project
1. Install Dependencies
pip install -r requirements.txt
2. Train the Model
python train_model.py
3. Run the Web App
streamlit run app.py

🧪 Input Parameters
Parameter	Description

Age	Patient's age

Sex	Male/Female

Chest Pain Type	Type of chest pain

Resting Blood Pressure	Measured in mm Hg

Cholesterol	Serum cholesterol in mg/dl

Fasting Blood Sugar	>120 mg/dl (Yes/No)

Resting ECG	ECG results

Max Heart Rate	Maximum heart rate achieved

Exercise Induced Angina	Yes/No

Oldpeak	ST depression

ST Slope	Slope of peak exercise ST segment


 
