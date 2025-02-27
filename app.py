import streamlit as st

def apply_custom_css():
    st.markdown(
        """
        <style>
            body {
                background-color: #000000;
                color: white;
                font-family: Arial, sans-serif;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 24px;
                border-radius: 5px;
                border: none;
                cursor: pointer;
                font-size: 18px;
            }
            .stButton>button:hover {
                background-color: #45a049;
            }
            .stTitle {
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def convert_length(value, from_unit, to_unit):
    length_units = {
        "meters": 1.0,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "grams": 1.0,
        "kilograms": 0.001,
        "milligrams": 1000,
        "pounds": 0.00220462,
        "ounces": 0.035274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value

def unit_converter():
    apply_custom_css()
    st.title("🔄 Unit Converter 🔥")
    category = st.selectbox("📏 Choose category", ["Length 📐", "Weight ⚖️", "Temperature 🌡️"])
    value = st.number_input("🔢 Enter value to convert", min_value=0.0, step=0.1)
    
    if category == "Length 📐":
        units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"]
    elif category == "Weight ⚖️":
        units = ["grams", "kilograms", "milligrams", "pounds", "ounces"]
    elif category == "Temperature 🌡️":
        units = ["celsius", "fahrenheit", "kelvin"]
    
    from_unit = st.selectbox("🔄 Convert from", units)
    to_unit = st.selectbox("🔄 Convert to", units)
    
    if st.button("🚀 Convert"):
        if category == "Length 📐":
            result = convert_length(value, from_unit, to_unit)
        elif category == "Weight ⚖️":
            result = convert_weight(value, from_unit, to_unit)
        elif category == "Temperature 🌡️":
            result = convert_temperature(value, from_unit, to_unit)
        
        st.success(f"✅ {value} {from_unit} is equal to {result:.2f} {to_unit} 🎉")

if __name__ == "__main__":
    unit_converter()