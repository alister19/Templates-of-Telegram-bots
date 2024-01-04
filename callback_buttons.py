from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram import F 
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
                          Message, CallbackQuery

BOT_TOKEN = 'YOUR TOKEN'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

big_button_1 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed'
)
big_button_2 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed'
)

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]]
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки! Нажми на любую!',
        reply_markup=keyboard
    )

# Этот хэндлер будет срабатывать на апдейт типа
# CallbackQuery с data 'big_button_1_pressed' и присылать сообщение.
@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1!':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1!',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()


# Этот хэндлер будет срабатывать на апдейт типа
# CallbackQuery с data 'big_button_2_pressed' и присылать сообщение.
@dp.callback_query(F.data == 'big_button_2_pressed')
async def big_button_2_pressed(callback: CallbackQuery):
    if callback.message.text != 'А вот и нажали БОЛЬШУЮ КНОПКУ 2':
        await callback.message.edit_text(
            text='А вот и нажали БОЛЬШУЮ КНОПКУ 2',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)