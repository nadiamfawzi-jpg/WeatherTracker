import pandas as pd 
import requests

FILE_NAME = "Data.csv"

def load_data():  
    try:
        data = pd.read_csv(FILE_NAME)
        return data
    except FileNotFoundError:
        data = pd.DataFrame(columns=["Date", "City", "Temperature", "Humidity", "Wind Speed", "Condition"]) 
        return data

def add_observation(date, city, temperature, humidity, wind_speed, condition):
    data = load_data()

    new_row = {"Date": date, "City": city, "Temperature": temperature, "Humidity": humidity, "Wind Speed": wind_speed, "Condition": condition}

    data.loc[len(data)] = new_row
    data.to_csv(FILE_NAME, index=False)


def get_all_data():
    return load_data()

def search_by_city(city):
    data = load_data()
    result = data[data["City"].str.lower() == city.lower()]
    return result 

def search_by_date(date):
    data = load_data()
    result = data[data["Date"] == str(date)]
    return result 

def get_statistics():
    data = load_data()

    if data.empty:
        return None

    stats = {"Average Temperature": round(data["Temperature"].mean(), 2), 
                  "Highest Temperature": data["Temperature"].max(), 
                  "Lowest Temperature": data["Temperature"].min(), 
                  "Average Humidity": round(data["Humidity"].mean(), 2), 
                  "Highest Humidity": data["Humidity"].max(), 
                  "Lowest Humidity": data["Humidity"].min(), 
                  "Average Wind Speed": round(data["Wind Speed"].mean(), 2), 
                  "Total Observations": len(data), 
                  "Most Common Weather": data["Condition"].mode()[0]}
    return stats 

def get_live_weather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"

    querystring = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(url, params=querystring)

    if response.status_code == 200:
        weather = response.json()

        live_weather = {"City": weather["name"], "Temperature": weather["main"]["temp"], 
                        "Humidity": weather["main"]["humidity"], 
                        "Wind Speed": round(weather["wind"]["speed"] * 3.6, 2), 
                        "Condition": weather["weather"][0]["main"]}
        return live_weather

    return None
    
def get_weather_forecast(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/forecast"

    querystring = {"q": city, "appid": api_key, "units": "metric", "cnt": 8}
    response = requests.get(url, params=querystring)

    
    if response.status_code == 200:
        weather = response.json()
        forecast = []

        for item in weather["list"]:
            forecast.append({"Date and Time": item["dt_txt"], 
                             "Temperature": item["main"]["temp"], 
                             "Humidity": item["main"]["humidity"],
                             "Condition": item["weather"][0]["main"]})
        forecast_data = pd.DataFrame(forecast)
        return forecast_data
        
    return None



       
    
