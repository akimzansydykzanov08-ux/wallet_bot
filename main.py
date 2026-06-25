import asyncio
from aiogram import Dispatcher, Bot
from config import BOT_TOKEN
from handlers import router
from database import init_db


dp = Dispatcher()
bot = Bot(BOT_TOKEN)
dp.include_router(router)

async def main():
    print("bot is running")
    init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


