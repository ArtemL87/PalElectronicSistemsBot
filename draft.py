import re

def is_valid_ru(phone: str) -> bool:
    """
    Принимает строки вроде:
    +7 912 345-67-89, 8(912)3456789, 89123456789, 9123456789
    """
    s = re.sub(r"[ \-\(\)]", "", phone)  # убрать пробелы, дефисы, скобки
    # допустимые варианты: +996XXXXXXXXXX, 0XXXXXXXXXX, XXXXXXXXXX (9 цифр)
    return bool(re.fullmatch(r"(?:\+996|0)?\d{9}", s))

# Примеры
for p in ["+996 559 09-06-87", "0(912)345678", "912345678", "+996912345678"]:
    print(p, is_valid_ru(p))
