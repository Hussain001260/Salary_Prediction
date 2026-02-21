import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("salary_model.pkl")
columns = joblib.load("model_columns.pkl")

st.set_page_config(page_title="Salary Prediction App", layout="centered")
st.title("💼 Salary Prediction System")

st.write("Enter the employee details to predict salary.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=65, value=30)
experience = st.number_input("Years of Experience", min_value=0.0, max_value=40.0, value=5.0)

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
education = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
job = st.text_input("Job Title", "Software Engineer")

if st.button("Predict Salary"):
    row = pd.DataFrame(columns=columns)
    row.loc[0] = 0

    row.at[0, 'Age'] = age
    row.at[0, 'Years of Experience'] = experience

    g_col = f"Gender_{gender}"
    e_col = f"Education Level_{education}"
    j_col = f"Job Title_{job}"

    if g_col in row.columns:
        row.at[0, g_col] = 1
    if e_col in row.columns:
        row.at[0, e_col] = 1
    if j_col in row.columns:
        row.at[0, j_col] = 1

    prediction = model.predict(row)[0]
    st.success(f"Predicted Salary: {int(prediction):,}")
