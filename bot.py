import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "8072082871:AAGzbtK7On3xiQb8vI8V38DuZjD2YI8JiTk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет! Я твой первый Telegram-бот 🤖")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())