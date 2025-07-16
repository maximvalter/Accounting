# application/rainbow.py
from rich.text import Text

def rainbow_text(text: str) -> Text:
    """
    Функция позволяет раскрасить каждый символ строки в цвета радуги.
    Параметры:
    text: Входная строка, каждый символ которой будет окрашен
    Возвращает:
    Text: Объект rich.text.Text с применёнными радужными цветами к символам
    """
    rainbow_colors = ["red", "orange1", "yellow1", "green", "cyan", "blue", "magenta"]
    rainbow = Text()
    for i, char in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        rainbow.append(char, style=color)
    return rainbow
