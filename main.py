import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("place: ")
days = st.slider("forecast Days", min_value=1, max_value=5,
                 help='Select the number of days to forecast')
option = st.selectbox("select data to view",
                      ("temperature", "sky"))
st.subheader(f"{option} for the next {days} days in {place}")

d, t = get_data(place, days, option)

d, t = get_data(days)

figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (celsius)"})
st.plotly_chart(figure)
