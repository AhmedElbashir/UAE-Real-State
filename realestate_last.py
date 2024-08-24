# -*- coding: utf-8 -*-
"""realestate_last

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19e8JMC7egVwsK696V_jq-QUsqhOqngoN
"""

import streamlit as st
import pickle
import numpy as np

# Load the trained model
model_path = 'best_gb_reg last.pkl'
try:
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error(f"Model file not found: {model_path}")
    st.stop()

# Load feature names or assume you have them saved
X_columns = ['Area', 'Bedrooms', 'Bathrooms', 'TotalRooms', 'B_type_ Apartment',
       'B_type_Penthouse', 'B_type_Townhouses', 'B_type_Villa Compound',
       'B_type_Villas', 'District_Abu Dhabi Gate City (Officers City)',
       'District_Al Ghadeer', 'District_Al Jubail Island', 'District_Al Jurf',
       'District_Al Maryah Island', 'District_Al Matar',
       'District_Al Raha Beach', 'District_Al Raha Gardens',
       'District_Al Reef', 'District_Al Reem Island', 'District_Al Samha',
       'District_Al Shamkha', 'District_Khalifa City',
       'District_Madinat Al Riyadh', 'District_Masdar City', 'District_Others',
       'District_Rabdan', 'District_Saadiyat Island', 'District_Yas Island',
       'District_Zayed City', 'City_Abu Dhabi']

# Title of the Streamlit app
st.title('Real Estate Price Prediction')

# Input fields for user to provide data
B_type = st.selectbox('Building Type', ['Townhouse', 'Apartment', 'Villa', 'Penthouse'])
bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, step=1)
bathrooms = st.number_input('Number of Bathrooms', min_value=1, max_value=10, step=1)
city = st.selectbox('City', ['Abu Dhabi', 'Dubai', 'Sharjah', 'Ajman', 'Fujairah'])
district = st.selectbox('District', ['Yas Island', 'Downtown Dubai', 'Jumeirah', 'Marina', 'Al Qasba', 'Al Nuaimia', 'Saadiyat Island','Al Maryah Island','Zayed City'])
area = st.number_input('Area (in square meters)', min_value=10)

# Fix the mismatched column names by trimming any extra spaces in the key values
B_type_col = f'B_type_{B_type}'.replace(" ", "_")
district_col = f'District_{district}'.replace(" ", "_")
city_col = f'City_{city}'.replace(" ", "_")

# Create an input array with all zeros
input_data = np.zeros(len(X_columns))

# Populate the input array with the appropriate values
if B_type_col in X_columns:
    input_data[X_columns.index(B_type_col)] = 1
if city_col in X_columns:
    input_data[X_columns.index(city_col)] = 1
if district_col in X_columns:
    input_data[X_columns.index(district_col)] = 1

input_data[X_columns.index('Area')] = area
input_data[X_columns.index('Bedrooms')] = bedrooms
input_data[X_columns.index('Bathrooms')] = bathrooms

# Button to make predictions
if st.button('Predict'):
    # Reshape the input data to match the model's expected input shape
    input_data = input_data.reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_data)

    # Calculate price per square meter
    price_per_sqm = prediction[0] / area

    # Display the prediction
    formatted_price = f"{prediction[0]:,.2f}"
    formatted_price_per_sqm = f"{price_per_sqm:,.2f}"

    st.success(f'The predicted price is: {formatted_price} AED')
    st.info(f'The price per square meter is: {formatted_price_per_sqm} AED/sqm')

!pi