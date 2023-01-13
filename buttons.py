from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_WEATHER = InlineKeyboardButton('Weather', callback_data='weather')
BTN_EXCHANGE_RATE = InlineKeyboardButton('Official exchange rate UAH', callback_data='exchange_rate')
MENU = InlineKeyboardMarkup().add(BTN_WEATHER).add(BTN_EXCHANGE_RATE)


LOCAL_WEATHER = InlineKeyboardButton('Weather in your current location', callback_data='local_weather')
CITY_WEATHER = InlineKeyboardButton('Weather in a particular city', callback_data='city_weather')
WEATHER_PARAMETERS = InlineKeyboardMarkup().add(LOCAL_WEATHER).add(CITY_WEATHER)
