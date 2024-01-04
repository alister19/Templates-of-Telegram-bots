from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

BOT_TOKEN = 'YOUR TOKEN'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Созхдаем объекты инлайн-кнопок
url_button_1 = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и AIOgram"',
    url = 'https://stepik.org/120924'
)
url_button_2 = InlineKeyboardButton(
    text='Документация Telegram Bot API',
    url = 'https://core.telegram.org/bots/api'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2]]
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки с параметром "url"',
        reply_markup=keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)