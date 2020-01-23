"""Настройки фикстур для dz4."""
import os.path
import sys

import pytest


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def pytest_generate_tests(metafunc):
    """Pytest hook для настройки схемы параметризации фикстур."""
    if 'input_item' in metafunc.fixturenames:
        metafunc.parametrize(
            'input_item', [
                (
                    [{}, {'A': 1, 'B': 2}, {'C': 3}],
                    [{}, {'a': 1, 'b': 2}, {'c': 3}]
                ),
                (
                    [],
                    []
                )
            ]
        )

    if 'input_books_users' in metafunc.fixturenames:
        metafunc.parametrize(
            'input_books_users', [
                (
                    (
                        [
                            {
                                'name': 'name',
                                'gender': 'gender',
                                'addres': 'addres'
                            }
                        ],
                        [
                            {
                                'title': 'title',
                                'author': 'author',
                                'height': 'height'
                            }
                        ],
                        [
                            {
                                'name': 'name',
                                'gender': 'gender',
                                'addres': 'addres',
                                'books': [
                                    {
                                        'title': 'title',
                                        'author': 'author',
                                        'height': 'height'
                                    }
                                ]
                            }
                        ]
                    )
                )
            ]
        )
    if 'input_json' in metafunc.fixturenames:
        metafunc.parametrize(
            'input_json',
            [
                [{}],
                [{"1": 1}]
            ]
        )
