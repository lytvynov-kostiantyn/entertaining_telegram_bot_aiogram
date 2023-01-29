import requests
from emoji import emojize
from pprint import pprint

COUNTIES = {
    'USD': f"{emojize(':United_States:')} USD",
    'EUR': f"{emojize(':European_Union:')} EUR",
    'PLN': f"{emojize(':Poland:')} PLN",
    'GBP': f"{emojize(':United_Kingdom:')} GBP",
}


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
                if val['cc'] in COUNTIES.keys():
                    flag = COUNTIES.get(val['cc'])
                    rates[flag] = f"{round(val['rate'], 3)} UAH {emojize(':Ukraine:')}"

            return rates

# exchange_rate()
