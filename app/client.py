from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

import app.keyboard as kb
from converter import excel_sql


client = Router()


@client.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать! 👋'
                         '\n\nДля рассылки писем счастья нажми кнопку ниже 👇',
                         reply_markup=kb.menu)


@client.message(F.text == '✉️ Начать новую рассылку')
async def new_mail(message: Message):
    await message.answer('Загрузите файл', reply_markup=ReplyKeyboardRemove())


@client.message(F.document)
async def converter(message: Message):
    await message.answer(f'ID документа: {message.document}')

    doc = message.document.file_name
    excel_sql(doc)


@client.message()
async def other(message: Message):
    await message.answer(f'Привет {message.from_user.first_name.capitalize()}\n'
                         f'Этот бот создан для помощи в отправки рассылки долга за пользования воротами \n'
                         f'Чтобы начать рассылку нажми /start')
