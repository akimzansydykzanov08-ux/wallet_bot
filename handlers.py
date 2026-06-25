from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from config import TRANSACTION, INCOME, STATISTIC, DAILY_LIMIT
from keyboards import get_main_keyboard
from aiogram.fsm.context import FSMContext

from states import Add_expense, Add_income
from database import add_transaction, get_balance, get_today_expenses


router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("hello, i am yuor pocket wallet", 
                         reply_markup=get_main_keyboard())



    # РАСХОД-------------------------------------------------------------
    @router.message(F.text==TRANSACTION)
    async def expense_handler(message: Message, state: FSMContext):

        await message.answer("Напиши сумму расхода")
        await state.set_state(Add_expense.waiting_for_expense)

    @router.message(Add_expense.waiting_for_expense)
    async def procces_money(message: Message, state: FSMContext):
        transaction = message.text

        if not transaction.isdigit():
            await message.answer("Нужно писать цифры, ублюдок!")
            return

        add_transaction(
            user_id=message.from_user.id,
            amount=int(transaction),
            trans_type="expense"
            )

        await message.answer("Данные успешно внесены!")
        await state.clear()


    #ДОХОД--------------------------------------------------------------------

    @router.message(F.text==INCOME)
    async def income_handler(message: Message, state: FSMContext):
    


        await message.answer("Напишите сумму дохода")
        await state.set_state(Add_income.waiting_for_income)

    @router.message(Add_income.waiting_for_income)
    async def procces_income(message: Message, state: FSMContext):
        income = message.text

        if not income.isdigit():
            await message.answer("Нужно писать цифры, ублюдок!")
            return

        add_transaction(
            user_id=message.from_user.id,
            amount=int(income),
            trans_type="income"
            )

        await message.answer("Данные успешно внесены!")
        await state.clear()

#СТАТИСТИКА--------------------------------------------------------------------

@router.message(F.text==STATISTIC)
async def statistic_handler(message: Message):
    user_id = message.from_user.id

    total_income, total_expense = get_balance(user_id)

    current_balance = total_income - total_expense

    text = (
        f"📊 *Твоя финансовая статистика:*\n\n"
        f"💰 Общий доход: `{total_income}` тенге\n"
        f"💸 Общий расход: `{total_expense}` тенге\n"
        f"───────────────────\n"
        f"💳 Текущий баланс: *{current_balance} тенге*"
    )
    await message.answer(text, parse_mode="Markdown")

@router.message(F.text==DAILY_LIMIT)
async def daily_limit_handler(message: Message):
    user_id = message.from_user.id

    spent_today = get_today_expenses(user_id)

    fixed_limit = 2000

    limit_left = fixed_limit - spent_today

    if limit_left > 0:
        await message.answer(
            f"💵 *Твой лимит на день:* {fixed_limit} тенге\n"
            f"📉 Сегодня уже потрачено: {spent_today} тенге\n"
            f"💰 Осталось потратить: *{limit_left} тенге*",
            parse_mode="Markdown"
        )
    else:
        await message.answer(
            f"🚨 *Лимит исчерпан!*\n"
            f"Ты просрал все 2000 тенге и ушел в минус на {abs(limit_left)} тенге! Оторвись от кассы! 🪓",
            parse_mode="Markdown"
        )

                
