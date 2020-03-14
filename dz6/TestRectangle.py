"""Тесты для класса Rectangle."""
import pytest

from .BaseTest import BaseTest
from .Rectangle import (
    ANGLES, LENGTH_OF_SIDES_MUST_BE_GTE_0, Rectangle, RectangleSides)


class TestRectangle(BaseTest):
    """Тесты для класса Rectangle."""

    t = Rectangle(RectangleSides(1, 2), '')

    def test__calc_area(self, rectangle__calc_area):
        """Тест вычисления площади прямоугольника.

        - Вычисяется площадь прямоугольника;
        - Полученное значение сравнивается с ожидаемым.

        Arg:
            rectangle__calc_area (list): Стороны прямоугольника и
                 ожидаемая площадь.
        """
        r, area = rectangle__calc_area
        r = RectangleSides(*r)

        real_area = self.t._calc_area(r)

        self.check_area(area, real_area)

    def test__calc_perimeter(self, rectangle__calc_perimeter):
        """Тест вычисления периметра прямоугольника.

        - Вычисяется периметер прямоугольника;
        - Полученное значение сравнивается с ожидаемым.

        Arg:
            rectangle__calc_perimeter (list): Стороны прямоугольника и
                ожидаемый периметер.
        """
        r, perimeter = rectangle__calc_perimeter
        r = RectangleSides(*r)

        real_perimeter = self.t._calc_perimeter(r)

        self.check_perimeter(perimeter, real_perimeter)

    def test_creation(self, rectangle_creation):
        """Тест создания прямоугольника с валидными данными.

        - Создаётся прямоугольник с переданными параметрами;
        - Проверяется значение периметра;
        - Проверяется значение площади;
        - Проверяется значение количества углов;
        - Проверяется значение наименования.

        Arg:
            rectangle_creation (list): Стороны прямоугольника, периметер,
                 площадь и наименование.
        """
        r, perimeter, area, name = rectangle_creation
        r = RectangleSides(*r)
        t = Rectangle(r, name)

        self.check_main_parameters((area, ANGLES, name, perimeter), t)

    def test_validate_rectangle(self, rectangle_validate_rectangle):
        """Тест валидации прямоугольника.

        - Проверка того, что стороны больше или равены 0;
        - Проверка, что при создании прямоугольника не некорректным радиусом
          будет сгенерирована определённая ошибка.

        Arg:
            rectangle_validate_rectangle (list): Стороны прямоугольника и
                наименование.
        """
        r, name = rectangle_validate_rectangle
        r = RectangleSides(*r)

        assert not self.t.validate_rectangle(r),\
            "Проверка прошла удачно, хотя переданы не валидные стороны."

        with pytest.raises(AssertionError) as e:
            Rectangle(r, name)

        self.check_exception_message(e, LENGTH_OF_SIDES_MUST_BE_GTE_0)

    def test_name_type_error(self, rectangle_name_type_error):
        """Тест того, что Наименование должно быть строкой.

        - Создаётся прямоугольник с переданными параметрами;
        - Проверяется генерация ошибки при попытке задания Наименование
          с типом не строка.

        Arg:
            rectangle_name_type_error (list): Стороны прямоугольника,
                наименование, новое наименование.
        """
        r, name, new_name = rectangle_name_type_error
        r = RectangleSides(*r)
        r = Rectangle(r, name)

        self.name_type_error(r, new_name)

    def test_angles_not_changable(self, rectangle_angles_not_changable):
        """Тест невозможности изменения количествяа углов.

        - Создаётся прямоугольник с переданными параметрами;
        - Проверяется генерация ошибки при смене количества углов.

        Arg:
            rectangle_angles_not_changable (list): Стороны прямоугольника,
                наименование, количество углов.
        """
        r, name, angles = rectangle_angles_not_changable
        r = RectangleSides(*r)
        r = Rectangle(r, name)

        self.angles_not_changable(r, angles)
