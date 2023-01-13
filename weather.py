from requests import get
import os


def get_weather(city: str):
    key = os.getenv('WEATHER_API_KEY')
    weather = dict()
    try:
        response = get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}&units=metric'
        )
    except:
        return weather
    else:
        if response.status_code == 200:
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
