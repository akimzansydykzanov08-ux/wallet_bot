import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

TRANSACTION = "Учет"
INCOME = "Доход"
STATISTIC = "Статистика"
DAILY_LIMIT = "Лимит"