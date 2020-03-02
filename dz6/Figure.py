"""Описание абстрактного класса Figure."""
from abc import ABC, abstractmethod, abstractproperty, abstractstaticmethod


class Figure(ABC):
    """Абстрактный класс фигур.

    Arg:
        ABC (abc.ABCMeta): Вспомогательный класс,
            который имеет метакласс ABCMeta.

    Arguments:
        _angles (int): Количество углов.
        _name (str): Наименовани фигуры.
    """

    _angles = None
    _name = None

    @abstractmethod
    def __init__(self, r):
        """Инициализация фигуры.

        Arg:
            r (): Параметр, характеризующий размер(ы) фигуры.
        """
        pass

    def __repr__(self):
        """Текстовое представление фигуры."""
        return f"{{{self.__class__.__name__}: {self.name}}}"

    def add_square(self, other):
        """Вычисляет сумму площадей двух фигур.

        Arg:
            other (Figure): Фигура.

        Raises:
            TypeError: Если переданый объект не является фигурой.
        """
        if not isinstance(other, Figure):
            raise TypeError("Добавляемый объект должен быть фигурой.")

        return self.area + other.area

    @abstractproperty
    def area(self):
        """Метод для вычисления площади фигуры."""
        pass

    @abstractstaticmethod
    def _calc_area(r):
        """Метод для вычисления площади на основе данных из r.

        Arg:
            r (): Параметр, характеризующий размер(ы) фигуры.
        Returns:
            (): Значение площади фигуры.
        """
        pass

    @abstractproperty
    def perimeter(self):
        """Метод для вычисления периметра фигуры."""
        pass

    @abstractstaticmethod
    def _calc_perimeter(r):
        """Метод для вычисления периметра на основе данных из r.

        Arg:
            r (): Параметр, характеризующий размер(ы) фигуры.
        Returns:
            (): Значение периметра фигуры.
        """
        pass

    @property
    def angles(self):
        """Количество углов фигуры."""
        return self._angles

    @angles.setter
    def angles(self, angles):
        """Сеттер количества углов фигуры.

        Arg:
            angles (int): Количество углов фигуры.

        Raises:
            TypeError: Если происходит переопределения количества углов.
            ValuesError: Если количество углов меньше нуля.
            TypeError: Если количество углов не целое число.
        """
        if self._angles is not None:
            raise TypeError("Нельзя переопределять количесво углов у фигуры.")
        elif isinstance(angles, int):
            if angles >= 0:
                self._angles = angles
            else:
                raise ValueError("Количество углов должно быть >= 0.")
        else:
            raise TypeError("Количество углов должно быть целым числом.")

    @property
    def name(self):
        """Название фигуры."""
        return self._name

    @name.setter
    def name(self, name):
        """Сеттер названия фигуры.

        Arg:
            name (str): Название фигуры.

        Raises:
            TypeError: Если название фигуры не строка.
        """
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("Название фигуры должно быть строкой.")
