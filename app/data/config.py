from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DB_URL")
    OPENAI_API_KEY = os.getenv("AI_TOKEN")
    BOT_TOKEN = os.getenv("BOT_TOKEN")

settings = Settings()