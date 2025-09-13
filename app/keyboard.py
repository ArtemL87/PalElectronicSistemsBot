from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='✉️ Начать новую рассылку')],
    [KeyboardButton(text='📲 Контакты')]],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню ниже... ⬇️'
)


