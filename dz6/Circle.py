"""Описание класса Circle."""
from math import pi

from Figure import Figure


class Circle(Figure):
    """Класс кругов."""

    def __init__(self, r, name):
        """Инициализация круга.

        Arg:
            r (float): Радиус круга.
            name (str): Наименование круга.
        """
        self.angles = 0
        self.name = name
        self.r = r

    @property
    def area(self):
        """Метод для вычисления площади круга."""
        return self._calc_area(self.r)

    @property
    def perimeter(self):
        """Метод для вычисления периметра круга."""
        return self._calc_perimeter(self.r)

    @staticmethod
    def _calc_area(r):
        """Метод для вычисления площади на основе радиуса r.

        Arg:
            r (float): Радиус круга.

        Returns:$
            float: Значение площади круга.
        """
        return pi * r**2

    @staticmethod
    def _calc_perimeter(r):
        """Метод для вычисления периметра на основе радиуса r.

        Arg:
            r (float): Радиус круга.

        Returns:
            float: Значение периметра круга.
        """
        return 2 * pi * r
