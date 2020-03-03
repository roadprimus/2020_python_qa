"""Настройки фикстур для dz6."""
import re

import pytest

from .DataStore import get_data


def pytest_generate_tests(metafunc):
    """Pytest hook для настройки схемы параметризации фикстур."""
    data = get_data()
    fixtures = [
        'figure_add_square'
    ]
    circle_fxt = [
        'circle_angles_not_changable',
        'circle_creation',
        'circle_name_type_error',
        'circle_validate_circle',
        'circle__calc_area',
        'circle__calc_perimeter',
    ]
    fixtures.extend(circle_fxt)

    triangle_fxt = [
        'triangle_angles_not_changable',
        'triangle_creation',
        'triangle_name_type_error',
        'triangle_validate_triangle',
        'triangle__calc_area',
        'triangle__calc_perimeter',
        'triangle__calc_half_perimeter'
    ]
    fixtures.extend(triangle_fxt)

    rectangle_fxt = [
        'rectangle_angles_not_changable',
        'rectangle_creation',
        'rectangle_name_type_error',
        'rectangle_validate_rectangle',
        'rectangle__calc_area',
        'rectangle__calc_perimeter',
    ]
    fixtures.extend(rectangle_fxt)

    square_fxt = [
        'square_creation',
    ]
    fixtures.extend(square_fxt)
    for name in fixtures:
        obj, func = re.findall(r'^(\w+?)_(.*)$', name)[0]
        if name in metafunc.fixturenames:
            metafunc.parametrize(name, data[obj][func])
