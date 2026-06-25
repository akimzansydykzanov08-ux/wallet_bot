from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TRANSACTION, INCOME, STATISTIC, DAILY_LIMIT

def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=TRANSACTION), KeyboardButton(text=INCOME)],
            [KeyboardButton(text=STATISTIC), KeyboardButton(text=DAILY_LIMIT)]
            ], resize_keyboard=True
        )
    return keyboard