import streamlit as st
import joblib
import numpy as np
import datetime as dt

model = joblib.load("rain_probability_model.pkl")

st.set_page_config(page_title="Abuja Rain Predictor", layout="centered")

st.markdown("""
🌧️Abuja Rain Probability Predictor🌦️
----
**Welcome!**  
Ever wondered if it will rain on a specific day in Abuja, even years from now? This app uses **historical climate patterns** and **machine learning** to estimate the **likelihood of rainfall** for any date you select.
### How It Works
1. Pick a date from the calendar 📅  
2. The app calculates probabilities based on **seasonal and historical trends** 📊  
3. See the result with a **probability percentage** and a fun **animated GIF** that matches the likelihood:  
   - ☀️ Low chance of rain  
   - ⛅ Moderate chance of rain  
   - 🌧️ High chance of rain""", unsafe_allow_html=True)

st.markdown("""⚠️ Please Take Note: These predictions are **probabilistic estimates** derived from historical data, not real-time forecasts. Use them as guidance, not guaranteed weather information.""")

selected_date = st.date_input(
    "Select a date",
    min_value=dt.date(2025, 1, 1),
    max_value=dt.date(2035, 12, 31)
)

month = selected_date.month
day = selected_date.day
day_of_year = selected_date.timetuple().tm_yday

if st.button("Predict Rain Probability"):
    input_data = np.array([[month, day, day_of_year]])
    probability = model.predict_proba(input_data)[0][1] * 100

    st.metric("🌧️ Probability of Rain", f"{probability:.2f}%")
    date_str = selected_date.strftime("%A, %B %d, %Y")

    if probability > 70:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmR5bm0yYjNibXg0YTNocms1OWwyMTljcGcwOWQ0dWU0NXV0aDB3ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/pNn4hlkovWAHfpLRRD/giphy.gif")
        st.warning(f"It will Rain on {date_str}. 🌧️")


    elif probability > 40:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWQ3Nzd3bGQydWxyMDhpcHNoaWxqbWRxa252cTlqdm8zaHdjZ3FodyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/gk3s6G7AdUNkey0YpE/giphy.gif")
        st.info(f"It will be Cloudy/Windy with a chance of rain on {date_str}.⛅")


    else:
        st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NzZrM2MzNDFuZWM1OHhnNXJkZnQyN2h0ZXVlN3BqYjI0eGpyaG56eSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/59e2sUzi36bIr4FyD7/giphy.gif")
        st.success(f"The Sun will shine upon {date_str}. ☀️")


st.markdown("This is Praise's Weather Prediction Project in DCH")


