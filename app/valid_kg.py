import re

def is_valid_kg(phone: str) -> bool:
    """
    Проверка номера Кыргызстана в формате:
    996XXXXXXXXX (12 цифр: код 996 + 9 цифр)
    """
    s = re.sub(r"\D", "", phone)  # убираем все кроме цифр
    return bool(re.fullmatch(r"996\d{9}", s))
