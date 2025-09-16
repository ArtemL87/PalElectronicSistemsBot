import re

def is_valid_kg(phone: str) -> bool:
    """
    Проверка номеров Кыргызстана:
    +996XXXXXXXXX (12 символов, код страны)
    0XXXXXXXXX (10 символов, локальный формат)
    """
    s = re.sub(r"[ \-\(\)]", "", phone)  # убираем пробелы, дефисы, скобки

    pattern = r"^(?:\+996\d{9}|0\d{9})$"
    return bool(re.fullmatch(pattern, s))
