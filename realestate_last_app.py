# -*- coding: utf-8 -*-
"""realestate_last_app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19e8JMC7egVwsK696V_jq-QUsqhOqngoN
"""

import streamlit as st
import pickle
import numpy as np


# Load the trained model
model_path = 'best_gb_reg_last_joblib.pkl'
try:
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
# Ensure the loaded model has a predict method
    if not hasattr(model, 'predict'):
        st.error(f"The loaded object is not a model or does not have a 'predict' method. Loaded object type: {type(model)}")
        st.stop()
except FileNotFoundError:
    st.error(f"Model file not found: {model_path}")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()


# Load feature names or assume you have them saved
X_columns=[
    'Area', 'Bedrooms', 'Bathrooms', 'B_type_ Apartment', 'B_type_Hotel Apartments',
    'B_type_Penthouse', 'B_type_Townhouses', 'B_type_Villa Compound', 'B_type_Villas',
    'District_Abu Dhabi Gate City (Officers City)', 'District_Ajman Downtown',
    'District_Ajman Free Zone', 'District_Ajman Uptown', 'District_Al Alia',
    'District_Al Amerah', 'District_Al Bahia', 'District_Al Barari', 'District_Al Bateen',
    'District_Al Bustan', 'District_Al Dhait', 'District_Al Fisht', 'District_Al Furjan',
    'District_Al Ghadeer', 'District_Al Gharayen', 'District_Al Hamidiyah', 'District_Al Hamra Village',
    'District_Al Hamriyah', 'District_Al Helio', 'District_Al Hudayriat Island', 'District_Al Jaddaf',
    'District_Al Jubail Island', 'District_Al Jurf', 'District_Al Khan', 'District_Al Majaz',
    'District_Al Mamzar', 'District_Al Marjan Island', 'District_Al Maryah Island', 'District_Al Matar',
    'District_Al Mowaihat', 'District_Al Muntazah', 'District_Al Muroor', 'District_Al Mushrif',
    'District_Al Nahyan', 'District_Al Nuaimiya', 'District_Al Qasba', 'District_Al Qasimia',
    'District_Al Qurm', 'District_Al Raha Beach', 'District_Al Raha Gardens', 'District_Al Rahmaniya',
    'District_Al Ramlah', 'District_Al Rashidiya', 'District_Al Rawda', 'District_Al Reef',
    'District_Al Reem Island', 'District_Al Rumaila', 'District_Al Samha', 'District_Al Seanneeah',
    'District_Al Shamkha', 'District_Al Suyoh', 'District_Al Taawun', 'District_Al Tai',
    'District_Al Tallah 2', 'District_Al Wasl', 'District_Al Yasmeen', 'District_Al Zahraa',
    'District_Al Zahya', 'District_Al Zorah', 'District_Aljada', 'District_Arabian Ranches',
    'District_Arabian Ranches 2', 'District_Arabian Ranches 3', 'District_Arjan', 'District_Athlon by Aldar',
    'District_Baniyas', 'District_Barashi', 'District_Barsha Heights (Tecom)',
    'District_Between Two Bridges (Bain Al Jessrain)', 'District_Bluewaters Island', 'District_Bukadra',
    'District_Bur Dubai', 'District_Business Bay', 'District_City of Arabia', 'District_Corniche Ajman',
    'District_Culture Village (Jaddaf Waterfront)', 'District_DAMAC Hills', 'District_DAMAC Hills 2 (Akoya by DAMAC)',
    'District_DAMAC Lagoons', 'District_DIFC', 'District_Discovery Gardens', 'District_Downtown Dubai',
    'District_Dubai Creek Harbour', 'District_Dubai Design District', 'District_Dubai Festival City',
    'District_Dubai Harbour', 'District_Dubai Hills Estate', 'District_Dubai Industrial City',
    'District_Dubai Investment Park (DIP)', 'District_Dubai Islands', 'District_Dubai Marina',
    'District_Dubai Maritime City', 'District_Dubai Production City (IMPZ)', 'District_Dubai Residence Complex',
    'District_Dubai Science Park', 'District_Dubai Silicon Oasis (DSO)', 'District_Dubai South',
    'District_Dubai Sports City', 'District_Dubai Studio City', 'District_Dubailand', 'District_Emirates City',
    'District_Expo City', 'District_Falcon City of Wonders', 'District_Garden City', 'District_Green Community',
    'District_Hadbat Al Zaafran', 'District_Hoshi', 'District_International City', 'District_Jebel Ali',
    'District_Jumeirah', 'District_Jumeirah Beach Residence (JBR)', 'District_Jumeirah Golf Estates',
    'District_Jumeirah Islands', 'District_Jumeirah Lake Towers (JLT)', 'District_Jumeirah Park',
    'District_Jumeirah Village Circle (JVC)', 'District_Jumeirah Village Triangle (JVT)', 'District_Khalifa City',
    'District_Khor Fakkan', 'District_Living Legends', 'District_Liwan', 'District_Liwara 2',
    'District_Madinat Al Riyadh', 'District_Majan', 'District_Marina Village', 'District_Masdar City',
    'District_Meydan City', 'District_Mina Al Arab', 'District_Mina Rashid', 'District_Mirdif',
    'District_Mohammed Bin Rashid City', 'District_Mohammed Bin Zayed City', 'District_Motor City',
    'District_Mudon', 'District_Musherief', 'District_Muwaileh', 'District_Nad Al Sheba',
    'District_Palm Jebel Ali', 'District_Palm Jumeirah', 'District_Pearl Jumeirah', 'District_Rabdan',
    'District_Ramhan Island', 'District_Ras Al Khor', 'District_Reem', 'District_Remraam', 'District_Saadiyat Island',
    'District_Serena', 'District_Shakhbout City', 'District_Sharjah Garden City', 'District_Sharjah Waterfront City',
    'District_Sheikh Khalifa Bin Zayed Street', 'District_Sheikh Maktoum Bin Rashid Street',
    'District_Sobha Hartland', 'District_The Acres', 'District_The Greens', 'District_The Lakes',
    'District_The Marina', 'District_The Meadows', 'District_The Oasis by Emaar', 'District_The Ritz-Carlton Residences',
    'District_The Springs', 'District_The Valley by Emaar', 'District_The Views', 'District_The Villa',
    'District_The World Islands', 'District_Tilal Al Ghaf', 'District_Tilal City', 'District_Town Square',
    'District_Umm Al Quwain Marina', 'District_Umm Suqeim', 'District_Wasl Gate', 'District_Yas Island',
    'District_Za\'abeel', 'District_Zayed City', 'City_Abu Dhabi', 'City_Ajman', 'City_Dubai',
    'City_Ras Al Khaimah', 'City_Sharjah', 'City_Umm Al Quwain'
]
# Title of the Streamlit app
st.title('Real Estate Price Prediction')

# Input fields for user to provide data
B_type = st.selectbox('Building Type', ['Townhouse', 'Apartment', 'Villa', 'Penthouse'])
bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, step=1)
bathrooms = st.number_input('Number of Bathrooms', min_value=1, max_value=10, step=1)
city = st.selectbox('City', ['Abu Dhabi', 'Dubai', 'Sharjah', 'Ajman', 'Fujairah'])
district = st.selectbox('District', ['Abu Dhabi Gate City (Officers City)', 'Ajman Downtown', 'Ajman Free Zone', 'Ajman Uptown',
                                    'Al Alia', 'Al Amerah', 'Al Bahia', 'Al Barari', 'Al Bateen', 'Al Bustan', 'Al Dhait',
                                    'Al Fisht', 'Al Furjan', 'Al Ghadeer', 'Al Gharayen', 'Al Hamidiyah', 'Al Hamra Village',
                                    'Al Hamriyah', 'Al Helio', 'Al Hudayriat Island', 'Al Jaddaf', 'Al Jubail Island',
                                    'Al Jurf', 'Al Khan', 'Al Majaz', 'Al Mamzar', 'Al Marjan Island', 'Al Maryah Island',
                                    'Al Matar', 'Al Mowaihat', 'Al Muntazah', 'Al Muroor', 'Al Mushrif', 'Al Nahyan',
                                    'Al Nuaimiya', 'Al Qasba', 'Al Qasimia', 'Al Qurm', 'Al Raha Beach', 'Al Raha Gardens',
                                    'Al Rahmaniya', 'Al Ramlah', 'Al Rashidiya', 'Al Rawda', 'Al Reef', 'Al Reem Island',
                                    'Al Rumaila', 'Al Samha', 'Al Seanneeah', 'Al Shamkha', 'Al Suyoh', 'Al Taawun',
                                    'Al Tai', 'Al Tallah 2', 'Al Wasl', 'Al Yasmeen', 'Al Zahraa', 'Al Zahya', 'Al Zorah',
                                    'Aljada', 'Arabian Ranches', 'Arabian Ranches 2', 'Arabian Ranches 3', 'Arjan',
                                    'Athlon by Aldar', 'Baniyas', 'Barashi', 'Barsha Heights (Tecom)', 'Between Two Bridges (Bain Al Jessrain)',
                                    'Bluewaters Island', 'Bukadra', 'Bur Dubai', 'Business Bay', 'City of Arabia', 'Corniche Ajman',
                                    'Culture Village (Jaddaf Waterfront)', 'DAMAC Hills', 'DAMAC Hills 2 (Akoya by DAMAC)',
                                    'DAMAC Lagoons', 'DIFC', 'Discovery Gardens', 'Downtown Dubai', 'Dubai Creek Harbour',
                                    'Dubai Design District', 'Dubai Festival City', 'Dubai Harbour', 'Dubai Hills Estate',
                                    'Dubai Industrial City', 'Dubai Investment Park (DIP)', 'Dubai Islands', 'Dubai Marina',
                                    'Dubai Maritime City', 'Dubai Production City (IMPZ)', 'Dubai Residence Complex',
                                    'Dubai Science Park', 'Dubai Silicon Oasis (DSO)', 'Dubai South', 'Dubai Sports City',
                                    'Dubai Studio City', 'Dubailand', 'Emirates City', 'Expo City', 'Falcon City of Wonders',
                                    'Garden City', 'Green Community', 'Hadbat Al Zaafran', 'Hoshi', 'International City',
                                    'Jebel Ali', 'Jumeirah', 'Jumeirah Beach Residence (JBR)', 'Jumeirah Golf Estates',
                                    'Jumeirah Islands', 'Jumeirah Lake Towers (JLT)', 'Jumeirah Park', 'Jumeirah Village Circle (JVC)',
                                    'Jumeirah Village Triangle (JVT)', 'Khalifa City', 'Khor Fakkan', 'Living Legends',
                                    'Liwan', 'Liwara 2', 'Madinat Al Riyadh', 'Majan', 'Marina Village', 'Masdar City',
                                    'Meydan City', 'Mina Al Arab', 'Mina Rashid', 'Mirdif', 'Mohammed Bin Rashid City',
                                    'Mohammed Bin Zayed City', 'Motor City', 'Mudon', 'Musherief', 'Muwaileh', 'Nad Al Sheba',
                                    'Palm Jebel Ali', 'Palm Jumeirah', 'Pearl Jumeirah', 'Rabdan', 'Ramhan Island', 'Ras Al Khor',
                                    'Reem', 'Remraam', 'Saadiyat Island', 'Serena', 'Shakhbout City', 'Sharjah Garden City',
                                    'Sharjah Waterfront City', 'Sheikh Khalifa Bin Zayed Street', 'Sheikh Maktoum Bin Rashid Street',
                                    'Sobha Hartland', 'The Acres', 'The Greens', 'The Lakes', 'The Marina', 'The Meadows',
                                    'The Oasis by Emaar', 'The Ritz-Carlton Residences', 'The Springs', 'The Valley by Emaar',
                                    'The Views', 'The Villa', 'The World Islands', 'Tilal Al Ghaf', 'Tilal City',
                                    'Town Square', 'Umm Al Quwain Marina', 'Umm Suqeim', 'Wasl Gate', 'Yas Island',
                                    'Za\'abeel', 'Zayed City'])
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

    try:
        # Make prediction
        prediction = model.predict(input_data)

        # Calculate price per square meter
        price_per_sqm = prediction[0] / area

        # Display the prediction
        formatted_price = f"{prediction[0]:,.2f}"
        formatted_price_per_sqm = f"{price_per_sqm:,.2f}"

        st.success(f'The predicted price is: {formatted_price} AED')
        st.info(f'The price per square meter is: {formatted_price_per_sqm} AED/sqm')
    except Exception as e:
        st.error(f"Prediction failed: {e}")
