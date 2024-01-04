from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

BOT_TOKEN = 'YOUR_TOKEN'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем список с кнопками
buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(10)
]

# Распаковываем список с кнопками в билдер, указываем, что
# в одном ряду должно быть 4 кнопки.
kb_builder.row(*buttons, width=4)

# Этот хэндлер будет срабатывать на команду /start
# и отправляет в чат клавиатуру.
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Вот такая получается клавиатура',
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )

if __name__ == '__main__':
    dp.run_polling(bot)