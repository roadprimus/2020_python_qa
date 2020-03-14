"""Описание класса Triangle."""
from collections import namedtuple
from math import sqrt

from .Figure import Figure


TriangleSides = namedtuple('TriangleSides', ('a', 'b', 'c'))


ANGLES = 3
TRIANGLE_EXIST_ERROR = 'Треугольника с такими сторонами не существует.'


class Triangle(Figure):
    """Класс треугольников."""

    def __init__(self, r, name):
        """Инициализация треугольника.

        Arg:
            r (TriangleSides): Стороны треугольника.
            name (str): Наименование треугольника.

        Raises:
            AssertionError: Если указанные стороны не образуют треугольник.
        """
        assert self.validate_triangle(r), TRIANGLE_EXIST_ERROR
        self.angles = ANGLES
        self.name = name
        self.r = r

    @property
    def area(self):
        """Метод для вычисления площади треугольника."""
        return self._calc_area(self.r, self.half_perimeter)

    @property
    def half_perimeter(self):
        """Метод для вычисления полупериметра треугольника."""
        perimeter = self.perimeter
        return self._calc_half_perimeter(perimeter)

    @property
    def perimeter(self):
        """Метод для вычисления периметра треугольника."""
        return self._calc_perimeter(self.r)

    @staticmethod
    def validate_triangle(r):
        """Проверка существования треугольника.

        Arg:
            r (TriangleSides): Стороны треугольника.

        Returns:
            bool: Существует ли треугольник.
        """
        return r.a + r.b > r.c and r.c + r.b > r.a and r.a + r.c > r.b

    @staticmethod
    def _calc_area(r, p):
        """Метод для вычисления площади на основе сторон r.

        Arg:
            r (TriangleSides): Стороны треугольника.
            p (float): Полупериметер треугольника.

        Returns:
            float: Значение площади треугольника.
        """
        return sqrt(p*(p - r.a)*(p - r.b)*(p - r.c))

    @staticmethod
    def _calc_half_perimeter(perimeter):
        """Метод для вычисления полупериметра.

        Arg:
            perimeter (float): Периметер треугольника.

        Returns:
            float: Значение полупериметра треугольника.
        """
        return perimeter / 2

    @staticmethod
    def _calc_perimeter(r):
        """Метод для вычисления периметра на основе сторон r.

        Arg:
            r (TriangleSides): Стороны треугольника.

        Returns:
            float: Значение периметра треугольника.
        """
        return r.a + r.b + r.c
