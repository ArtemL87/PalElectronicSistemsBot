from datetime import date

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

import app.keyboard as kb
from app.converter import excel_sql
from app.valid_kg import is_valid_kg
from app.database.requests import get_users, get_phone


client = Router()


@client.callback_query(F.data == 'start')
@client.message(CommandStart())
async def cmd_start(message: Message | CallbackQuery):
    await message.answer('Добро пожаловать! 👋'
                         '\n\nДля рассылки писем счастья нажми кнопку ниже 👇',
                         reply_markup=kb.menu)


@client.message(F.text == '✉️ Начать новую рассылку')
async def new_mail(message: Message):
    await message.answer('💾 Загрузите файл', reply_markup=ReplyKeyboardRemove(), )


@client.message(F.document)
async def converter(message: Message):
    doc = message.document.file_name
    try:
        excel_sql(doc)

        users = await get_users()

        x = 0
        debt = 0
        for user in users:
            if user[11] and user[13] < 0:
                debt -= int(user[13])
                x += 1

        await message.answer(f'На {date.today()}:\n'
                             f'Количество задолжников: {x} квартир\n'
                             f'Общая сумма задолжности: {debt} сом\n\n'
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

        await message.answer('Начать рассылку писем счастья?', reply_markup=await kb.go_score())

    except FileNotFoundError:
        await message.answer('❌ Файл не соответствует требованиям бота ❌\n'
                             '💾 Загрузите корректный файл.')


@client.callback_query(F.data == 'push')
async def go(callback: CallbackQuery):
    await callback.message.answer('📲 Запущен процесс рассылки...')
    users = await get_users()
    phones = await get_phone()

    dict_phones = {}
    incorrect_number_format = []

    for phone in phones:
        if is_valid_kg(str(phone[1])):
            dict_phones[phone[0]] = f'+{phone[1]}'
        else:
            incorrect_number_format.append((phone[0], phone[1]))

    account_without_phone_number = []

    x = 0
    for user in users:
        if user[11] and user[13] < 0:
            try:
                await callback.message.answer(f'Счет: {user[1]}\n\n'
                                              f'ФИО: {user[2]}\n'
                                              f'Адрес: {user[4]}, дом {user[5]}, кв. {user[6]}\n\n'
                                              f'Тариф: {user[11]}\n'
                                              f'Баланс: {user[13]} сом\n\n'
                                              f'Номер: {dict_phones[user[1]]}\n'
                                              f'Необходимо оплатить до 20 числа!')
                x += 1
            except KeyError:
                account_without_phone_number.append(user[1])



    await callback.message.answer(f'✅ Процесс рассылки окончен\n\n'
                                  f'💬 Сообщения отправлены {x} абонентам',
                                  reply_markup=kb.menu)

    if account_without_phone_number:
        await callback.message.answer('❗️  ❗️  ❗️\n'
                                      '📵 Счета без номера телефона ⬇️')
        for score in account_without_phone_number:
            await callback.message.answer(f'{score}')

        account_without_phone_number.clear()

    if incorrect_number_format:
        await callback.message.answer('❗️  ❗️  ❗️\n'
                                      '📴 Счета с некорректными номерами ⬇️')
        for score, phone in incorrect_number_format:
            await callback.message.answer(f'{score} - {phone}')

        incorrect_number_format.clear()


@client.message()
async def other(message: Message):
    await message.delete()
    await message.answer(f'Привет {message.from_user.first_name.capitalize()}\n'
                         f'Этот бот создан для помощи в отправки напоминания об оплате за обслуживание автоворот \n'
                         f'Чтобы начать рассылку нажми /start')
