import logging
from aiogram import Bot, Dispatcher, executor, types
import os

import logic
import buttons


logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('BOT_API_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def main(message: types.Message):
    await message.answer(
        text="Hello, choose one of the menu items:",
        reply_markup=buttons.WEATHER
    )


@dp.callback_query_handler(text='weather')
async def with_puree(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text='Select option:',
        reply_markup=buttons.WEATHER_PARAMETERS
    )


@dp.callback_query_handler(text='local_weather')
async def with_puree(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=logic.weather_result(logic.get_location()),
    )


@dp.callback_query_handler(text='city_weather')
async def with_puree(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text='Enter the name of the city:',
    )


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет!')
   else:
       await msg.answer('Не понимаю, что это значит.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
