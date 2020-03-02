"""Описание класса Rectangle."""
from Rectangle import Rectangle, RectangleSides


class Square(Rectangle):
    """Класс квадратов."""

    def __init__(self, r, name):
        """Инициализация квадрата.

        Arg:
            r (float): Сторона квадрата.
            name (str): Наименование кdflhfnf.
        """
        r = RectangleSides(r, r)
        super().__init__(r, name)
