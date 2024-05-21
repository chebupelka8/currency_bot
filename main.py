import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

import colorama

from src import *


TOKEN = Loader.get_token()


if TOKEN is not None: bot = Bot(TOKEN)
else: raise KeyError("There isn't such token.")

dp = Dispatcher()

DataBase.create_table()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello!")
    # await message.answer(load_currency(get_currency_soup("USD")))

    keys = [[types.KeyboardButton(text=i)] for i in get_currencies_name()]
    keyboard = types.ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    await message.answer("Choose currency", reply_markup=keyboard)

    if message.from_user is not None:
        DataBase.add_user(message.from_user.id, message.from_user.first_name, "std")
        print(f"Added {DataBase.get_user(message.from_user.id)}")

@dp.message()
async def load(message: types.Message):
    if message.text is not None:
        print(message.text)
        if message.text.upper() in get_currencies_name():
            await message.answer(load_currency(get_currency_soup(message.text.upper())))
    
    return


async def on_startup():
    print(colorama.Fore.LIGHTGREEN_EX + f"{(await bot.get_my_name()).name} was started..." + colorama.Style.RESET_ALL)


if __name__ == "__main__":
    dp.startup.register(on_startup)
    asyncio.run(dp.start_polling(bot))
