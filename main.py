import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("place: ")
days = st.slider("forecast Days", min_value=1, max_value=5,
                 help='Select the number of days to forecast')
option = st.selectbox("select data to view",
                      ("temperature", "sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10", "2022-28-10", "2022-29-10"]
    temperature = [10, 11, 15, 20, 21]
    temperature = [days * i for i in temperature]
    return dates, temperature

d, t = get_data(days)

figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (celsius)"})
st.plotly_chart(figure)
