import requests
import os
from pprint import pprint

directions = {
    0: 'North',
    1: 'Northeast',
    2: 'East',
    3: 'Southeast',
    4: 'South',
    5: 'Southwest',
    6: 'West',
    7: 'Northwest',
    8: 'North',

}


def wind_convert(deg: int) -> str:
    direction = round(deg / 45)
    return directions[direction]


def get_weather(city: str) -> dict:
    key = os.getenv('WEATHER_API_KEY')
    weather = dict()
    try:
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}&units=metric'
        )
    except requests.exceptions.RequestException:
        return weather
    else:
        if response.status_code == 200:
            data = response.json()
            # pprint(data)
            weather = {
                'Country': data['sys']['country'],
                'City': data['name'],
                'Weather': data['weather'][0]['main'],
                'Temperature, °C': data['main']['temp'],
                'Temperature(feels like), °C': data['main']['feels_like'],
                'Wind direction': wind_convert(data['wind']['deg']),
                'Wind speed, m/s': data['wind']['speed'],
            }

        return weather

# pprint(get_weather('123'))
# pprint(get_weather('odesa'))
