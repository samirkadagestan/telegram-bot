import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("8072082871:AAGzbtK7On3xiQb8vI8V38DuZjD2YI8JiTk")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- КНОПКИ ---
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👋 Привет")],
        [KeyboardButton(text="ℹ️ О боте")]
    ],
    resize_keyboard=True
)

# --- /start ---
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Cалам Алейкум\n"
        "Здесь ты можешь купить ашки по самой низкой цене😁\n\n"
        "Выбери что хочешь купить 👇",
        reply_markup=keyboard
    )

# --- Кнопка Товары ---
@dp.message(lambda message: message.text == "👋 Привет")
async def hello(message: types.Message):
    await message.answer("Привет-привет 😄 Рад тебя видеть!")

# --- Кнопка Информация ---
@dp.message(lambda message: message.text == "ℹ️ О боте")
async def about(message: types.Message):
    await message.answer(
        "🤖 Я простой Telegram-бот.\n"
        "Создан на Python с помощью aiogram."
    )

async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
