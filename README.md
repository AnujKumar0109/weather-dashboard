# 🌤 Weather Dashboard

<div align="center">

### Real-Time Weather Dashboard built with Python, Streamlit, OpenWeatherMap API & PostgreSQL (Supabase)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge\&logo=streamlit)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge\&logo=postgresql)
![Supabase](https://img.shields.io/badge/Supabase-Backend-3ECF8E?style=for-the-badge\&logo=supabase)
![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-orange?style=for-the-badge)



</div>

---

## 📖 Overview

The **Weather Dashboard** is a Python-based web application that provides **real-time weather information** for cities around the world.

The application is developed using **Streamlit** and integrates the **OpenWeatherMap API** to fetch live weather data. Every weather search is stored in a **PostgreSQL database hosted on Supabase**, allowing users to maintain a searchable history while demonstrating backend database integration.

This project showcases practical implementation of:

* REST API Integration
* PostgreSQL Database Connectivity
* Python Programming
* SQL
* Cloud Deployment
* Streamlit UI Development
* Secure Environment Variable Management

---

## 🚀 Live Demo

The application is deployed on **Streamlit Community Cloud** and is publicly accessible.

🌐 **Live Application**

**https://weather-dashboard-igioqvelequtr43mggzn4t.streamlit.app/**

You can use the application to:

* 🌍 Search weather information for any city
* 🌡 View real-time temperature
* 💧 Check humidity
* 🌬 View wind speed
* 🔽 Check atmospheric pressure
* 💾 Store search history in PostgreSQL (Supabase)

---

## 🔗 Project Links

### 🌐 Live Demo

https://weather-dashboard-igioqvelequtr43mggzn4t.streamlit.app/

### 💻 GitHub Repository

https://github.com/AnujKumar0109/weather-dashboard

### 👨‍💻 Author

**Anuj Kumar**

GitHub: https://github.com/AnujKumar0109

---

## 🙏 Acknowledgements

This project was built using the following technologies and services:

* Python
* Streamlit
* OpenWeatherMap API
* PostgreSQL
* Supabase
* Git & GitHub



---

# ✨ Features

* 🌍 Search weather by city name
* 🌡 Live temperature updates
* 💧 Humidity information
* 🌬 Wind speed
* 🔽 Atmospheric pressure
* 📍 City and country information
* 📅 Current date display
* 🕒 Current time display
* 💾 Weather search history saved in PostgreSQL
* 📊 Total searches counter
* 🎨 Responsive user interface
* ⚡ Fast API response
* 🔐 Secure credential management using Streamlit Secrets
* ⚠ Graceful error handling for invalid cities

---

# 🛠 Tech Stack

| Category             | Technology         |
| -------------------- | ------------------ |
| Programming Language | Python             |
| Frontend             | Streamlit          |
| Styling              | CSS                |
| Weather API          | OpenWeatherMap API |
| Database             | PostgreSQL         |
| Cloud Database       | Supabase           |
| Version Control      | Git                |
| Repository           | GitHub             |

---

# 📸 Screenshots

### 🏠 Home Screen

```
screenshots/home.png
```

---

### 🌤 Weather Details

```
screenshots/weather.png
```

---

### 🗄 PostgreSQL Database

```
screenshots/database.png
```

---

# 📁 Project Structure

```text
weather-dashboard/
│
├── api/
│   └── weather_api.py
│
├── assets/
│   └── style.css
│
├── database/
│   └── db.py
│
├── screenshots/
│   ├── home.png
│   ├── weather.png
│   └── database.png
│
├── .streamlit/
│   └── secrets.toml
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/AnujKumar0109/weather-dashboard.git
```

Move into the project directory:

```bash
cd weather-dashboard
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate (Windows)

```bash
venv\Scripts\activate
```

Activate (Linux/macOS)

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create the following file:

```text
.streamlit/secrets.toml
```

Add:

```toml
OPENWEATHER_API_KEY = "YOUR_API_KEY"

DATABASE_URL = "postgresql://username:password@host:5432/postgres"
```

---

# 🗄 Database Schema

```sql
CREATE TABLE weather_history (

    id SERIAL PRIMARY KEY,

    city VARCHAR(100),

    temperature FLOAT,

    humidity INTEGER,

    wind_speed FLOAT,

    pressure INTEGER,

    searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
```

---

# ▶ Running the Application

```bash
streamlit run app.py
```

Open your browser:

```text
http://localhost:8501
```

---

# 🌍 Weather Information Displayed

The application displays:

* 🌡 Temperature
* 💧 Humidity
* 🌬 Wind Speed
* 🔽 Pressure
* 📍 City
* 🌍 Country
* 📅 Current Date
* 🕒 Current Time

---

# 💾 Database Workflow

```text
            User
              │
              ▼
      Enter City Name
              │
              ▼
     Streamlit Application
              │
              ▼
   OpenWeatherMap API Request
              │
              ▼
     Receive Weather Data (JSON)
              │
      ┌───────┴────────┐
      ▼                ▼
Display Weather     Save Search
Information         to PostgreSQL
      │                │
      └───────┬────────┘
              ▼
       Weather Dashboard
```

---

# 🔒 Security

Sensitive credentials are stored securely using **Streamlit Secrets** instead of being hardcoded.

### Stored Secrets

* `OPENWEATHER_API_KEY`
* `DATABASE_URL`

Example:

```toml
OPENWEATHER_API_KEY="YOUR_API_KEY"

DATABASE_URL="postgresql://username:password@host:5432/postgres"
```

---

# 📦 Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```

Main libraries used:

```text
streamlit
requests
psycopg2-binary
python-dotenv
```

---

# ☁️ Deployment

This project can be deployed on several cloud platforms.

### Supported Platforms

* ✅ Streamlit Community Cloud
* ✅ Render
* ✅ Railway
* ✅ Heroku

### Database

* PostgreSQL
* Supabase

---

# 🧪 Example Usage

1. Launch the application.
2. Enter a city name.
3. Click **Search**.
4. The application requests weather data from the OpenWeatherMap API.
5. Weather details are displayed instantly.
6. The search is automatically saved in the PostgreSQL database.
7. The total search counter is updated.

---

# 📈 Future Enhancements

Planned improvements include:

* 🌦 7-Day Weather Forecast
* ⏰ Hourly Weather Forecast
* 🌍 Automatic Location Detection
* 🌫 Air Quality Index (AQI)
* ☀ UV Index
* ❤️ Favorite Cities
* 📜 Search History Page
* 🔐 User Authentication
* 🌙 Dark Mode
* 📊 Interactive Charts
* 🗺 Weather Maps
* 📤 Export Search History
* 🔔 Weather Alerts
* 🌐 Multi-language Support

---

# 📚 Learning Outcomes

Through this project I gained practical experience with:

* Python Programming
* REST API Integration
* JSON Parsing
* PostgreSQL Database
* SQL Queries
* Streamlit Web Development
* Database Connectivity
* Environment Variables
* Git & GitHub
* Cloud Deployment
* Error Handling
* Clean Project Structure

---

# 🤝 Contributing

Contributions are welcome!

### Steps

1. Fork this repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 🐞 Known Issues

* Internet connection is required.
* Invalid API keys return an authentication error.
* Some cities may have multiple results depending on the API.
* Weather information depends on OpenWeatherMap API availability.

---

# 📋 Roadmap

* [x] Real-time Weather Search
* [x] PostgreSQL Database Integration
* [x] Streamlit User Interface
* [x] Responsive Design
* [ ] User Login System
* [ ] Weather Forecast
* [ ] Air Quality Index
* [ ] Favorite Cities
* [ ] Weather Charts
* [ ] Search History Dashboard

---

# 👨‍💻 Author

## Anuj Kumar

🎓 MCA Student

💻 Python Developer

🌤 Weather Dashboard Developer

### GitHub

https://github.com/AnujKumar0109

### Repository

https://github.com/AnujKumar0109/weather-dashboard

---

# ⭐ Show Your Support

If you found this project useful, please consider:

⭐ Starring the repository

🍴 Forking the project

🐛 Reporting issues

💡 Suggesting improvements

Your support is greatly appreciated!

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for educational and learning purposes.

---

# 🙏 Acknowledgements

Special thanks to:

* OpenWeatherMap API
* Streamlit
* Supabase
* PostgreSQL
* Python Community
* GitHub

---

<div align="center">

## 🌤 Weather Dashboard

### Built with ❤️ using

**Python • Streamlit • PostgreSQL • Supabase • OpenWeatherMap API**

---

⭐ **If you like this project, don't forget to star the repository!**

**Happy Coding! 🚀**

</div>
