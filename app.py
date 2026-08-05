import streamlit as st
from api.weather_api import get_weather, get_forecast
from database.db import save_weather, get_total_searches
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤", layout="centered")


def load_css():
    css_path = Path("assets/style.css")
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()

st.title("🌤 Weather Dashboard")
st.caption("Real-time weather monitoring powered by OpenWeatherMap API & PostgreSQL")

with st.sidebar:
    st.markdown("""
    # 🌤 WEATHER DASHBOARD

    ### Professional Weather App
    """)
    st.divider()

    st.subheader("📌 Features")
    st.write("✅ Current Weather")
    st.write("✅ 5-Day Forecast")
    st.write("✅ Weather History")
    st.write("✅ Statistics Dashboard")
    st.divider()

    try:
        st.metric("📊 Total Searches", get_total_searches())
    except Exception:
        st.metric("📊 Total Searches", 0)

    st.divider()
    st.caption("Version 1.0")
    st.caption("Powered by")
    st.caption("🌤 OpenWeatherMap API")
    st.caption("🐘 PostgreSQL")

st.write("🕒", datetime.now().strftime("%A, %d %B %Y | %I:%M %p"))

city = st.text_input("Enter City Name", placeholder="e.g. Delhi, London, New York")

if st.button("🔍 Search"):
    if not city.strip():
        st.warning("Please enter a city name.")
        st.stop()

    weather = get_weather(city)

    if str(weather.get("cod")) == "200":
        try:
            save_weather(weather)
        except Exception as e:
            st.warning(f"Database Error: {e}")

        forecast = get_forecast(city)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(
                "<div class='weather-card'>🌡️ Temperature</div>", unsafe_allow_html=True
            )
            st.metric("", f"{weather['main']['temp']} °C")

        with col2:
            st.markdown(
                "<div class='weather-card'>💧 Humidity</div>", unsafe_allow_html=True
            )
            st.metric("", f"{weather['main']['humidity']} %")

        with col3:
            st.markdown(
                "<div class='weather-card'>🌬 Wind Speed</div>", unsafe_allow_html=True
            )
            st.metric("", f"{weather['wind']['speed']} m/s")

        with col4:
            st.markdown(
                "<div class='weather-card'>🔽 Pressure</div>", unsafe_allow_html=True
            )
            st.metric("", f"{weather['main']['pressure']} hPa")

        icon = weather["weather"][0]["icon"]
        condition = weather["weather"][0]["description"].title()
        temperature = weather["main"]["temp"]

        st.markdown(
            f"""
            <div class="weather-summary">
                <h2>📍 {weather['name']}, {weather['sys']['country']}</h2>
                <img src="https://openweathermap.org/img/wn/{icon}@2x.png" width="120">
                <div class="weather-temperature">{temperature} °C</div>
                <div class="weather-condition">☁️ {condition}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### 🌍 Weather Details")
        st.write(f"☁️ **Condition:** {condition}")
        st.write(f"👁️ **Visibility:** {weather['visibility'] / 1000:.1f} km")
        st.write(f"🌍 **Country:** {weather['sys']['country']}")

        sunrise = datetime.fromtimestamp(weather["sys"]["sunrise"]).strftime("%I:%M %p")
        sunset = datetime.fromtimestamp(weather["sys"]["sunset"]).strftime("%I:%M %p")

        st.write(f"🌅 **Sunrise:** {sunrise}")
        st.write(f"🌇 **Sunset:** {sunset}")

        st.divider()
        st.subheader("📅 5-Day Weather Forecast")

        if forecast and "list" in forecast:
            forecast_list = forecast["list"]

            for item in forecast_list[::8]:
                date = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime(
                    "%A, %d %b %Y"
                )
                temp = item["main"]["temp"]
                humidity = item["main"]["humidity"]
                description = item["weather"][0]["description"].title()
                icon = item["weather"][0]["icon"]

                st.container(border=True)

                col1, col2 = st.columns([1, 4])

                with col1:
                    st.image(
                        f"https://openweathermap.org/img/wn/{icon}@2x.png", width=70
                    )

                with col2:
                    st.markdown(f"### 📅 {date}")
                    st.write(f"🌡 **Temperature:** {temp:.1f} °C")
                    st.write(f"☁️ **Condition:** {description}")
                    st.write(f"💧 **Humidity:** {humidity}%")

                st.divider()
        else:
            st.warning("Forecast data not available")

    else:
        st.error(weather.get("message", "City not found"))

st.divider()
st.caption("🌤 Weather Dashboard • Version 1.0")
st.caption("Built with ❤️ using Streamlit, OpenWeatherMap API, Plotly & PostgreSQL")
