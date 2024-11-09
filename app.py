import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
with open("liver-disease.pkl", 'rb') as f:
    model = pickle.load(f)

# Define the function to get predictions
def predict_disease(input_data):
    prediction = model.predict(input_data)[0]
    if prediction == 0.0:
        return "Cirrhosis"
    elif prediction == 1.0:
        return "Fibrosis"
    elif prediction == 2.0:
        return "Hepatitis"
    elif prediction == 3.0:
        return "No Disease"
    else:
        return "Suspect Disease"

# Streamlit app
st.title("Liver Disease Prediction")

st.markdown("""
### Please enter the patient's information:
""")

# Collecting user inputs
Age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)
Sex = st.selectbox("Select Gender", options=["Female", "Male"])  # Clearer label
sex_value = 0 if Sex == "Female" else 1
albumin = st.number_input("Albumin", value=4.0)
alkaline_phosp = st.number_input("Alkaline Phosphatase", value=80.0)
alanine_aminotransferase = st.number_input("Alanine Aminotransferase", value=30.0)
asparate_aminotransferase = st.number_input("Aspartate Aminotransferase", value=35.0)
bilirubin = st.number_input("Bilirubin", value=1.0)
cholinesterase = st.number_input("Cholinesterase", value=6.0)
cholesterol = st.number_input("Cholesterol", value=200.0)
creatinina = st.number_input("Creatinine", value=1.0)
gamma_glutamyl_transferase = st.number_input("Gamma-Glutamyl Transferase", value=30.0)
protein = st.number_input("Protein", value=7.0)

# Prepare input data for prediction
user_input = np.array([[Age, sex_value, albumin, alkaline_phosp,
                        alanine_aminotransferase, asparate_aminotransferase,
                        bilirubin, cholinesterase, cholesterol, creatinina,
                        gamma_glutamyl_transferase, protein]])

# Make prediction
if st.button("Predict"):
    prediction = predict_disease(user_input)
    st.success(f"The predicted condition is: **{prediction}**")
