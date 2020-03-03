"""Тесты для класса Square."""
from .BaseTest import BaseTest
from .Rectangle import ANGLES
from .Square import Square


class TestSquare(BaseTest):
    """Тесты для класса Square."""

    def test_creation(self, square_creation):
        """Тест создания квадрата с валидными данными.

        - Создаётся квадрат с переданными параметрами;
        - Проверяется значение периметра;
        - Проверяется значение площади;
        - Проверяется значение количества углов;
        - Проверяется значение наименования.

        Arg:
            square_creation (list): Сторона квадрата, периметер,
                 площадь и наименование.
        """
        r, perimeter, area, name = square_creation
        s = Square(r, name)

        self.check_main_parameters((area, ANGLES, name, perimeter), s)
