"""Тесты для модуля main_module.py."""
from json import load
import os

import pytest

from . import main_module as mm
from . import settings


def test_read_books():
    """
    Тест функции чтения файла с информацией о книгах.

    - Проверяется выпадение исключения DZ4Exception, если указать
      некорректный путь к файлу;
    - Проверяется структура полученных данных:
        - Список;
        - Внутри списка словари.
    """
    with pytest.raises(mm.DZ4Exception) as e:
        mm.read_books('')
    assert e.typename == 'DZ4Exception',\
        'Файл был прочтён, хотя путь указан некорректно.'

    source = settings.PATH_TO_BOOKS_CSV
    books = mm.read_books(source)
    assert isinstance(books, list),\
        'Результат прочтения файла не список.'

    assert all([isinstance(book, dict) for book in books]),\
        'Информация хотя бы об одной из книг хранится не в словаре.'


def test_filter_books_data():
    """
    Тест фильтрации информации о книгах.

    - Пролучаю данные о книгах;
    - Провожу фильтрацию информации о книгах;
    - Проверяю полученную информацию для кажой книги:
        - Длина информации о книге должна быть равна 3;
        - Все 3 ключа информации о книге должны быть из кортежа book_fields.
    """
    source = settings.PATH_TO_BOOKS_CSV
    books = mm.read_books(source)
    books = mm.filter_books_data(books)

    fields = mm.book_fields
    for book in books:
        assert len(book) == 3,\
            'Количесво информации о книге не равно 3.'

        assert all([field in book for field in fields]),\
            'Не все необходимые поля есть в информации о книге.'


def test_books_keys_to_lower_case(input_item):
    """
    Тест приведения ключей словаря к ниженму регистру.

    - Применяю тестируемую функцию к исходному словарю;
    - Сравниваю полученный словарь с ожидаемым.

    :input_item: Пара значений: Исходный и ожидаемый словари.
    """
    input_dict, result_dict = input_item
    assert mm.books_keys_to_lower_case(input_dict) == result_dict,\
        'Полученный словарь не равен ожидаемому'


def test_read_users():
    """
    Тест функции чтения файла с информацией о пользователях.

    - Проверяется выпадение исключения DZ4Exception, если указать
      некорректный путь к файлу;
    - Проверяется структура полученных данных:
        - Список;
        - Внутри списка словари.
    """
    with pytest.raises(mm.DZ4Exception) as e:
        mm.read_users('')
    assert e.typename == 'DZ4Exception',\
        'Файл был прочтён, хотя путь указан некорректно.'

    source = settings.PATH_TO_USERS_JSON
    users = mm.read_users(source)
    assert isinstance(users, list),\
        'Результат прочтения файла не список.'

    assert all([isinstance(user, dict) for user in users]),\
        'Информация хотя бы об одном из пользователей хранится не в словаре.'


def test_filter_users_data():
    """
    Тест фильтрации информации о пользователях.

    - Пролучаю данные о пользователях;
    - Провожу фильтрацию информации о пользователях;
    - Проверяю полученную информацию для каждого пользователя:
        - Длина информации о пользователе должна быть равна ;
        - Все 3 ключа информации о пользователе должны быть из кортежа
          user_fields.
    """
    source = settings.PATH_TO_USERS_JSON
    users = mm.read_users(source)
    users = mm.filter_users_data(users)

    fields = mm.user_fields
    for user in users:
        assert len(user) == 3,\
            'Количесво информации о книге не равно 3.'

        assert all([field in user for field in fields]),\
            'Не все необходимые поля есть в информации о книге.'


def test_distribute_books_by_users(input_books_users):
    """
    Тестирует распределение книг по пользователям.

    - Извлекаю данные о пользователях, книгах и ожидаемом результате;
    - Получаю результат работы функции распределения книг по пользователям;
    - Проверяю соответствие ожидаемого и полученного результатов.

    :param input_books_users: Тестовая информация о пользователях, книгах и
        ожидаемом результате.
    """
    users, books, expect = input_books_users
    result = mm.distribute_books_by_users(users, books, True)

    assert expect == result,\
        'Полученный результа не равен ожидаемому'


def test_save_books_by_users(input_json):
    """
    Тестирует сохранение данных в файл.

    - Проверяется выпадение исключения FileNotFoundError, если указать
      некорректный путь к файлу;
    - Сохраняю тестовые данные в тестовый файл;
    - Читаю тестовый файл;
    - Проверяю равенство прочтённого результата и  исходных тестовых данных.

    :param input_json: Исходные тестовые данные для сохранения в json-файл.
    """
    with pytest.raises(FileNotFoundError) as e:
        mm.save_books_by_users(input_json, '')
    assert e.type == FileNotFoundError,\
        'Файл был прочтён, хотя путь указан некорректно.'

    save_path = settings.PATH_TO_RESULT_TEST
    mm.save_books_by_users(input_json, save_path)

    with open(save_path, 'r') as f:
        data = load(f)

    assert data == input_json,\
        'Данные сохраняются в файл неккоректно.'

    if os.path.exists(save_path):
        os.remove(save_path)
