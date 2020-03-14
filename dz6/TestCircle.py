"""Тесты для класса Circle."""
import pytest

from .BaseTest import BaseTest
from .Circle import ANGLES, Circle, RADIUS_MUST_BE_GTE_0


class TestCircle(BaseTest):
    """Тесты для класса Circle."""

    c = Circle(0, '')

    def test__calc_area(self, circle__calc_area):
        """Тест вычисления площади круга.

        - Вычисяется площадь круга;
        - Полученное значение сравнивается с ожидаемым.

        Arg:
            circle__calc_area (list): Радиус и ожидаемая площадь.
        """
        r, area = circle__calc_area

        real_area = self.c._calc_area(r)

        self.check_area(area, real_area)

    def test__calc_perimeter(self, circle__calc_perimeter):
        """Тест вычисления длины круга.

        - Вычисяется длина круга;
        - Полученное значение сравнивается с ожидаемым.

        Arg:
            circle__calc_perimeter (list): Радиус и ожидаемый периметер.
        """
        r, perimeter = circle__calc_perimeter

        real_perimeter = self.c._calc_perimeter(r)

        self.check_perimeter(perimeter, real_perimeter)

    def test_creation(self, circle_creation):
        """Тест создания круга с валидными данными.

        - Создаётся круг с переданными параметрами;
        - Проверяется значение периметра;
        - Проверяется значение площади;
        - Проверяется значение количества углов;
        - Проверяется значение наименования.

        Arg:
            circle_creation (list): Радиус, периметер, площадь и наименование.
        """
        r, perimeter, area, name = circle_creation
        c = Circle(r, name)

        self.check_main_parameters((area, ANGLES, name, perimeter), c)

    def test_validate_circle(self, circle_validate_circle):
        """Тест валидации круга.

        - Проверка того, что радиус больше или равен 0;
        - Проверка, что при создании круга не некорректным радиусом
          будет сгенерирована определённая ошибка.

        Arg:
            circle_validate_circle (list): Значение радиуса и наименования.
        """
        r, name = circle_validate_circle

        assert not self.c.validate_circle(r),\
            "Проверка прошла удачно, хотя передан невалидный радиус."

        with pytest.raises(AssertionError) as e:
            Circle(r, name)

        self.check_exception_message(e, RADIUS_MUST_BE_GTE_0)

    def test_name_type_error(self, circle_name_type_error):
        """Тест того, что Наименование должно быть строкой.

        - Создаётся круг с переданными параметрами;
        - Проверяется генерация ошибки при попытке задания Наименование
          с типом не строка.

        Arg:
            circle_name_type_error (list): Радиус, наименование,
                новое наименование.
        """
        r, name, new_name = circle_name_type_error
        c = Circle(r, name)

        self.name_type_error(c, new_name)

    def test_angles_not_changable(self, circle_angles_not_changable):
        """Тест невозможности изменения количества углов.

        - Создаётся круг с переданными параметрами;
        - Проверяется генерация ошибки при смене количества углов.

        Arg:
            circle_angles_not_changable (list): Радиус, наименование,
                количество углов.
        """
        r, name, angles = circle_angles_not_changable
        c = Circle(r, name)

        self.angles_not_changable(c, angles)
