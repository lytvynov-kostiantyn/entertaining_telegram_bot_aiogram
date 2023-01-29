import openweathermap
import rate
from geopy import Nominatim
import asyncio


def weather(*args) -> str:
    if len(args) == 1:
        # checking a string for digits
        if any(ch.isdigit() for ch in args[0]):
            return 'Invalid input'
        city = args[0]
    elif len(args) == 2:
        # free openweathermap api is not support two different requests, so I convert coordinates to city
        coordinates = ' '.join(map(str, args))
        nom = Nominatim(user_agent='user')
        location = nom.reverse(coordinates).raw
        city = location['address']['city']

    data = openweathermap.get_weather(city)

    if not data:
        return 'The server is not responding, please try again later or contact administrator.'
    else:
        result = ''.join([f'{key}: {value}\n' for key, value in data.items()])
        return result


def get_rates():
    data = rate.exchange_rate()
    result = ''.join([f'{key}: {value}\n' for key, value in data.items()])
    return result
