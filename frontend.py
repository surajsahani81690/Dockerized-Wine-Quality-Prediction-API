import streamlit as st
import requests
import pandas as pd
from model.model_prediction import model_prediction

API_URL = "http://127.0.0.1:8000/predict"
st.set_page_config(page_title="Wine Quality Predictor", layout="centered")

st.title("🍷 Wine Quality Prediction")
st.markdown("Enter the wine chemical properties to predict quality")

# Input fields
fixed_acidity = st.number_input("Fixed Acidity", min_value=0.01,value = 7.1)
volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, value=0.65)
citric_acid = st.number_input("Citric Acid", min_value=0.0, value=0.06)
residual_sugar = st.number_input("Residual Sugar", min_value=0.0, value=1.9)
chlorides = st.number_input("Chlorides", min_value=0.0, value=0.065)
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, value=15.0)
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, value = 40.0)
density = st.number_input("Density", min_value=0.0, value=0.9978)
pH = st.number_input("pH", min_value=0.0, value=3.52)
sulphates = st.number_input("Sulphates", min_value=0.0, value = 0.56)
alcohol = st.number_input("Alcohol (%)", min_value=0.0, value=9.8)

# Predict button
if st.button("Predict Quality"):
    input_data = {
        "fixed_acidity": fixed_acidity,
        "volatile_acidity": volatile_acidity,
        "citric_acid": citric_acid,
        "residual_sugar": residual_sugar,
        "chlorides": chlorides,
        "free_sulfur_dioxide": free_sulfur_dioxide,
        "total_sulfur_dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": pH,
        "sulphates": sulphates,
        "alcohol": alcohol}
    result = model_prediction(input_data)
    if "error" in result:
        st.error("Prediction failed: " + result["error"])
    else:
        # Display predicted category
        st.success(f"Predicted category: {result['predicted_category']}")
    
        # Display confidence
        st.info(f"Confidence: {result['confidence'] * 100:.2f}%")
    
        # Display class probabilities
        st.write("Class Probabilities:")
        for cls, prob in result["class_probabilities"].items():
            st.write(f"Class {cls}: {prob * 100:.2f}%")
