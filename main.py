import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from handlers import question, different_types
from DataBase.DBSQL import DataB
async def main():
    bot = Bot(token='6601951999:AAFTizUh_4d_Im2uLLuMMq9FHphuN0hJTmY', parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_routers(question.router, different_types.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

