import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('trainedLF2')

# Streamlit webpage
def main():
    st.title("Customer Churn Prediction")
    st.markdown("## Enter Customer Details to Predict Churn")

    # Layout: Create columns for better organization
    col1, col2, col3 = st.columns(3)

    with col1:
        # Continuous variables
        tenure = st.slider("Tenure (months)", 0, 72, 1)
        monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=20.0)
    
    with col2:
        total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=100.0)
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    
    with col3:
        dependents = st.radio("Dependents", ["Yes", "No"])
        device_protection = st.radio("Device Protection", ["Yes", "No", "No internet service"])

    # More columns for other inputs
    col4, col5, col6 = st.columns(3)

    with col4:
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        multiple_lines = st.radio("Multiple Lines", ["Yes", "No", "No phone service"])
    
    with col5:
        online_backup = st.radio("Online Backup", ["Yes", "No", "No internet service"])
        online_security = st.radio("Online Security", ["Yes", "No", "No internet service"])
    
    with col6:
        paperless_billing = st.radio("Paperless Billing", ["Yes", "No"])
        partner = st.radio("Partner", ["Yes", "No"])

    col7, col8 = st.columns(2)

    with col7:
        payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
        phone_service = st.radio("Phone Service", ["Yes", "No"])
    
    with col8:
        senior_citizen = st.radio("Senior Citizen", ["Yes", "No"])
        streaming_movies = st.radio("Streaming Movies", ["Yes", "No", "No internet service"])
    
    streaming_tv = st.radio("Streaming TV", ["Yes", "No", "No internet service"])
    tech_support = st.radio("Tech Support", ["Yes", "No", "No internet service"])
    gender = st.radio("Gender", ["Male", "Female"])

    if st.button('Predict'):
        # Convert inputs to the correct format
        # One-hot encoding for categorical variables
        features = {
            'tenure': [tenure],
            'MonthlyCharges': [monthly_charges],
            'TotalCharges': [total_charges],
            'Contract_One year': [1 if contract == "One year" else 0],
            'Contract_Two year': [1 if contract == "Two year" else 0],
            'Dependents_Yes': [1 if dependents == "Yes" else 0],
            'DeviceProtection_No internet service': [1 if device_protection == "No internet service" else 0],
            'DeviceProtection_Yes': [1 if device_protection == "Yes" else 0],
            'InternetService_Fiber optic': [1 if internet_service == "Fiber optic" else 0],
            'InternetService_No': [1 if internet_service == "No" else 0],
            'MultipleLines_No phone service': [1 if multiple_lines == "No phone service" else 0],
            'MultipleLines_Yes': [1 if multiple_lines == "Yes" else 0],
            'OnlineBackup_No internet service': [1 if online_backup == "No internet service" else 0],
            'OnlineBackup_Yes': [1 if online_backup == "Yes" else 0],
            'OnlineSecurity_No internet service': [1 if online_security == "No internet service" else 0],
            'OnlineSecurity_Yes': [1 if online_security == "Yes" else 0],
            'PaperlessBilling_Yes': [1 if paperless_billing == "Yes" else 0],
            'Partner_Yes': [1 if partner == "Yes" else 0],
            'PaymentMethod_Credit card (automatic)': [1 if payment_method == "Credit card (automatic)" else 0],
            'PaymentMethod_Electronic check': [1 if payment_method == "Electronic check" else 0],
            'PaymentMethod_Mailed check': [1 if payment_method == "Mailed check" else 0],
            'PhoneService_Yes': [1 if phone_service == "Yes" else 0],
            'SeniorCitizen_1': [1 if senior_citizen == "Yes" else 0],
            'StreamingMovies_No internet service': [1 if streaming_movies == "No internet service" else 0],
            'StreamingMovies_Yes': [1 if streaming_movies == "Yes" else 0],
            'StreamingTV_No internet service': [1 if streaming_tv == "No internet service" else 0],
            'StreamingTV_Yes': [1 if streaming_tv == "Yes" else 0],
            'TechSupport_No internet service': [1 if tech_support == "No internet service" else 0],
            'TechSupport_Yes': [1 if tech_support == "Yes" else 0],
            'gender_Male': [1 if gender == "Male" else 0]
}

        # Convert to DataFrame
        input_features = pd.DataFrame(features)

        # Make prediction
        prediction = model.predict(input_features)

        # Display the prediction
        result = 'The customer is likely to churn.' if prediction[0] == 1 else 'The customer is likely not to churn.'
        st.subheader(result)

if __name__ == '__main__':
    main()
