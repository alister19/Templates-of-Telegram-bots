from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message 

# Здесь вставляем токен бота
BOT_TOKEN = 'YOUR_TOKEN_BOT'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer("Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь?")

# Этот хэндлер будет срабатывать на команду "/help"
async def prrocess_help_command(message: Message):
    await message.answer("Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение")

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    # Выведет в терминал json запись об апдейте.
    print(message.model_dump_json(indent=4, exclude_none=True))
    try:
        await message.send_copy(chat_id=message.chat.id)    # send_copy вбирает в себя все апдейты(audio, text, sticker)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается'
            'методом send_copy.'
        )

# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(prrocess_help_command, Command(commands='help'))
dp.message.register(send_echo)

if __name__ == "__main__":
    dp.run_polling(bot)