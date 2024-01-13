"""Отпарвка ноавого сообщения без удаления старого"""

import random

from aiogram import Bot, Dispatcher, F 
from aiogram.filters import Command
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

BOT_TOKEN = 'YOU_TOKEN'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

jokes: dict[int, str] = {
    1: 'Привет! Похоже я сошел с ума. Но, это не точно',
    2: 'У меня на одном курсе был сосед, который жевал козявки',
    3: 'Я его не виню за это. У каждого свои тараканы в голове и дурь',
    4: 'Как же так полковник Сапогов!? Почему вы пропили казенную лошадь?',
    5: 'О чем вы говорите генерал? У нас самолет под заливку!! СПЗ!!!!',
    6: 'Никому невдомек, что страус был лицом нашей сборной по футболу! Аминь...'
}

# Функция генерирующая случайное число в диапазоне от 1 до длины словаря jokes
def random_joke() -> int:
    return random.randint(1, len(jokes))

# Этот хэндлер будет срабатывать на команду /start и /joke
@dp.message(Command(commands=['start', 'joke']))
async def process_start_command(message: Message):
    keyboard: list[list[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text='Хочу еще!', callback_data='more')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer(
        text=jokes[random_joke()],
        reply_markup=markup
    )

# Этот хэндлер будет срабатывать на нажатие кнопки "Хочу еще!"

@dp.callback_query(F.data == 'more')
async def process_more_press(callback: CallbackQuery):
    keyboard: list[list[InlineKeyboardButton]] = [[
        InlineKeyboardButton(text='Давай еще!!!', callback_data='more')
    ]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    # Редактируем сообщение
    
    await callback.message.edit_text(
        text=jokes[random_joke()],
        reply_markup=markup
    )

# Этот хэндлер будет срабатывать на любые сообщения, кроме команд
@dp.message()
async def send_echo(message: Message):
    await message.answer(
        text='Не понимаю, о чем ты!?\n\n'
             'Отправь команду /joke, чтобы получить шутку'
    )


if __name__ == '__main__':
    dp.run_polling(bot)