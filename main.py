import streamlit as st
import plotly.express as px
from backend import get_data, get_air_quality

st.title("Weather Forecast for the Next Days")
place = st.text_input("place: ")
option = st.selectbox("select data to view",
                      ("temperature", "sky", "humidity", "feels like", "air quality"))
days = st.slider("forecast Days", min_value=1, max_value=5,
                 help='Select the number of days to forecast',
                 disabled=(option == "air quality"))
if option == "air quality":
    st.subheader(f"Air Quality in {place}")
else:
    st.subheader(f"{option} for the next {days} days in {place}")

if place:

    try:
        filtered_data = get_data(place, days)

        if option == "temperature":
            temperatures = [dict["main"]["temp"] - 273.15 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (celsius)"})
            st.plotly_chart(figure)

        if option == "sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)

        if option == "humidity":
                humidity = [dict["main"]["humidity"] for dict in filtered_data]
                dates = [dict["dt_txt"] for dict in filtered_data]

                figure = px.line(x=dates,y=humidity,labels={"x": "Date", "y": "Humidity (%)"})

                st.plotly_chart(figure)

        if option == "feels like":
            feels_like = [dict["main"]["feels_like"] - 273.15 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            figure = px.line(x=dates,y=feels_like,labels={"x": "Date", "y": "Feels Like (Celsius)"})

            st.plotly_chart(figure)
        if option == "air quality":
            if option == "air quality":

                air_data = get_air_quality(place)

                aqi = air_data["list"][0]["main"]["aqi"]

                aqi_labels = {
                    1: "Good",
                    2: "Fair",
                    3: "Moderate",
                    4: "Poor",
                    5: "Very Poor"
                }

                if aqi == 1:
                    st.success("Air Quality: Good")
                elif aqi == 2:
                    st.info("Air Quality: Fair")
                elif aqi == 3:
                    st.warning("Air Quality: Moderate")
                elif aqi == 4:
                    st.error("Air Quality: Poor")
                else:
                    st.error("Air Quality: Very Poor")

                components = air_data["list"][0]["components"]

                st.write("### Pollutant Levels")

                col1, col2, col3, col4, col5 = st.columns(5)

                col1.metric("PM2.5", components["pm2_5"])
                col2.metric("PM10", components["pm10"])
                col3.metric("NO2", components["no2"])
                col4.metric("O3", components["o3"])
                col5.metric("CO", components["co"])
    except KeyError:
        st.error("THAT PLACE DOES NOT EXIST")
