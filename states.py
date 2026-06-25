from aiogram.fsm.state import StatesGroup, State

class Add_expense(StatesGroup):
    waiting_for_expense = State()

class Add_income(StatesGroup):
    waiting_for_income = State()
    