import logging
from aiogram import Bot, Dispatcher, executor, types
import os
from emoji import emojize

import buttons
import openweathermap
import UAH_rate
import crypto_rate


logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('BOT_API_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        text='Hello ' + emojize(":waving_hand:"),
        reply_markup=buttons.kb_client
    )
    await message.answer(
        text="Choose one of the menu items:",
        reply_markup=buttons.MENU
    )


@dp.message_handler(commands=['help'])
async def handle_help_command(message: types.Message):
    await message.answer(text=f"""
{emojize(":robot:")} Bot features:
1. Show current weather;
{emojize(":round_pushpin:")} Show the current weather for your location (you must attach your current \
location to the message);
{emojize(":round_pushpin:")} Show the weather in the city you specified;
2. Show the official hryvnia exchange rate set by the national bank {emojize(":money_bag:")};
3. Show the latest cryptocurrency rate to USD {emojize(":money_with_wings:")}.
""")


@dp.callback_query_handler(text='weather')
async def weather_select(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text='Select option:',
        reply_markup=buttons.WEATHER_PARAMETERS
    )


@dp.callback_query_handler(text='local_weather')
async def weather_in_location(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text='Submit your location:',
    )


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    data = await openweathermap.get_weather(lat, lon)
    await message.answer(
        text=data
    )


@dp.callback_query_handler(text='city_weather')
async def weather_in_city(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text='Enter the name of the city:',
    )


@dp.message_handler(content_types=['text'])
async def get_city_name(msg: types.Message):
    data = await openweathermap.get_weather(msg.text)
    await msg.answer(
       text=data
    )


@dp.callback_query_handler(text='exchange_rate')
async def exchange_rate_select(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = await UAH_rate.exchange_rate()
    await bot.send_message(
        callback_query.from_user.id,
        text=data
    )


@dp.callback_query_handler(text='crypto_rate')
async def exchange_crypto_rate(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = await crypto_rate.get_crypto_rate()
    await bot.send_message(
        callback_query.from_user.id,
        text=data
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
