from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = "7689778723:AAFdlwxKJ_hM_OEEVJqJI893QRHQkCQVY8M"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
