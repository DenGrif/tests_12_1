from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = 'Ключи'

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

dp.middleware.setup(LoggingMiddleware())

# Клавиатура с кнопками "Информация" и "Купить"
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
keyboard.add(button_info, button_buy)

# Inline клавиатура с продуктами для покупки
inline_buy_keyboard = InlineKeyboardMarkup(row_width=2)
products = [
    ("Небольшая игра", "Lgame.jpg"),
    ("Средняя игра", "Mgame.jpg"),
    ("Большая игра", "XLgame.jpg"),
    ("Очень большая игра", "XXLgame.jpg")
]

for product_name, _ in products:
    inline_buy_keyboard.add(InlineKeyboardButton(product_name, callback_data=product_name))

# Клавиатура с кнопкой "Назад"
inline_back_keyboard = InlineKeyboardMarkup(row_width=1)
back_button = InlineKeyboardButton('Назад', callback_data='back')
inline_back_keyboard.add(back_button)


# Команда /start, отправка клавиатуры
@dp.message_handler(commands=['start'])
async def start(message: Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = f"{first_name} {last_name}" if last_name else first_name
    await message.reply(
        f"Добро пожаловать, {full_name}! 😉\n Посмотрите информацию о наших играх, кнопка: 'Информация', выбирайте - кнопка: 'Купить'",
        reply_markup=keyboard  # добавляем клавиатуру
    )


# Хэндлер для кнопки "Купить"
@dp.message_handler(Text(equals='Купить', ignore_case=True))
async def get_buying_list(message: Message):
    # Показываем Inline-клавиатуру с продуктами без описания
    await message.reply("Выберите продукт для покупки:", reply_markup=inline_buy_keyboard)


# Callback хэндлер для покупки продуктов и вывода изображений
@dp.callback_query_handler(lambda call: call.data in [product[0] for product in products])
async def send_product_image(call: CallbackQuery):
    # Получаем соответствующую картинку
    for product_name, image_file in products:
        if call.data == product_name:
            with open(image_file, 'rb') as photo:
                await call.message.reply_photo(photo)
            break

    # Отправляем подтверждение покупки
    await call.message.reply(f"Вы выбрали {call.data}. Отличный выбор! 😉")

    # Добавляем кнопку "Назад"
    await call.message.reply("Вернуться назад к выбору продуктов:", reply_markup=inline_back_keyboard)
    await call.answer()  # Закрываем кнопку


# Callback хэндлер для кнопки "Назад"
@dp.callback_query_handler(lambda call: call.data == 'back')
async def go_back(call: CallbackQuery):
    # Возвращаем пользователя к выбору продуктов
    await call.message.edit_text("Выберите продукт для покупки:", reply_markup=inline_buy_keyboard)
    await call.answer()  # Закрываем кнопку


# Хэндлер для кнопки "Информация"
@dp.message_handler(Text(equals='Информация', ignore_case=True))
async def send_info(message: Message):
    info_text = (
        "Мы продаём лучшие игры уже 2000 лет, но вы нам не поверите, поэтому скажем, что два дня"
    )
    await message.reply(info_text)

    # Отправка картинки About.jpg
    with open('About.jpg', 'rb') as photo:
        await message.reply_photo(photo)


# Хэндлер для любого другого текста
@dp.message_handler()
async def handle_any_text(message: Message):
    await send_info(message)


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
