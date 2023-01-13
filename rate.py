import requests
from pprint import pprint


def exchange_rate():
    try:
        response = requests.get(
            "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        )
    except requests.exceptions.RequestException:
        return "Invalid request"
    else:
        if response.status_code == 200:
            data = response.json()
            # pprint(data)

            rates = dict()
            for val in data:
                if val['cc'] in ['USD', 'EUR', 'PLN', 'GBP']:
                    rates[val['cc']] = round(val['rate'], 3)

            return rates

# exchange_rate()
