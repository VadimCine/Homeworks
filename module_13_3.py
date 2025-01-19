from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7701027879:AAHCWlz67A3rRVjM5ts7ybe5DfPDhhyfIzw"
bot = Bot(token=api)
db = Dispatcher(bot, storage = MemoryStorage())

@db.message_handler(commands=["start"])
async def start(message):
    #print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@db.message_handler()
async def all_message(message):
    #print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(db, skip_updates=True)

