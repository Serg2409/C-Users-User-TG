import asyncio
from aiogram import Bot, Dispatcher

TOKEN = "8196132098:AAFFeJRBZCZmR65kA3UNe4iiZRS_BGtfrpY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

