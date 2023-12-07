from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import *


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)

b1 = KeyboardButton('/help')
b2 = KeyboardButton('/start')
b3 = KeyboardButton('/description')

kb.add(b1).insert(b2).add(b3)

async def on_startup(_):
    print("Bot have started correctly!")

async def on_shutdown(_):
    print("Bot have stoped!")

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply(message.from_user.id,
                        text=HELP_COMMAND, 
                        parse_mode="HTML")

@dp.message_handler(commands=["description"])
async def descriptionFoo(message: types.Message):
    await message.answer(message.from_user.id,
                         text=DESCRIPTION_COMMAND, 
                         parse_mode="HTML",  
                         disable_web_page_preview=True)
    await message.delete()

@dp.message_handler(commands=["start"])
async def startFoo(message: types.Message):
    await message.answer(START_COMMAND, parse_mode="HTML")
    await bot.send_sticker(message.from_user.id, 
                           sticker="CAACAgIAAxkBAAEK26tlaKJfxfWw2tm0fo6f1Z-jxFmlgAAC1xgAAm4m4UsFYy3CmOv8qzME",
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=["give"])
async def sticker(message: types.Message):
    await message.answer(text="Смотри какой смешной кот ❤️")
    await bot.send_sticker(message.from_user.id,  
                           sticker="CAACAgQAAxkBAAEK3q9lac256UChlEuQd0tN6OQcd4IFWwACMQADzjkIDct1CToayEPXMwQ")

@dp.message_handler()
async def sms(message: types.Message):
    if message.text == "🖤":
        await message.answer(text="❤️")

if __name__== "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)