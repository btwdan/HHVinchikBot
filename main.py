from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import *


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

@dp.message_handler(commands=["description"])
async def descriptionFoo(message: types.Message):
    await message.answer(text=DESCRIPTION_COMMAND, 
                         parse_mode="HTML",  
                         disable_web_page_preview=True)
    await message.delete()

@dp.message_handler(commands=["start"])
async def startFoo(message: types.Message):
    await message.answer(text=START_COMMAND, 
                         parse_mode="HTML")
    
    await bot.send_sticker(message.from_user.id, 
                           sticker="CAACAgIAAxkBAAEK26tlaKJfxfWw2tm0fo6f1Z-jxFmlgAAC1xgAAm4m4UsFYy3CmOv8qzME",
                           reply_markup=kb)
    await message.delete()

@dp.message_handler()
async def another_messages(message: types.Message):
    if message.text == "Пошел нахуй":
        await message.answer(text="Сам иди!")
    if message.text == "👍":
        await message.answer(text="Крутой перец")
    elif message.text == "👎":
        await message.answer(text="Не крутой перец")

if __name__== "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)