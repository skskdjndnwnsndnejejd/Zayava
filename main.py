
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.start import start_router
from handlers.rules import rules_router
from handlers.form import form_router
from handlers.menu import menu_router
from handlers.builds import builds_router

async def main():
    token = os.getenv("BOT_TOKEN")
    bot = Bot(token=token, parse_mode=ParseMode.MARKDOWN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start_router)
    dp.include_router(rules_router)
    dp.include_router(form_router)
    dp.include_router(menu_router)
    dp.include_router(builds_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
