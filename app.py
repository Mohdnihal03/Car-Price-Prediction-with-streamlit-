import streamlit as st
import pandas as pd
import pickle
# Load your trained model (replace 'pipeline.pkl' with your actual pipeline file path)
with open('LinearRegressionModel.pkl', 'rb') as file:
    pipeline = pickle.load(file)

# Define a function to make predictions
def predict(input_data):
    return pipeline.predict(input_data)

# Streamlit app
st.title("Car Price Prediction")

st.write("Please enter the details of the car:")

# List of companies
companies = ['Hyundai', 'Mahindra', 'Ford', 'Maruti', 'Skoda', 'Audi', 'Toyota',
             'Renault', 'Honda', 'Datsun', 'Mitsubishi', 'Tata', 'Volkswagen',
             'Chevrolet', 'Mini', 'BMW', 'Nissan', 'Hindustan', 'Fiat', 'Force',
             'Mercedes', 'Land', 'Jaguar', 'Jeep', 'Volvo']

# User input fields
name = st.text_input("Name")
company = st.selectbox("Company", companies)
year = st.number_input("Year", min_value=1900, max_value=2024, value=2010)
kms_driven = st.number_input("Kms Driven", min_value=0, value=50000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])

# Prediction button
if st.button("Predict"):
    # Create a DataFrame from user input
    input_data = pd.DataFrame({
        'name': [name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })

    # Make prediction
    prediction = predict(input_data)

    # Display prediction
    st.write(f"The predicted price is: {prediction[0]}")
