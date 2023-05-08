# This is a sample Python script.

import streamlit as st

st.title("Welcome to Lap Splitter!")
st.caption("A website where you can understand the pace you need to run to go fast, win races, and qualify for championships.")

mins = st.number_input('Enter number of minutes', min_value=1)
mins_secs = mins *60
secs = st.number_input('Enter number of seconds', max_value=59)
hundreths = st.number_input('Enter Seconds to Hundreths Place:', max_value=0.99)
total_time_in_seconds = float(mins_secs + secs + hundreths)
st.write("Your goal time in seconds is: ", total_time_in_seconds)

#race_dist = st.number_input('Enter Race Distance:', min_value=800)
#st.write('Race Distance ', race_dist)
race_dist= st.radio(
    "Select your race distance",
    (800, 1500, 1600, 3000, 3200, 5000, 10000))

num_hundreds = int(race_dist / 100)
total_time_per_hundred = total_time_in_seconds / num_hundreds

for i in range(1, num_hundreds+1):
    st.write('{0}00m split: '.format(i), round(i*total_time_per_hundred,2))
#streamlit run /Users/allyryan/PycharmProjects/pythonProject16/StreamlitLapSplitter11.py