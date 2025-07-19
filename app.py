import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("heart_model.pkl", "rb"))

st.title("💓 Heart Disease Prediction App")
st.subheader("Provide the patient's health details below:")

# Input form
age = st.number_input("Age", min_value=1, max_value=120, step=1)
sex = st.selectbox("Sex", ["Male", "Female"])
chest_pain = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
rest_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0)
cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=0)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
resting_ecg = st.selectbox("Resting ECG Result", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=0)
exercise_angina = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
oldpeak = st.number_input("Oldpeak (ST Depression)", min_value=0.0, format="%.2f")
st_slope = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])

# Manual encoding
sex_map = {"Male": 1, "Female": 0}
cp_map = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}
fbs_map = {"Yes": 1, "No": 0}
restecg_map = {"Normal": 0, "ST-T Wave Abnormality": 1, "Left Ventricular Hypertrophy": 2}
exang_map = {"No": 0, "Yes": 1}
slope_map = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}

# Create input array
input_data = np.array([
    age,
    sex_map[sex],
    cp_map[chest_pain],
    rest_bp,
    cholesterol,
    fbs_map[fasting_bs],
    restecg_map[resting_ecg],
    max_hr,
    exang_map[exercise_angina],
    oldpeak,
    slope_map[st_slope]
]).reshape(1, -1)

# Predict
if st.button("Predict"):
    result = model.predict(input_data)
    if result[0] == 1:
        st.error("⚠️ High Risk of Heart Disease!")
    else:
        st.success("✅ Low Risk of Heart Disease.")
