import os
from pprint import pprint
from emoji import emojize
import asyncio
import aiohttp

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


async def get_weather(*args) -> str:
    key = os.getenv('WEATHER_API_KEY')

    if len(args) == 1:
        # checking a string for digits
        if any(ch.isdigit() for ch in args[0]):
            return 'Invalid input'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={args[0]}&APPID={key}&units=metric'

    elif len(args) == 2:
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={args[0]}&lon={args[1]}&appid={key}&units=metric'

    async with aiohttp.request('get', url) as response:
        data = await response.json()
        if data['cod'] == "404":
            return 'City not found'
        # pprint(data)

    weather = {
        'Country': data['sys']['country'],
        'City': data['name'],
        'Weather': data['weather'][0]['main'],
        f'{emojize(":thermometer:")} Temperature, °C': data['main']['temp'],
        f'{emojize(":thermometer:")} Temperature(feels like), °C': data['main']['feels_like'],
        f'{emojize(":dashing_away:")} Wind direction': wind_convert(data['wind']['deg']),
        f'{emojize(":dashing_away:")} Wind speed, m/s': data['wind']['speed'],
    }

    if not weather:
        return 'The server is not responding, please try again later or contact administrator.'
    else:
        result = ''.join([f'{key}: {value}\n' for key, value in weather.items()])
        return result
