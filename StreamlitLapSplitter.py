# This is a sample Python script.



import streamlit as st

EXAMPLE_NO = 3





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
