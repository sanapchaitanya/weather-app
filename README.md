# Weather Forecast & Air Quality Dashboard

A simple interactive dashboard built with **Python and Streamlit** that allows users to check the weather forecast and air quality for any city.
The application fetches real-time data from the OpenWeather API and presents it in a clean and easy-to-understand interface.

This project was built to practice working with APIs, building data dashboards, and deploying applications using Streamlit Cloud.

---

## Features

* Search weather data for any city
* View weather forecast for up to **5 days**
* Display multiple weather metrics:

  * Temperature
  * Sky conditions
  * Humidity
  * Feels like temperature
* Check **Air Quality Index (AQI)** for a location
* View pollutant levels including:

  * PM2.5
  * PM10
  * NO₂
  * O₃
  * CO
* Clean dashboard layout using Streamlit components
* Interactive UI with sliders and dropdown selections

---

## Tech Stack

* **Python**
* **Streamlit**
* **Plotly**
* **Requests**
* **OpenWeather API**

---

## How It Works

The application retrieves weather and air quality data using the OpenWeather API.
The backend processes the data and the frontend built with Streamlit displays it in an interactive dashboard.

Users can enter a city name and select what type of data they want to view.

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/weather-forecast-dashboard.git
```

Navigate to the project folder:

```
cd weather-forecast-dashboard
```

Install the required dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run main.py
```

---

## Environment Variables

Create a `.env` file in the project root and add your API key:

```
OPENWEATHER_API_KEY=your_api_key_here
```

The app uses this key to fetch data from the OpenWeather API.

---

## Deployment

This project is deployed using **Streamlit Community Cloud**.
API keys are stored securely using **Streamlit Secrets** instead of exposing them in the repository.

---

## Future Improvements

* Add weather trend charts
* Improve dashboard styling
* Add historical weather data analysis
* Add location autocomplete
* Mobile UI optimization

---

## Author

**Chaitanya Sanap**

