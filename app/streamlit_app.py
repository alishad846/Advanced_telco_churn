import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from scripts.utils import load_model
from scripts.preprocess import preprocess_input

st.set_page_config(page_title="Telco Churn Predictor", page_icon="📉", layout="wide")


st.title("📉 Telco Customer Churn Prediction")
st.markdown("Fill in customer details below:")

model = load_model()

with st.form("churn_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior = st.selectbox("Senior Citizen", ["No", "Yes"])
        partner = st.selectbox("Has Partner?", ["No", "Yes"])
        dependents = st.selectbox("Has Dependents?", ["No", "Yes"])
        tenure = st.slider("Tenure (months)", 0, 72, 12)
        monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=1000.0, value=70.0)

    with col2:
        phone_service = st.selectbox("Phone Service", ["Yes", "No"])
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
        payment_method = st.selectbox("Payment Method", [
            "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
        ])

    submitted = st.form_submit_button("🔍 Predict Churn")

    if submitted:
        input_data = pd.DataFrame({
            'gender': [gender],
            'SeniorCitizen': [1 if senior == "Yes" else 0],
            'Partner': [partner],
            'Dependents': [dependents],
            'tenure': [tenure],
            'PhoneService': [phone_service],
            'InternetService': [internet_service],
            'Contract': [contract],
            'PaperlessBilling': [paperless_billing],
            'PaymentMethod': [payment_method],
            'MonthlyCharges': [monthly_charges],
        })

        processed = preprocess_input(input_data)
        result = model.predict(processed)[0]
        st.success(f"🔔 Prediction: {'Churn' if result == 1 else 'Not Churn'}")


