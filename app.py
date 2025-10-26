# app.py (main file)
# By Ali Emad

import streamlit as st
import pandas as pd
import pickle

# Load model
with open("car_model.pkl", "rb") as f:
    model = pickle.load(f)

# Title
st.title("🚗 Car Price Prediction App")
st.markdown("### Predict the approximate market price of a car using AI")

# Sidebar inputs
st.sidebar.header("Car Specifications")

symboling = st.sidebar.slider("Symboling (risk factor)", -3, 3, 0)
fueltype = st.sidebar.selectbox("Fuel Type", ["gas", "diesel"])
aspiration = st.sidebar.selectbox("Aspiration", ["std", "turbo"])
doornumber = st.sidebar.selectbox("Number of Doors", ["two", "four"])
carbody = st.sidebar.selectbox("Car Body", ["convertible", "hatchback", "sedan", "wagon", "hardtop"])
drivewheel = st.sidebar.selectbox("Drive Wheel", ["rwd", "fwd", "4wd"])
enginelocation = st.sidebar.selectbox("Engine Location", ["front", "rear"])
wheelbase = st.sidebar.number_input("Wheelbase (inches)", 80.0, 120.0, 95.0)
carlength = st.sidebar.number_input("Car Length (inches)", 140.0, 210.0, 170.0)
carwidth = st.sidebar.number_input("Car Width (inches)", 60.0, 80.0, 65.0)
carheight = st.sidebar.number_input("Car Height (inches)", 45.0, 60.0, 54.0)
curbweight = st.sidebar.number_input("Curb Weight (kg)", 1500, 4000, 2500)
enginetype = st.sidebar.selectbox("Engine Type", ["dohc", "ohcv", "ohc", "l", "rotor"])
cylindernumber = st.sidebar.selectbox("Cylinder Number", ["four", "six", "five", "eight", "three", "twelve", "two"])
enginesize = st.sidebar.number_input("Engine Size (cc)", 60, 350, 130)
fuelsystem = st.sidebar.selectbox("Fuel System", ["mpfi", "2bbl", "idi", "1bbl", "spdi"])
boreratio = st.sidebar.number_input("Bore Ratio", 2.0, 4.0, 3.0)
stroke = st.sidebar.number_input("Stroke", 2.0, 5.0, 3.0)
compressionratio = st.sidebar.number_input("Compression Ratio", 7.0, 12.0, 9.0)
horsepower = st.sidebar.number_input("Horsepower", 40, 250, 100)
peakrpm = st.sidebar.number_input("Peak RPM", 4000, 7000, 5500)
citympg = st.sidebar.number_input("City MPG", 10, 60, 25)
highwaympg = st.sidebar.number_input("Highway MPG", 10, 60, 30)

# Convert text inputs to numeric encoding (quick manual mapping)
encoder_dict = {
    "fueltype": {"gas": 0, "diesel": 1},
    "aspiration": {"std": 0, "turbo": 1},
    "doornumber": {"two": 0, "four": 1},
    "carbody": {"convertible": 0, "hatchback": 1, "sedan": 2, "wagon": 3, "hardtop": 4},
    "drivewheel": {"rwd": 0, "fwd": 1, "4wd": 2},
    "enginelocation": {"front": 0, "rear": 1},
    "enginetype": {"dohc": 0, "ohcv": 1, "ohc": 2, "l": 3, "rotor": 4},
    "cylindernumber": {"four": 0, "six": 1, "five": 2, "eight": 3, "three": 4, "twelve": 5, "two": 6},
    "fuelsystem": {"mpfi": 0, "2bbl": 1, "idi": 2, "1bbl": 3, "spdi": 4}
}

# Collect inputs in correct order
input_data = [[
    symboling,
    encoder_dict["fueltype"][fueltype],
    encoder_dict["aspiration"][aspiration],
    encoder_dict["doornumber"][doornumber],
    encoder_dict["carbody"][carbody],
    encoder_dict["drivewheel"][drivewheel],
    encoder_dict["enginelocation"][enginelocation],
    wheelbase,
    carlength,
    carwidth,
    carheight,
    curbweight,
    encoder_dict["enginetype"][enginetype],
    encoder_dict["cylindernumber"][cylindernumber],
    enginesize,
    encoder_dict["fuelsystem"][fuelsystem],
    boreratio,
    stroke,
    compressionratio,
    horsepower,
    peakrpm,
    citympg,
    highwaympg
]]

if st.button("Predict Price"):
    price = model.predict(input_data)[0]
    st.success(f"💰 Estimated Car Price: **${round(price, 2):,} USD**")
