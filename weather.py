import requests
import os


def get_weather(city: str):
    key = os.getenv('WEATHER_API_KEY')
    weather = dict()
    try:
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}&units=metric'
        )
    except requests.exceptions.RequestException:
        return weather
    else:
        data = response.json()

        weather = {
            'Country': data['sys']['country'],
            'City': data['name'],
            'Longitude': data['coord']['lon'],
            'Latitude': data['coord']['lat'],
            'Weather': data['weather'][0]['main'],
            'Temperature': data['main']['temp'],
        }

        return weather
