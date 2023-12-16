import asyncio
from contextlib import suppress
from aiogram import types
from aiogram.utils.exceptions import (MessageCantBeDeleted, MessageToDeleteNotFound)
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_API = os.environ.get("TOKEN")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

HELP_COMMAND = """
Итак давай пройдемся по тому что я могу делать)
<b>/description</b> - <em>описание бота</em>
<b>/vacancies</b> - <em>начать просматривать вакансии</em>
<b>/statistic</b> - <em>статистика</em>
"""

DESCRIPTION_COMMAND = """
Я <b>бот-помощник</b>🤖 в поисках твоей работы, я работаю с помощью официального <a  href="https://dev.hh.ru/">HH API</a>😌. 

Подключение к твоему аккаунту происходит через протокол <a href="https://github.com/hhru/api/blob/master/docs/authorization.md">OAuth</a>🔐 который не передает твои личные данные. 

Поэтому тебе не стоит беспокоиться о своей безопастности😉.

Я могу тебе скидывать объясвление о работе а ты в свою очередь выбирать нравится "👍" или не нравится "👎", в зависимости от твоего ответа будет отправляться твой отклик работадателю или мы перейдем к следующему объявлению)

Желаю тебе успешного поиска работы!😀
"""

START_COMMAND = """
<em>Привет <b>{0}</b>, я помогу тебе найти работу❤️</em>
"""

STATISTIC_COMAND = """
<em>Твоя статистка:</em>

👍 - <b>{0}</b>

👎 - <b>{1}</b>

<em>{2}</em>
"""

under50 = 'Начало положено как правилло каждые 10 откликов приносят один офер, не нужно растраиваться😀'
unde100 = 'Уже отправлено достаточно откликов, видать просто ты ЧМО ебаное которое нах никому не нужно😉'

async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()