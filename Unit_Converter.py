
import streamlit as st

# page title or icon k liye
st.set_page_config(page_title="Google Unit Converter", page_icon="🔄")

# Title of app
st.title("Google Unit Converter")

# Instructions for user
st.write("""
This simple app allows you to convert various units. 
Select the units and the values you want to convert.
""")

# Function to handle unit conversion
def convert_units(value, from_unit, to_unit):
    # Conversion for length units
    if from_unit == "Meter" and to_unit == "Kilometer":
        return value / 1000
    elif from_unit == "Kilometer" and to_unit == "Meter":
        return value * 1000
    elif from_unit == "Centimeter" and to_unit == "Meter":
        return value / 100
    elif from_unit == "Meter" and to_unit == "Centimeter":
        return value * 100

    # Conversion for weight units
    elif from_unit == "Gram" and to_unit == "Kilogram":
        return value / 1000
    elif from_unit == "Kilogram" and to_unit == "Gram":
        return value * 1000
    elif from_unit == "Pound" and to_unit == "Kilogram":
        return value * 0.453592
    elif from_unit == "Kilogram" and to_unit == "Pound":
        return value / 0.453592

    # Conversion for temperature
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9

    # Conversion for volume
    elif from_unit == "Liter" and to_unit == "Milliliter":
        return value * 1000
    elif from_unit == "Milliliter" and to_unit == "Liter":
        return value / 1000

    return None

# menu for selecting units
unit_types = ["Length", "Weight", "Temperature", "Volume"]
unit_type = st.selectbox("Select the type of units you want to convert", unit_types)

# Length conversion
if unit_type == "Length":
    st.subheader("Length Conversion")
    length_units = ["Meter", "Kilometer", "Centimeter"]
    from_unit = st.selectbox("From Unit", length_units)
    to_unit = st.selectbox("To Unit", length_units)
    value = st.number_input("Enter value to convert", min_value=0.0, step=0.1)
    
    if value:
        result = convert_units(value, from_unit, to_unit)
        if result is not None:
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.write("Conversion not available for selected units.")

# Weight conversion
elif unit_type == "Weight":
    st.subheader("Weight Conversion")
    weight_units = ["Gram", "Kilogram", "Pound"]
    from_unit = st.selectbox("From Unit", weight_units)
    to_unit = st.selectbox("To Unit", weight_units)
    value = st.number_input("Enter value to convert", min_value=0.0, step=0.1)

    if value:
        result = convert_units(value, from_unit, to_unit)
        if result is not None:
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.write("Conversion not available for selected units.")

# Temperature conversion
elif unit_type == "Temperature":
    st.subheader("Temperature Conversion")
    temperature_units = ["Celsius", "Fahrenheit"]
    from_unit = st.selectbox("From Unit", temperature_units)
    to_unit = st.selectbox("To Unit", temperature_units)
    value = st.number_input("Enter value to convert", min_value=-273.15, step=0.1)

    if value:
        result = convert_units(value, from_unit, to_unit)
        if result is not None:
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.write("Conversion not available for selected units.")

# Volume conversion
elif unit_type == "Volume":
    st.subheader("Volume Conversion")
    volume_units = ["Liter", "Milliliter"]
    from_unit = st.selectbox("From Unit", volume_units)
    to_unit = st.selectbox("To Unit", volume_units)
    value = st.number_input("Enter value to convert", min_value=0.0, step=0.1)

    if value:
        result = convert_units(value, from_unit, to_unit)
        if result is not None:
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.write("Conversion not available for selected units.")

#Last line
st.write("---")
st.write("Made by Mubashir Awan")
st.write("Rollno: 208369")
st.write("Date of Registration: 6/3/2023")
st.write("venue: Governor House, Sindh")