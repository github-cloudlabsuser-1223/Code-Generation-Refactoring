# Fetch weather data from OpenWeatherMap One Call API 3.0
import requests
import os

api_key = "f22c202a9311ef05a9767a14eae449d3"

def get_coordinates(city, api_key):
    # Use OpenWeatherMap Geocoding API to get latitude and longitude for the city
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    response = requests.get(geo_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
        else:
            print(f"City '{city}' not found.")
            return None, None
    else:
        print(f"Failed to get coordinates for {city}. Error code: {response.status_code}")
        return None, None

def get_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 401:
        print("Invalid or missing API key. Please check your OpenWeatherMap API key.")
        return
    if response.status_code == 200:
        data = response.json()
        current = data.get('current', {})
        temp = current.get('temp')
        humidity = current.get('humidity')
        weather = current.get('weather', [{}])[0]
        description = weather.get('description')
        print(f"Current weather:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description}")
    else:
        print(f"Failed to get weather data. Error code: {response.status_code}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    lat, lon = get_coordinates(city, api_key)
    if lat is not None and lon is not None:
        get_weather(lat, lon, api_key)
