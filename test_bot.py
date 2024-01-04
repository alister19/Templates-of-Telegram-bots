from aiogram import Bot, Dispatcher
from aiogram.types import Message

BOT_TOKEN = 'YOUR_BOT_TOKEN'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Фильтр по команде /start
def my_start_filter(message: Message) -> bool:
    return message.text == '/start'

@dp.message(my_start_filter)
async def process_start_command(message: Message):
    await message.answer(text='Это команда /start')

if __name__ == '__main__':
    dp.run_polling(bot)