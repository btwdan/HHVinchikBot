from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from config import *
from statistic import Statisttic
import time

pos_count = Statisttic(0)
neg_count = Statisttic(0)

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)

b1 = KeyboardButton('👍')
b2 = KeyboardButton('👎')

kb.add(b1).insert(b2)

async def on_startup(_):
    print("Bot have started correctly!")

async def on_shutdown(_):
    print("Bot have stoped!")

@dp.message_handler(commands=["help"])
async def helpCommandFoo(message: types.Message):
    await message.reply(text=HELP_COMMAND, 
                        parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=["description"])
async def descriptionFoo(message: types.Message):
    await message.answer(text=DESCRIPTION_COMMAND, 
                         parse_mode="HTML",  
                         disable_web_page_preview=True)
    await message.delete()

@dp.message_handler(commands=["start"])
async def startFoo(message: types.Message):
    username = message.from_user.first_name
    await message.answer(text=START_COMMAND.format(username), 
                         parse_mode="HTML")
    
    await bot.send_sticker(message.from_user.id, 
                           sticker="CAACAgIAAxkBAAEK26tlaKJfxfWw2tm0fo6f1Z-jxFmlgAAC1xgAAm4m4UsFYy3CmOv8qzME",
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=["statistic"])
async def statisticFoo(message: types.Message):
    await message.answer(text=STATISTIC_COMAND.format(pos_count.get(), neg_count.get(), under50 if pos_count.get() < 50 else unde100),
                         parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=["vacancies"])
async def vacanciesFoo(message: types.Message):
    await message.answer(text="🔍")
    await asyncio.sleep(2.0)
    await message.answer("К сожаления пока вакансий нет(")
    await message.delete()

@dp.message_handler()
async def another_messages(message: types.Message):
    if message.text == "Пошел нахуй":
        await message.answer(text="Сам иди!")
    if message.text == "👍":
        await message.answer(text="Крутой перец")
        pos_count.set()
    elif message.text == "👎":
        await message.answer(text="Не крутой перец")
        neg_count.set()

if __name__== "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)