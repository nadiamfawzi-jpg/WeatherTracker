import streamlit as st 
import pandas as pd   
from weather_utils import (add_observation, get_all_data, search_by_city, search_by_date, get_statistics)




st.set_page_config(page_title = "weather_tracker", page_icon = "🌤️", layout= "wide")

st.title("🌤️Weather Observation Tracker")

st.write(""" Welcome to the Weather Observation Tracker. 

This app helps you record daily weather observations, view saved data, search by city or date, and check simple weather statistics. """)

menu = st.sidebar.selectbox("choose a page", ["Home", "Add Observation", "View Observations", "Search", "Statistics"])

if menu == "Home":
    st.header("Home")
    st.write("Use the sidebar to add, view, search, or analyze weather observations.")

elif menu == "Add Observation":
    st.header("Add Weather Observation")
    date = st.date_input("Date")
    city = st.text_input("City")
    temperature = st.number_input("Temperature (°c)", min_value = -20, max_value = 60, value = 25)
    humidity = st.number_input("Humidity (%)", min_value = 0, max_value = 100, value = 50)
    wind_speed = st.number_input("Wind Speed (km/h)", min_value = 0, max_value = 200, value = 10)
    condition = st.selectbox("Weather Condition", ["Sunny", "Cloudy", "Rainy", "Windy", "Stormy"])

    if st.button("Save Observation"):
        city = city.strip().title()

        if city == "":
            st.error("Please enter a city name.")
        else:
            add_observation(date = str(date), city = city, temperature = temperature, humidity = humidity, wind_speed = wind_speed, condition = condition)
            st.success("Observation Saved Successfully")

elif menu == "View Observations":
    st.header("📋 All Weather Observation")
    weather_data = get_all_data()

    if weather_data.empty:
        st.warning("No weather observations found.")
    else:
        st.success(f"Total observations: {len(weather_data)}")
        st.dataframe(weather_data, use_container_width=True)

        csv_file = weather_data.to_csv(index=False)
        st.download_button(label= "Download Data as CSV", data= csv_file, file_name= "weather_observation.csv", mime= "text/csv")

elif menu == "Search":
    st.header("🔍 Search Weather Observations")

    search_option = st.radio("Search by:", ["City","Date"])

    if search_option == "City":
        city_search = st.text_input("Enter city name")
        if st.button("search"):
            city_search = city_search.strip().title()

            if city_search == "":
                st.error("Please enter a city name")
            else:
                result = search_by_city(city_search)
                
                if result.empty:
                    st.warning("No observations found for this city")
                else:
                    st.dataframe(result, use_container_width=True)

    else:
        date_search = st.date_input("Select date")
        if st.button("Search"):
            result = search_by_date(date_search)
            if result.empty:
                st.warning("No observations found for this date")
            else:
                st.dataframe(result, use_container_width=True)

elif menu == "Statistics":
    st.header("📊 Weather Statistics")
    statistics = get_statistics()
    if statistics is None: 
        st.warning("No observations found for this statistics")
    else:
        st.metric("Average Temperature", f"{statistics['Average Temperature']} °c")
        st.metric("Highest Temperature", f"{statistics['Highest Temperature']} °c")
        st.metric("Lowest Temperature", f"{statistics['Lowest Temperature']} °c")
        st.metric("Average Humidity", f"{statistics['Average Humidity']} %")
        st.metric("Average Wind Speed", f"{statistics['Average Wind Speed']} km/h")
        st.metric("Total observations", statistics['Total Observations'])
        st.metric("Most common weather", statistics['Most Common Weather'])

        weather_data = get_all_data()
        weather_data["Date"] = pd.to_datetime(weather_data["Date"])
        st.subheader("📈 Temperature ove time")
        temperature_chart = weather_data.set_index("Date")["Temperature"]
        st.line_chart(temperature_chart)

        st.subheader("💧 Humidity over time")
        humidity_chart = weather_data.set_index("Date")["Humidity"]
        st.line_chart(humidity_chart)

        st.subheader("🌤️ Weather Condition Count")
        condition_count = weather_data["Condition"].value_counts()
        st.bar_chart(condition_count) 
        
    















        

        

        

        









    

    

        

        

    

    


    

    


    

    

    
    
    






              

    

    