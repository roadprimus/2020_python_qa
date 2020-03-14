"""Описание класса Rectangles."""
from collections import namedtuple

from .Figure import Figure


ANGLES = 4
LENGTH_OF_SIDES_MUST_BE_GTE_0 = "Длина сторон должна быть больше или равна 0."


RectangleSides = namedtuple('RectangleSides', ('a', 'b'))


class Rectangle(Figure):
    """Класс прямоугльников."""

    def __init__(self, r, name):
        """Инициализация прямоугольника.

        Arg:
            r (RectangleSides): Стороны прямоугольника.
            name (str): Наименование круга.
        """
        assert self.validate_rectangle(r),\
            LENGTH_OF_SIDES_MUST_BE_GTE_0
        self.angles = ANGLES
        self.name = name
        self.r = r

    @property
    def area(self):
        """Метод для вычисления площади прямоугольника."""
        return self._calc_area(self.r)

    @property
    def perimeter(self):
        """Метод для вычисления периметра прямоугольника."""
        return self._calc_perimeter(self.r)

    @staticmethod
    def validate_rectangle(r):
        """Проверка существования прямоугольника.

        Arg:
            r (RectangleSides): Стороны прямоугольника.

        Returns:
            bool: Существует ли треугольник.
        """
        return r.a >= 0 and r.b > 0

    @staticmethod
    def _calc_area(r):
        """Метод для вычисления площади на основе сторон r.

        Arg:
            r (RectangleSides): Стороны прямоугольника.

        Returns:
            float: Значение площади прямоугольника.
        """
        return r.a * r.b

    @staticmethod
    def _calc_perimeter(r):
        """Метод для вычисления периметра на основе сторон r.

        Arg:
            r (RectangleSides): Стороны прямоугольника.

        Returns:
            float: Значение периметра прямоугольника.
        """
        return 2*(r.a + r.b)
