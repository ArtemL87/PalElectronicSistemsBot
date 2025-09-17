import re

def is_valid_kg(phone: str) -> bool:
    """
    Проверка номера Кыргызстана в формате:
    996XXXXXXXXX (12 цифр: код 996 + 9 цифр)
    """
    s = re.sub(r"\D", "", phone)  # убираем все кроме цифр
    return bool(re.fullmatch(r"996\d{9}", s))


# Примеры
tests = [
    "996912345678",  # верный
    "99650123456",   # неверный (мало цифр)
    "+996912345678", # неверный (лишний +)
    "0912345678",    # неверный
    "996 700 123 456" # верный (с пробелами)
]

for t in tests:
    print(t, "->", is_valid_kg(t))

import pywhatkit as kit
from aiogram import Bot, Dispatcher, types
import asyncio

bot = Bot(token='8053033384:AAF5TRuXjJDhFsOjSwEDuxt4NE7JPL6u5Bs')
dp = Dispatcher()

WHATSAPP_NUMBER = "+996559090687"  # номер получателя


@dp.message()
async def forward_to_whatsapp(message: types.Message):
    text = 'Артем привет'

    # отправляем в WhatsApp
    # hour/minute должны быть >= текущего времени
    import datetime
    now = datetime.datetime.now()
    kit.sendwhatmsg(WHATSAPP_NUMBER, text, now.hour, now.minute + 1)

    await message.reply("Сообщение переслано в WhatsApp!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
