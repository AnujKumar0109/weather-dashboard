import streamlit as st
import pandas as pd
import plotly.express as px

from database.db import get_statistics

st.set_page_config(
    page_title="Weather Statistics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Weather Analytics")

st.caption("Analyze weather trends using historical data.")

data = get_statistics()

if data:

    df = pd.DataFrame(
        data,
        columns=[
            "City",
            "Temperature",
            "Humidity",
            "Date"
        ]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Searches",
        len(df)
    )

    col2.metric(
        "Average Temp",
        f"{df['Temperature'].mean():.1f} °C"
    )

    col3.metric(
        "Highest Temp",
        f"{df['Temperature'].max():.1f} °C"
    )

    st.divider()

    fig = px.line(
        df,
        x="Date",
        y="Temperature",
        color="City",
        markers=True,
        title="Temperature Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    fig2 = px.bar(
        df,
        x="City",
        y="Humidity",
        color="City",
        title="Humidity by City"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

else:

    st.info("No data available.")
    
st.divider()
st.caption("🌤 Weather Dashboard • Weather Analytics")