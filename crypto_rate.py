from pprint import pprint
import asyncio
import aiohttp
from emoji import emojize


async def get_crypto_rate():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2CLitecoin%2Csolana%2Cdogecoin&vs_currencies=usd"
    async with aiohttp.request('get', url) as response:
        data = await response.json()
        # pprint(data)

        crypto_rates = {
            'Bitcoin': data['bitcoin']['usd'],
            'Solana': data['solana']['usd'],
            'Litecoin': data['litecoin']['usd'],
            'Dogecoin': data['dogecoin']['usd'],
            'Ethereum': data['ethereum']['usd'],
        }

        if not crypto_rates:
            return 'The server is not responding, please try again later or contact administrator.'
        else:
            sorted_dict = dict(sorted(crypto_rates.items()))
            result = ''.join([f'{key}: {value:.3f} ＄\n' for key, value in sorted_dict.items()])
            return result
