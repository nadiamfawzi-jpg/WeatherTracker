import streamlit as st
import pandas as pd
def read():
    return pd.read_csv('Data.csv')    
def weather():
    df = read()
    weather = df.sample()
    return weather

"""
weather_utils.py

This module contains all the functions used to
manage weather observations.
"""

import pandas as pd

FILE_NAME = "Data.csv"


def load_data():
    """
    Loads the weather observations from the CSV file.

    Returns:
        pandas.DataFrame
    """

    try:
        weather_data = pd.read_csv(FILE_NAME)

    except FileNotFoundError:
        weather_data = pd.DataFrame(
            columns=[
                "Date",
                "City",
                "Temperature",
                "Humidity",
                "Wind Speed",
                "Condition"
            ]
        )

    return weather_data


def add_observation(date, city, temperature, humidity, wind_speed, condition):
    """
    Adds one weather observation to the CSV file.
    """

    weather_data = load_data()

    new_observation = {
        "Date": date,
        "City": city,
        "Temperature": temperature,
        "Humidity": humidity,
        "Wind Speed": wind_speed,
        "Condition": condition
    }

    weather_data.loc[len(weather_data)] = new_observation

    weather_data.to_csv(FILE_NAME, index=False)

    


def get_all_data():
    """
    Returns every weather observation.
    """

    return load_data()


def search_by_city(city):
    """
    Search observations by city.
    """

    weather_data = load_data()

    results = weather_data[
        weather_data["City"].str.lower() == city.lower()
    ]

    return results


def search_by_date(date):
    """
    Search observations by date.
    """

    weather_data = load_data()

    results = weather_data[
        weather_data["Date"] == str(date)
    ]

    return results


def get_statistics():
    """
    Calculates summary statistics.
    """

    weather_data = load_data()

    if weather_data.empty:
        return None

    statistics = {
        "Average Temperature": round(weather_data["Temperature"].mean(), 2),
        "Highest Temperature": weather_data["Temperature"].max(),
        "Lowest Temperature": weather_data["Temperature"].min(),
        "Average Humidity": round(weather_data["Humidity"].mean(), 2),
        "Highest Humidity": weather_data["Humidity"].max(),
        "Lowest Humidity": weather_data["Humidity"].min(),
        "Average Wind Speed": round(weather_data["Wind Speed"].mean(), 2),
        "Total Observations": len(weather_data),
        "Most Common Weather": weather_data["Condition"].mode()[0]
    }

    return statistics

weather_data = get_all_data()
def get_all_data():
    return load_data()
    st.dataframe(weather_data)
    
    



    

    
    
    

    


    