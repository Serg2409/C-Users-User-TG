import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv("BOT_TOKEN")  # Бот отримає токен із налаштувань Render

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привіт! Я Telegram-бот!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
