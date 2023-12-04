import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from handlers import question, different_types


async def main():
    bot = Bot(token='6511413380:AAFeQnExRJjMeJ5UPdVNtQC5Ddm0S6HxKB8', parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_routers(question.router, different_types.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

