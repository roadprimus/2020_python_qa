"""Описание абстрактного класса Figure."""
from abc import ABC, abstractmethod, abstractproperty, abstractstaticmethod


ADDED_OBJ_MUST_BE_A_FIGURE = "Добавляемый объект должен быть фигурой."
ANGLES_NOT_CHANGEABLE = "Нельзя переопределять количесво углов у фигуры."
COUNT_OF_ANGLES_MUST_BE_GTE_0 = "Количество углов должно быть >= 0."
COUNT_OF_ANGLES_MUST_BE_INTEGER = "Количество углов должно быть целым числом."
NAME_MUST_BE_STR = "Название фигуры должно быть строкой."


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
            raise TypeError(ADDED_OBJ_MUST_BE_A_FIGURE)

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
            raise TypeError(ANGLES_NOT_CHANGEABLE)
        elif isinstance(angles, int):
            if angles >= 0:
                self._angles = angles
            else:
                raise ValueError(COUNT_OF_ANGLES_MUST_BE_GTE_0)
        else:
            raise TypeError(COUNT_OF_ANGLES_MUST_BE_INTEGER)

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
            raise TypeError(NAME_MUST_BE_STR)
