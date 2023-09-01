import requests

# Enter your OpenWeatherMap API key here
api_key = "d157e44f7f8de79b4e34f1d9734c4e52"

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "d157e44f7f8de79b4e34f1d9734c4e52",
        "units": "imperial"  # You can change units to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        print(f"Weather in {city}: {weather_desc}, Temperature: {temperature}°C")
    else:
        print("Error fetching weather data")

if __name__ == "__main__":
    city = input("Waldorf: ")
    get_weather("Waldorf")

