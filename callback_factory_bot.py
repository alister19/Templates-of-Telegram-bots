"""
Использование фабрики коллбэков
"""

from aiogram import Bot, Dispatcher, F 
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (
    CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
)

BOT_TOKEN = 'YOUR_TOKEN'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создаем свой класс фабрики коллбэков, указывая префикс
# и структуру callback_data
class GoodsCallbackFactory(CallbackData, prefix='goods', sep=' | '):
    category_id: int
    subcategory_id: int
    item_id: int

# Создаем объекты кнопок, с применением фвбрики коллбэков
button_1 = InlineKeyboardButton(
    text='Категория 1',
    callback_data=GoodsCallbackFactory(
        category_id=1,
        subcategory_id=0,
        item_id=0
    ).pack()
)

button_2 = InlineKeyboardButton(
    text='Категория 2',
    callback_data=GoodsCallbackFactory(
        category_id=2,
        subcategory_id=0,
        item_id=0
    ).pack()
)

# Создаем объекты клавиатуры, добавляя в список списки с кнопками
markup = InlineKeyboardMarkup(
    inline_keyboard=[[button_1], [button_2]]
)

# Этот хэндлер будет срабатывать на команду /start
# и отправлять пользователю сообщение с клавиатурой
@dp.message(CommandStart)
async def process_start_command(message: Message):
    await message.answer(
        text='Вот такая клавиатура!',
        reply_markup=markup
    )

# Этот хэндлер будет срабатывать на нажатие любой 
# инлайн-кнопки и распечатывать апдейт в терминал
# @dp.callback_query(GoodsCallbackFactory.filter())
# async def process_category_press(
#     callback: CallbackQuery,
#     callback_data: GoodsCallbackFactory
# ):
#     print(callback.model_dump_json(indent=4, exclude_none=True))
#     await callback.message.answer(text=callback_data.pack())
#     await callback.answer()

# Если хотим поймать нажатие только на первую кнопку ("Категория 1")
# @dp.callback_query(GoodsCallbackFactory.filter|(F.category_id == 1))
# async def process_category_1(callback: CallbackQuery,
#                              callback_data: GoodsCallbackFactory):
#     await callback.message.answer(text=callback_data.pack())
#     await callback.answer()
    

# Этот хэндлер буде срабатывать на нажатие любой инлайн-кнопки
# и отправлять в чат форматированный ответ из callback_data
@dp.callback_query(GoodsCallbackFactory.filter())
async def process_category_press(callback: CallbackQuery,
                                 callback_data: GoodsCallbackFactory):
    await callback.message.answer(
        text=f'Категория товаров: {callback_data.category_id}\n'\
             f'Подкатегория товаров: {callback_data.subcategory_id}\n'\
             f'Товар: {callback_data.item_id}'
    )
    await callback.answer()




if __name__ == '__main__':
    dp.run_polling(bot)