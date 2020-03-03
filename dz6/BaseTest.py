"""Тесты для класса Triangle."""
import pytest

from .Figure import ANGLES_NOT_CHANGEABLE, NAME_MUST_BE_STR


class BaseTest:
    """Тесты для класса Треугольников."""

    def name_type_error(self, obj, name):
        """Проверка генерации ошибки, при установке невалидного наименования.

            - Установка невалидного наименования;
            - Проверка возвращаемого текста ошибки.

        Arg:
            obj (Figure): Объект фигуры.
            name: Невалидное наименование.
        """
        with pytest.raises(TypeError) as e:
            obj.name = name

        self.check_exception_message(e, NAME_MUST_BE_STR)

    def angles_not_changable(self, obj, angles):
        """Проверка генерации ошибки, при изменении количества углов.

            - Установка нового значения количества углов.
            - Проверка возвращаемого текста ошибки.

        Arg:
            obj (Figure): Объект фигуры.
            angles (int): Новое количество углов.
        """
        with pytest.raises(TypeError) as e:
            obj.angles = angles

        self.check_exception_message(e, ANGLES_NOT_CHANGEABLE)

    def check_angles(self, expected, real):
        """Проверка равенства ожидаемого и полученного количества углов.

        Args:
            expected (float): Ожидаемое количество углов.
            real (float): Полученное количество углов.
        """
        self.check(expected, real, "Количество углов не равно ожидаемому")

    def check_area(self, expected, real):
        """Проверка равенства ожидаемой и полученной площадей.

        Args:
            expected (float): Ожидаемая площадь.
            real (float): Полученная площадь.
        """
        self.check(expected, real, "Площадь не равна ожидаемой.")

    def check_exception_message(self, exception, message):
        """Проверка равенства ожидаемого и полученного текста ошибки.

        Args:
            expected: Информация о сгенерированной ошибки.
            message (str): Текст ожидаемой ошибки.
        """
        expected = message
        real = exception.value.args[0]
        self.check(expected, real, "Ошибка не соответствует ожидаемой.")

    def check_main_parameters(self, expected, obj):
        """Проверка равенства основыных параметров.

        Проверяются следующие параметры:
            - площадь;
            - количество углов;
            - наименование;
            - периметр.

        Args:
            expected: Информация о сгенерированной ошибки.
            message (str): Текст ожидаемой ошибки.
        """
        area, angles, name, perimeter = expected

        self.check_area(area, obj.area)
        self.check_angles(angles, obj.angles)
        self.check_name(name, obj.name)
        self.check_perimeter(perimeter, obj.perimeter)

    def check_name(self, expected, real):
        """Проверка равенства ожидаемого и полученного наименования.

        Args:
            expected (float): Ожидаемое наименование.
            real (float): Полученное наименование.
        """
        self.check(expected, real, "Наименование не равно ожидаемому.")

    def check_perimeter(self, expected, real):
        """Проверка равенства ожидаемого и полученного периметров.

        Args:
            expected (float): Ожидаемый периметр.
            real (float): Полученный периметр.
        """
        self.check(expected, real, "Периметр не равен ожидаемому.")

    @staticmethod
    def add_square_error(fig_1, fig_2):
        """Проверка вычисления суммы площадей двух фигур.

            - У фигуры 1 запрашивается метод add_square с фигурой 2,
              как аргумент;
            - Если произошла ошибка, то срабатывает ассерт.

        Arg:
            fig_1 (Figure): Фигура 1.
            fig_2 (Figure): Фигура 2.
        """
        try:
            fig_1.add_square(fig_2)
        except Exception:
            assert False,\
                f"Ошибка вычисления суммы площадей {fig_1} и {fig_2}."

    @staticmethod
    def check(expected, real, error_message):
        """Проверка равенства ожидаемого и полученного значений.

        Args:
            expected (float): Ожидаемое значение.
            real (float): Полученное значение.

        Raises:
            AssertionError: Ошибка, если ожидаемое значение не равно
                полученному. Отображается ошибка error_message.
        """
        assert expected == real, error_message
