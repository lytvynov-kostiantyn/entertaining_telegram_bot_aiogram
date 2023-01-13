import requests
import json
from pprint import pprint


def get_location() -> str:
    try:
        response = requests.get('http://ipinfo.io/json')
    except:
        return 'Invalid request'
    else:
        data = response.json()
        return data.get('city')


print(get_location())
