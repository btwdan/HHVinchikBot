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

Я могу тебе скидывать объясвление о работе а ты в свою очередб выбирать нравится "👍" или не нравится "👎", в зависимости от твоего ответа будет отправляться твой отклик работадателю или мы перейдем к следующему объявлению)

Желаю тебе успешного поиска работы!😀
"""

START_COMMAND = """
<em>Привет я помогу тебе найти работу❤️</em>
"""