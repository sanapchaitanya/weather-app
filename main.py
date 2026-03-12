import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("place: ")
days = st.slider("forecast Days", min_value=1, max_value=5,
                 help='Select the number of days to forecast')
option = st.selectbox("select data to view",
                      ("temperature", "sky"))
st.subheader(f"{option} for the next {days} days in {place}")
