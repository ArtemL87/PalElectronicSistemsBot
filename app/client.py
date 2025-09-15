from datetime import date

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

import app.keyboard as kb
from converter import excel_sql
from app.database.requests import get_users


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
    doc = message.document.file_name
    try:
        excel_sql(doc)

        users = await get_users()
        x = 0
        for user in users:
            if user[11] and user[13] < 0:
                x += 1

        await message.answer(f'Количество задолжников на {date.today()} составляет {x} квартир\n\n'
                             f'👇 Пример рассылки')

        for user in users:
            if user[11] and user[13] < 0:
                await message.answer(f'Счет: {user[1]}\n\n'
                                     f'ФИО: {user[2]}\n'
                                     f'Адрес: {user[4]}, дом {user[5]}, кв. {user[6]}\n\n'
                                     f'Тариф: {user[11]}\n'
                                     f'Баланс: {user[13]} сом\n\n'
                                     f'Необходимо оплатить до 20 числа!')
                break

    except FileNotFoundError:
        await message.answer('Файл не соответствует требованиям бота.\n'
                             'Загрузите корректный файл.')


@client.message(F.text == 'Отправить письма')
async def go(message: Message):
    users = await get_users()

    for user in users:
        if user[11] and user[13] < 0:
            await message.answer(f'Счет: {user[1]}\n\n'
                                 f'ФИО: {user[2]}\n'
                                 f'Адрес: {user[4]}, дом {user[5]}, кв. {user[6]}\n\n'
                                 f'Тариф: {user[11]}\n'
                                 f'Баланс: {user[13]} сом\n\n'
                                 f'Необходимо оплатить до 20 числа!')


@client.message()
async def other(message: Message):
    await message.delete()
    await message.answer(f'Привет {message.from_user.first_name.capitalize()}\n'
                         f'Этот бот создан для помощи в отправки напоминания об оплате за обслуживание автоворот \n'
                         f'Чтобы начать рассылку нажми /start')
