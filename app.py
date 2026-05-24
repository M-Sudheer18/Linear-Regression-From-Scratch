
# Inputs
# ['BHK',
#  'Size',
#  'Bathroom',
#  'Rent_per_sqft',
#  'Size_per_BHK',
#  'Bathroom_BHK_ratio',
#  'Is_Furnished',
#  'Is_Semi_Furnished',
#  'City_encoded',
#  'Area_Type_encoded']

import streamlit as st
import pandas as pd
import joblib as jb



# model = jb.load("linear_regression_scratch.pkl")
scaler = jb.load("Scaler.pkl")


model_data = jb.load("linear_model.pkl")

weights = model_data["weights"]
bias = model_data["bias"]







st.title("House Prediction")
st.write("Details of the House")

# BHK
bhk = st.number_input(
        "Enter No.of Bedrooms",
        min_value=0,
        max_value=None,
        value=0,
        step=1
)

size = st.number_input(
        "Size in Sqrft",
        min_value=111,
        value=123,
        step=1
)

bathroom = st.number_input(
        "Number of Bathrooms",
        min_value=1,
        max_value=7,
        value=2,
        step=1
)

rent_per_sqft = st.number_input(
        "Rent per Sqft",
        min_value=2.0,
        max_value=500.0,
        value=20.0,
        step=0.1,
        format="%.2f"
)



size_per_bhk = st.number_input(
        "Size per BHK",
        min_value=100.0,
        max_value=2000.0,
        value=500.0,
        step=1.0,
        format="%.2f"
)



bathroom_bhk_ratio = st.number_input(
        "Bathroom/BHK Ratio",
        min_value=0.1,
        max_value=5.0,
        value=1.0,
        step=0.1,
        format="%.2f"
)



furnishing = st.selectbox(
        "Furnishing Status",
        ["Unfurnished", "Semi-Furnished", "Furnished"]
)

is_furnished = 1 if furnishing == "Furnished" else 0
is_semi_furnished = 1 if furnishing == "Semi-Furnished" else 0



city = st.selectbox(
        "Select City",
        ["Bangalore", "Chennai", "Delhi", "Hyderabad", "Mumbai", "Pune"]
)

city_mapping = {
        "Bangalore": 0,
        "Chennai": 1,
        "Delhi": 2,
        "Hyderabad": 3,
        "Mumbai": 4,
        "Pune": 5
}

city_encoded = city_mapping[city]



area_type = st.selectbox(
        "Area Type",
        ["Super Area", "Carpet Area", "Built Area"]
)

area_mapping = {
        "Super Area": 0,
        "Carpet Area": 1,
        "Built Area": 2
}

area_type_encoded = area_mapping[area_type]



# Button

if st.button("Predict Rent"):
       
        input_data = pd.DataFrame({
                'BHK': [bhk],
                'Size': [size],
                'Bathroom': [bathroom],
                'Rent_per_sqft': [rent_per_sqft],
                'Size_per_BHK': [size_per_bhk],
                'Bathroom_BHK_ratio': [bathroom_bhk_ratio],
                'Is_Furnished': [is_furnished],
                'Is_Semi_Furnished': [is_semi_furnished],
                'City_encoded': [city_encoded],
                'Area_Type_encoded': [area_type_encoded]
        })

        # Scale Input 
        input_scaled = scaler.transform(input_data)

        # Predict Data
        prediction = input_scaled @ weights + bias

        st.success(f"Predicted Rent: ₹{prediction[0]:,.2f}")