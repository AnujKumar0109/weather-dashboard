import streamlit as st
import pandas as pd

from database.db import get_weather_history

st.set_page_config(
    page_title="Weather History",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Weather History")

st.caption("View previously searched weather records.")

history = get_weather_history()

if history:

    df = pd.DataFrame(
        history,
        columns=[
            "City",
            "Temperature (°C)",
            "Humidity (%)",
            "Weather",
            "Date & Time"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info("No weather history available.")
    
st.divider()
st.caption("🌤 Weather Dashboard • Weather History")   

 