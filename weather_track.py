import streamlit as st
import pandas as pd
from weather_utils import *

st.set_page_config(
    page_title="Weather Tracker",
    page_icon="🌤️",
    layout="wide"
)

st.title("🌤️ Weather Observation Tracker")

st.write("""
Welcome to the Weather Observation Tracker!

This application allows you to:
- Record daily weather observations
- View previous observations
- Search observations
- Analyze weather patterns over time
""")

menu = st.sidebar.selectbox(
    "Choose an option",
    ["Home", "Add Observation", "View Observations", "Search", "Statistics"]
)

if menu == "Home":
    st.header("Home")
    st.write("Select an option from the sidebar.")

elif menu == "Add Observation":
    st.header("Add Weather Observation")

    date = st.date_input("Select the Date")
    city = st.text_input("Enter the City")
    temperature = st.number_input(
    "Temperature (°C)",
    min_value=-20,
    max_value=60,
    value=25
)
    humidity = st.number_input(
    "Humidity (%)",
    min_value=0,
    max_value=100,
    value=50
)
    wind_speed = st.number_input(
    "Wind Speed (km/h)",
    min_value=0,
    max_value=200,
    value=10
)
    condition = st.selectbox(
        "Weather Condition",
        ["Sunny", "Cloudy", "Rainy", "Windy", "Stormy"]
    )
    
if st.button("Save Observation"):
        city = city.strip().title()
        if city == "":
            st.error("Please enter a city name.")
        else:
            add_observation(date=str(date), city=city, temperature=temperature, humidity=humidity, wind_speed=wind_speed, condition=condition)
            st.success("Observation saved successfully!") 

elif menu == "View Observations":
    st.header("📋 All Weather Observations")

    weather_data = get_all_data()

    if weather_data.empty:
        st.warning("No weather observations found.")
    else:
        st.success(f"Total observations: {len(weather_data)}")
        st.dataframe(
    weather_data,
    use_container_width=True
)

        csv_file = weather_data.to_csv(index=False)
        
    st.download_button(
    label="📥 Download Weather Data",
    data=csv_file,
    file_name="weather_observations.csv",
    mime="text/csv"
)
        
    st.download_button(
    label="Download Data as CSV",
    data=csv_file,
    file_name="weather_observations.csv",
    mime="text/csv" )  

elif menu == "Search":
    st.header("🔍 Search Weather Observations")

    search_option = st.radio(
        "Search by:",
        ["City", "Date"]
    )

    if search_option == "City":
        city_search = st.text_input("Enter City Name")

        if st.button("Search by City"):
            results = search_by_city(city_search)

            if results.empty:
                st.warning("No observations found.")
            else:
                st.dataframe(results)

    else:
        date_search = st.date_input("Select Date")

        if st.button("Search by Date"):
            city_search = city_search.strip().title() 
            results = search_by_date(date_search)

            if results.empty:
                st.warning("No observations found.")
            else:
                st.dataframe(results)

elif menu == "Statistics":
    st.header("📊 Weather Statistics")

    statistics = get_statistics()

    if statistics is None:
        st.warning("No data available to calculate statistics.")
    else:
        st.metric("Average Temperature", f"{statistics['Average Temperature']} °C")
        st.metric("Highest Temperature", f"{statistics['Highest Temperature']} °C")
        st.metric("Lowest Temperature", f"{statistics['Lowest Temperature']} °C")
        st.metric("Average Humidity", f"{statistics['Average Humidity']} %")
        st.metric("Average Wind Speed", f"{statistics['Average Wind Speed']} km/h")
        st.metric("Total Observations", statistics["Total Observations"])
        st.metric("Most Common Weather", statistics["Most Common Weather"]) 
        
        st.subheader("📈 Temperature Over Time")
        weather_data = get_all_data()
        
        st.write(weather_data.columns)
        st.dataframe(
    weather_data,
    use_container_width=True
)
        
        weather_data["Date"] = pd.to_datetime(weather_data["Date"])

        temperature_chart = weather_data.set_index("Date")["Temperature"]

        st.line_chart(temperature_chart)


        st.subheader("💧 Humidity Over Time")

        humidity_chart = weather_data.set_index("Date")["Humidity"]

        st.line_chart(humidity_chart)


        st.subheader("🌤️ Weather Condition Count")

        condition_count = weather_data["Condition"].value_counts()

        st.bar_chart(condition_count)

        
        
        
        
    















        

        

        

        









    

    

        

        

    

    


    

    


    

    

    
    
    






              

    

    