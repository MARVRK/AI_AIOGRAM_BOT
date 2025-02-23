import asyncio
import logging
from app.data.loader import bot
from app.services import admin_menu

from aiogram import Bot, Dispatcher


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s',
    handlers=[
        logging.FileHandler(filename="ai_bot.log", mode='a', encoding="utf-8"),
        logging.StreamHandler()])

log = logging.getLogger(__name__)


dp = Dispatcher()

async def main() -> None:
    # log.info("Starting Ai bot")
    dp.include_router(admin_menu.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
