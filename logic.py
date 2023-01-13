import requests
from pprint import pprint
import weather
import rate


def get_location() -> str:
    try:
        response = requests.get('http://ipinfo.io/json')
    except requests.exceptions.RequestException:
        return 'Invalid request'
    else:
        data = response.json()
        return data.get('city')


def weather_result(city: str):
    # checking a string for digits
    if any(ch.isdigit() for ch in city):
        return 'Invalid input'

    data = weather.get_weather(city)
    if not data:
        return 'The server is not responding, please try again later or contact administrator.'
    else:
        result = ''.join([f'{key}: {value}\n' for key, value in data.items()])
        return result


def get_rates():
    data = rate.exchange_rate()
    result = ''.join([f'{key}: {value}\n' for key, value in data.items()])
    return result

# print(weather_result('123'))
