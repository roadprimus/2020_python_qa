"""Тесты для класса Figure."""
from itertools import combinations

from .BaseTest import BaseTest
from .Circle import Circle as C
from .Rectangle import Rectangle as R, RectangleSides as RS
from .Triangle import Triangle as T, TriangleSides as TS


class TestFigure(BaseTest):
    """Общие тесты для объектов-потомков класса Figure."""

    def test_add_square(self, figure_add_square):
        """Тест получения суммы площадей двух фигур.

        - Получение списка кругов;
        - Получение списка тругольников;
        - Получение списка квадратов;
        - Получение списка прямоугольников.
        - Из вышеперечисленных объектов берутся всевозможные пары и
          проверяется возможность получения суммы площадей.

        Arg:
            figure_add_square (dict): Словарь со списками фигур.
        """
        raw_circles = figure_add_square['circle']
        raw_triangles = figure_add_square['triangle']
        raw_squares = figure_add_square['square']
        raw_rectangles = figure_add_square['rectangle']

        figures = []
        circles = [C(r, name) for r, name in raw_circles]
        figures.extend(circles)

        triangles = [T(TS(*r), name) for r, name in raw_triangles]
        figures.extend(triangles)

        squares = [R(RS(r, r), name) for r, name in raw_squares]
        figures.extend(squares)

        rectangles = [R(RS(*r), name) for r, name in raw_rectangles]
        figures.extend(rectangles)

        for fig_1, fig_2 in combinations(figures, 2):
            self.add_square_error(fig_1, fig_2)
