"""Настройки фикстур для dz5."""
import pytest

from .DataStore import store
from .settings import DOG_API_PATH as API_PATH


def pytest_addoption(parser):
    """Добавляет новый ключ при вызове pytest."""
    parser.addoption('--fn', action='store', default='', help='hlep')


def pytest_generate_tests(metafunc):
    """Pytest hook для настройки схемы параметризации фикстур."""
    data = store
    fixtures = ['api_path']
    dog_fxt = [
        'api_random_img',
        'breed_random_img',
        'by_breed',
        'by_sub_breed',
        'list_all_breeds',
    ]
    obdb_fxt = [
        'autocomplete',
        'per_page',
        'by_type',
        'get_brewery',
        'obdb_sort'
    ]
    fixtures.extend(dog_fxt)
    fixtures.extend(obdb_fxt)
    for name in fixtures:
        if name in metafunc.fixturenames:
            metafunc.parametrize(name, data[name])
