import streamlit as st
import joblib
import pandas as pd

model = joblib.load('car_price_model.pkl')

st.title("Prédicteur de Prix de Voiture d'Occasion")

year = st.slider("Année", 2000, 2023, 2015)
km_driven = st.number_input("Kilométrage", 0, 300000, 50000)
fuel = st.selectbox("Carburant", ["Diesel", "Petrol", "CNG", "LPG"])
seller_type = st.selectbox("Type de vendeur", ["Individual", "Dealer", "Trustmark Dealer"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Propriétaire", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])
mileage = st.number_input("Consommation (kmpl)", 0.0, 40.0, 20.0)
engine = st.number_input("Moteur (CC)", 600, 5000, 1200)
max_power = st.number_input("Puissance (bhp)", 20.0, 400.0, 80.0)
seats = st.selectbox("Nombre de sièges", [2, 4, 5, 6, 7, 8, 9])

if st.button("Prédire le prix"):
    input_data = pd.DataFrame({
        'year': [year], 'km_driven': [km_driven], 'mileage': [mileage],
        'engine': [engine], 'max_power': [max_power], 'seats': [seats],
        'fuel_Diesel': [1 if fuel == 'Diesel' else 0],
        'fuel_LPG': [1 if fuel == 'LPG' else 0],
        'fuel_Petrol': [1 if fuel == 'Petrol' else 0],
        'seller_type_Individual': [1 if seller_type == 'Individual' else 0],
        'seller_type_Trustmark Dealer': [1 if seller_type == 'Trustmark Dealer' else 0],
        'transmission_Manual': [1 if transmission == 'Manual' else 0],
        'owner_Fourth & Above Owner': [1 if owner == 'Fourth & Above Owner' else 0],
        'owner_Second Owner': [1 if owner == 'Second Owner' else 0],
        'owner_Test Drive Car': [1 if owner == 'Test Drive Car' else 0],
        'owner_Third Owner': [1 if owner == 'Third Owner' else 0],
    })
    input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)
    prediction = model.predict(input_data)
    st.success(f"Prix estimé : {prediction[0]:,.0f}")