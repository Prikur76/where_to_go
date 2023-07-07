import re


def get_short_title(title):
    """Возвращает короткое название экскурсии"""
    pattern = r'«(([А-ЯЁа-яёA-Za-z0-9\s.-]+))»'
    return re.search(pattern, title)[1]