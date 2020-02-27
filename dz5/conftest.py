"""Настройки фикстур для dz5."""
import pytest

from .DataStore import store, UrlCode
from .settings import DOG_API_PATH as API_PATH


def pytest_addoption(parser):
    """Добавляет новый ключ при вызове pytest."""
    parser.addoption(
        '--url', action='store', default='https://ya.ru', help='URL')
    parser.addoption(
        '--status_code', action='store', default='200', help='Status code')


@pytest.fixture
def url_code(request):
    """
    Фикстура для проверки статуса ответа от сайта.

    - Из коммандной строки берётся значение url;
    - Из коммандной строки берётся значение кода ожидаемого ответа;
        - Код приводится к целому числу;
        - Если введён некорректный код, то устанавливается код равный 200.
    - Формируется значение фикстуры.

    :param rquest: rquest-объект из pytest.
    :return: UrlCode, с информацией о сайте и ожидаемом коде ответа.
    """
    url = request.config.getoption('--url')
    try:
        status_code = int(request.config.getoption('--status_code'))
    except ValueError:
        status_code = 200

    return UrlCode(url, status_code)


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
    json_ph_fxt = [
        'posts',
        'comments',
        'posts_by_user_id',
        'comments_by_post_id',
        'users'
    ]
    fixtures.extend(dog_fxt)
    fixtures.extend(obdb_fxt)
    fixtures.extend(json_ph_fxt)
    for name in fixtures:
        if name in metafunc.fixturenames:
            metafunc.parametrize(name, data[name])
