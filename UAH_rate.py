from emoji import emojize
from pprint import pprint
import asyncio
import aiohttp

COUNTIES = {
    'USD': f"{emojize(':United_States:')} USD",
    'EUR': f"{emojize(':European_Union:')} EUR",
    'PLN': f"{emojize(':Poland:')} PLN",
    'GBP': f"{emojize(':United_Kingdom:')} GBP",
}


async def exchange_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    async with aiohttp.request('get', url) as response:
        data = await response.json()
        # pprint(data)

        rates = dict()
        for val in data:
            if val['cc'] in COUNTIES.keys():
                flag = COUNTIES.get(val['cc'])
                rates[flag] = f"{round(val['rate'], 3)} UAH {emojize(':Ukraine:')}"

        if not rates:
            return 'The server is not responding, please try again later or contact administrator.'
        else:
            result = ''.join([f'{key}: {value}\n' for key, value in rates.items()])
            return result
