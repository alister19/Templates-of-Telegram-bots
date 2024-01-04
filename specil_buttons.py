from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, \
                          Message
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

BOT_TOKEN = 'YOUR_TOKEN'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)
poll_btn = KeyboardButton(
    text='Создать опрос/викторину',
    request_poll=KeyboardButtonPollType()
)
web_app_btn = KeyboardButton(
    text='Start Web App',
    web_app=WebAppInfo(url='https://stepik.org')
)

# Добаляем кнопки в билдер
kb_builder.row(
    contact_btn, geo_btn, poll_btn, width=1
)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True, on_time_keyboard=True
)
web_app_keyboard = ReplyKeyboardMarkup(
    keyboard=[[web_app_btn]],
    resize_keyboard=True
)

# Этот хэндлер будет срабатывать на команду /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=web_app_keyboard
    )

if __name__ == '__main__':
    dp.run_polling(bot)
