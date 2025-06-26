# Fetch weather data from OpenWeatherMap API
import requests
import os

api_key = "f22c202a9311ef05a9767a14eae449d3"


def get_weather(city, api_key):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 401:
        print("Invalid or missing API key. Please check your OpenWeatherMap API key.")
        return
    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        temp = main.get('temp')
        humidity = main.get('humidity')
        description = weather.get('description')
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description}")
    else:
        print(f"Failed to get weather data for {city}. Error code: {response.status_code}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city, api_key)
