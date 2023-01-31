import logging
from aiogram import Bot, Dispatcher, executor, types

from database.CRUD import create_data, read_data
from settings import BotSettings

bot_token = BotSettings().bot_token.get_secret_value()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    # print(f'{message.from_user.first_name}, {message.from_user.username}: {message.text}')
    create_data(message.from_user.username, message.from_user.first_name, message.text)
    text_message = 'Приветствую тебя, {}!'.format(message.from_user.first_name)
    await message.answer(text=text_message, parse_mode=None)


@dp.message_handler(commands=["history"])
async def cmd_history(message: types.Message):
    create_data(message.from_user.username, message.from_user.first_name, message.text)
    read_data_from_DB = read_data(message.from_user.first_name, 3)
    for i in read_data_from_DB:
        await message.answer(text=i, parse_mode=None)


@dp.message_handler()
async def echo(message: types.Message):
    create_data(message.from_user.username, message.from_user.first_name, message.text)
    await message.answer(message.text)
