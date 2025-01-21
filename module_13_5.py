from cgitb import handler

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

from module_13_2 import start

api = "7701027879:AAHCWlz67A3rRVjM5ts7ybe5DfPDhhyfIzw"
bot = Bot(token=api)
db = Dispatcher(bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard = True)
calc_b = KeyboardButton(text = "Рассчитать")
kb.insert(calc_b)
info_b = KeyboardButton(text = "Информация")
kb.insert(info_b)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@db.message_handler(commands=["start"])
async def start(message):
    #print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup = kb)

@db.message_handler(text = "Информация")
async def calc(message):
    await message.answer("Бот, рассчитывающий твою дневную норму калорий.")

@db.message_handler(text = "Рассчитать")
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@db.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@db.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@db.message_handler()
async def all_message(message):
    #print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")

@db.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = float(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    await message.answer(f'Ваша норма калорий - {result}')
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(db, skip_updates=True)

