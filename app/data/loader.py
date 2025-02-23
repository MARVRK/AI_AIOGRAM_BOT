from aiogram import  Dispatcher, Bot
from app.data.config import settings

bot= Bot(settings.BOT_TOKEN)
dp = Dispatcher(bot=bot)