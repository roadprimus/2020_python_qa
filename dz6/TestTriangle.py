"""Тесты для класса Triangle."""
import pytest

from .BaseTest import BaseTest
from .Triangle import ANGLES, Triangle, TRIANGLE_EXIST_ERROR, TriangleSides


class TestCircle(BaseTest):
    """Тесты для класса Треугольников."""

    t = Triangle(TriangleSides(3, 4, 5), '')

    def test__calc_area(self, triangle__calc_area):
        """Тест вычисления площади треугольника.

        - Вычисяется площадь треугольника;
        - Полученное значение сравнивается с ожидаемым.

        Arg:
            triangle__calc_area (list): Три стороны треугольника, его
             полупериметр и ожидаемая площадь.
        """
        r, half_perimeter, area = triangle__calc_area
        r = TriangleSides(*r)

        real_area = self.t._calc_area(r, half_perimeter)

        self.check_area(area, real_area)

    def test__calc_perimeter(self, triangle__calc_perimeter):
        """Тест вычисления периметра треугольника.

        - Вычисяется периметр треугольника;
        - Полученное значение сравнивается с ожидаемым.

        Arg:
            triangle__calc_perimeter (list): Три стороны треугольника и
                ожидаемый периметер.
        """
        r, perimeter = triangle__calc_perimeter
        r = TriangleSides(*r)

        real_perimeter = self.t._calc_perimeter(r)

        self.check_perimeter(perimeter, real_perimeter)

    def test__calc_half_perimeter(self, triangle__calc_half_perimeter):
        """Тест вычисления полупериметра треугольника.

        - Вычисяется полупериметр треугольника;
        - Полученное значение сравнивается с ожидаемым.

        Arg:
            triangle__calc_half_perimeter (list): Периметр и ожидаемый
                полупериметер.
        """
        perimeter, half_perimeter = triangle__calc_half_perimeter

        real_half_perimeter = self.t._calc_half_perimeter(perimeter)

        self.check_half_perimeter(half_perimeter, real_half_perimeter)

    def test_creation(self, triangle_creation):
        """Тест создания треугольника с валидными данными.

        - Создаётся треугольник с переданными параметрами;
        - Проверяется значение периметра;
        - Проверяется значение полупериметра;
        - Проверяется значение площади;
        - Проверяется значение количества углов;
        - Проверяется значение наименования.

        Arg:
            triangle_creation (list): Три стороны, радиус, периметер,
                площадь, полуперметр и наименование.
        """
        r, perimeter, half_perimeter, area, name = triangle_creation
        r = TriangleSides(*r)
        t = Triangle(r, name)

        self.check_main_parameters((area, ANGLES, name, perimeter), t)
        self.check_half_perimeter(half_perimeter, t.half_perimeter)

    def test_validate_triangle(self, triangle_validate_triangle):
        """Тест валидации треугольника.

        - Проверка соотношения сторон;
        - Проверка, что при создании треугольника с некорректным сторонами
          будет сгенерирована определённая ошибка.

        Arg:
            triangle_validate_triangle (list): Три стороны и наименование
                треугольника.
        """
        r, name = triangle_validate_triangle
        r = TriangleSides(*r)

        assert not self.t.validate_triangle(r),\
            "Проверка прошла удачно, хотя переданы не валидные стороны."

        with pytest.raises(AssertionError) as e:
            Triangle(r, name)

        self.check_exception_message(e, TRIANGLE_EXIST_ERROR)

    def check_half_perimeter(self, expected, real):
        """Проверка равенства ожидаемого и реального полупериметров.

        Args:
            expected (float): Ожидаемый плупериметр.
            real (float): Полученный полупериметр.
        """
        self.check(expected, real, "Полупериметер не равен ожидаемому.")

    def test_name_type_error(self, triangle_name_type_error):
        """Тест того, что Наименование должно быть строкой.

        - Создаётся треугольник с переданными параметрами;
        - Проверяется генерация ошибки при попытке задания Наименование
          с типом не строка.

        Arg:
            triangle_name_type_error (list): Три стороны, наименование,
                новое наименование.
        """
        r, name, new_name = triangle_name_type_error
        r = TriangleSides(*r)
        t = Triangle(r, name)

        self.name_type_error(t, new_name)

    def test_angles_not_changable(self, triangle_angles_not_changable):
        """Тест невозможности изменения количества углов.

        - Создаётся треугольник с переданными параметрами;
        - Проверяется генерация ошибки при смене количества углов.

        Arg:
            triangle_angles_not_changable (list): Три стороны, наименование,
                количество углов.
        """
        r, name, angles = triangle_angles_not_changable
        r = TriangleSides(*r)
        t = Triangle(r, name)

        self.angles_not_changable(t, angles)
