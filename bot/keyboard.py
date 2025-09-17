from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='✉️ Начать новую рассылку')],
    [KeyboardButton(text='📲 Контакты')]],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню ниже... ⬇️'
)


async def go_score():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='▶️ Разослать письма', callback_data='push')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='start')]
    ])
