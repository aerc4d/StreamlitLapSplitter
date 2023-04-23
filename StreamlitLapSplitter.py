# This is a sample Python script.



import streamlit as st
from streamlit_option_menu import option_menu

EXAMPLE_NO = 3

def streamlit_menu(example=3):
    if example == 3:
        selected = option_menu(
            menu_title=None,  # required
            options=["Home"],
            icons=["house"],
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    st.title("Lap Splitter")


if selected == "Home":
    Home = st.selectbox('Home: Select one option:', ['', 'Lap Splitter'], format_func=lambda x: 'Select an option' if x == '' else x)
    if Home == 'Lap Splitter':
        st.markdown("# This will split laps")
        st.markdown("""
                    This is to split laps.
                    """)
        mins = st.number_input('Insert number of minutes')
        st.write('The number of minutes is ', mins)
        mins_secs = mins *60

        secs = st.number_input('Insert number of seconds')
        st.write('The number of seconds is ', secs)

        hundreths = st.number_input('Enter Seconds to Hundreths Place:')
        st.write('Seconds to Hundreths: ', hundreths)
        hundreths_decimal = float(hundreths / 100)


        total_time_in_seconds = float(mins_secs + secs + hundreths_decimal)
        st.write(total_time_in_seconds)

        race_dist = st.number_input('Enter Race Distance:')
        st.write('Race Distance ', race_dist)
        num_hundreds = int(race_dist / 100)
        st.write('Number of Hundreds: ', num_hundreds)
        total_time_per_hundred = total_time_in_seconds / num_hundreds
        st.write('100 time: ', total_time_per_hundred)


        for i in range(1, num_hundreds+1):
            st.write('{0}00m split: '.format(i), round(i*total_time_per_hundred,2))

#streamlit run /Users/allyryan/PycharmProjects/pythonProject16/StreamlitLapSplitter.py
