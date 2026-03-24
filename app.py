import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('house_model.pkl', 'rb'))

st.title("House Price Prediction")

area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")
parking = st.number_input("Parking")

mainroad = st.selectbox("Main Road", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])

furnishing = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)

# Convert inputs
def yes_no(val): return 1 if val == "yes" else 0

mainroad = yes_no(mainroad)
guestroom = yes_no(guestroom)
basement = yes_no(basement)
airconditioning = yes_no(airconditioning)
prefarea = yes_no(prefarea)

furn_semi = 1 if furnishing == "semi-furnished" else 0
furn_unfurn = 1 if furnishing == "unfurnished" else 0

features = np.array([[
    area, bedrooms, bathrooms, stories,
    mainroad, guestroom, basement, 0,
    airconditioning, parking, prefarea,
    furn_semi, furn_unfurn
]])

if st.button("Predict Price"):
    prediction = model.predict(features)
    st.success(f"Estimated Price: {int(prediction[0])}")