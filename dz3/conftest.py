from dz3.DataStore import DataStore
import pytest


def pytest_generate_tests(metafunc):
    ds = DataStore()
    fixtures = (
        'input_dict',
        'input_item',
        'input_list',
        'input_set',
        'input_string',
        'input_str_value',
        'input_hash_value',
        'input_value'
    )
    
    for name in fixtures:
        if name in metafunc.fixturenames:
            metafunc.parametrize(name, getattr(ds, name))


@pytest.fixture()
def list_fixture():
    """
    Тестовая фикстура.
    """
    return [1, 2, 3, 2, 4, 5]

