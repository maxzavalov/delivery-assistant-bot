import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()  # Загружаем переменные из .env

storage = MemoryStorage()
dp = Dispatcher(storage=storage)




async def main():
    # Используем токен из .env и настройки по умолчанию
    bot = Bot(
        token=os.getenv("BOT_TOKEN"),
        default=DefaultBotProperties()
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Проверка токена перед запуском
    if not os.getenv("BOT_TOKEN"):
        raise ValueError("Токен не найден в .env!")

    asyncio.run(main())