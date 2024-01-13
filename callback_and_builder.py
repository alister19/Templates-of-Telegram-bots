from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

BOT_TOKEN = 'YOUR TOKEN'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Фабрика коллбэков
class GoodsCallbackFactory(CallbackData, prefix='goods', sep=' | '):
    category_id: int
    subcategory_id: int
    item_id: int

# Инициализируем билдер инлайн-кнопок
builder = InlineKeyboardBuilder()

# Добавляем первую кнопку в билдер
builder.button(
    text='Категория 1',
    callback_data=GoodsCallbackFactory(
        category_id=1,
        subcategory_id=0,
        item_id=0
    )
)

# Добавляем вторую кнопку в билдер
builder.button(
    text='Категория 2',
    callback_data=GoodsCallbackFactory(
        category_id=2,
        subcategory_id=0,
        item_id=0
    )
)

# Сообщаем билдеру схему размещения
builder.adjust(1)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Клавиатура, ага!',
        reply_markup=builder.as_markup()
    )


if __name__ == '__main__':
    dp.run_polling(bot)