"""Домашнее задание №4. Чтение и запись файлов разных типов."""
from contextlib import contextmanager
from csv import DictReader
from json import dump, load
from random import randint
try:
    from . import settings
except ImportError:
    import settings


BOOKS = 'books'
book_fields = ('Title', 'Author', 'Height')
user_fields = ('name', 'gender', 'address')


class DZ4Exception(Exception):
    """Класс ошибок для пакета dz4."""

    TYPENAME = 'DZ4Exception'

    def __init__(self, error):
        """Инициализация класса."""
        self.error = error
        self.typename = self.TYPENAME


@contextmanager
def open_file(*args, **kwargs):
    """Контекстный менеджер для работы с файлом."""
    try:
        f = None
        f = open(*args, **kwargs)
        yield f
    except OSError:
        raise DZ4Exception(
            f'Произошла ошибка при работе с файлом! {args[0]}')
    finally:
        if f:
            f.close()


def read_books(source):
    """
    Читает информацию о книгах из файла source.

    :param source: Путь к файлу с информацией о книгах.
    :return: Возвращает информацию о книгах.
    """
    with open_file(source, 'r') as f:
        books = [row for row in DictReader(f)]

    return books


def filter_books_data(books):
    """
    Фильтрует информацию о книгах.

    В результирующий файл необходимо заносить только часть информации
    о книгах. Информация должна остаться по полям, указанным в кортеже
    book_fields.

    - Создаю список, в который будет помещена отфильтрованная информация
      о книгах;
    - Прохожу по всем книгам:
        - Из информации по каждой книге беру только данные по полям из
          кортежа book_fields.
        - Полученный словарь с информацией добовляю в список с отфильтрованной
          информацией о книгах.

    :param books: Инофрмация о книгах.
    :return: Отфильтрованная информация о книгах.
    """
    filtered_books = []
    for book in books:
        book_info = {}
        for field, value in book.items():
            if field in book_fields:
                book_info[field] = value
        filtered_books.append(book_info)

    return filtered_books


def books_keys_to_lower_case(books):
    """
    Преобразует ключи books к нижнему регистру.

    :param books: Информация о книгах.
    :return: Информация о книгах, ключи которой приведены к нижнему регистру.
    """
    return [{k.lower(): v for k, v in book.items()} for book in books]


def read_users(source):
    """
    Читает информацию о пользователях из файла source.

    :param source: Путь к файлу с информацией о пользователях.
    :return: Возвращает информацию о пользователях.
    """
    with open_file(source, 'r') as f:
        users = load(f)

    return users


def filter_users_data(users):
    """
    Фильтрует информацию о пользователях.

    В результирующий файл необходимо заносить только часть информации
    о пользователях.

    :param users: Инофрмация о пользователях.
    :return: Отфильтрованная информация о пользователях.
    """
    filtered_users = []
    for user in users:
        user_info = {}
        for field, value in user.items():
            if field in user_fields:
                user_info[field] = value
        filtered_users.append(user_info)

    return filtered_users


def distribute_books_by_users(users, books, one_book_for_user=False):
    """
    Распределяет книги по пользователям.

    :param users: Пользователи.
    :param books: Книги.
    :param one_book_for_user: По одной книге для одного пользователя.
    :return: Распределённые книги по пользователям.
    """
    tmp_books = books.copy()
    result = []
    for user in users:
        max_count_of_books = 1 if one_book_for_user else randint(1, 4)
        tmp = user.copy()
        tmp_books = []
        try:
            tmp_books = [books.pop() for i in range(max_count_of_books)]
        except IndexError:
            pass
        tmp[BOOKS] = tmp_books
        result.append(tmp)

    return result


def save_books_by_users(books_by_users, save_path):
    """
    Сохраняет распределение книг по пользователям.

    :param books_by_users: Распределение книг по пользователям.
    :param save_path: Путь к файлу, в который нужно сохранить информацию.
    :return:
    """
    with open(save_path, 'w') as f:
        dump(books_by_users, f, indent=4)


def main():
    """
    Основная функция модуля.

    - Получаю данные по пользователям;
    - Фильтрую данные по пользователям;
    - Получаю данные по книгам;
    - Фильтрую данные по книгам;
    - Привожу ключи в словарях, ответственных за данные по книгам, к нижнему
      регистру;
    - Распределяю книги между пользователями;
    - Сохраняю полученное распределение книг между пользователями в файл.
    """
    try:
        source_json = settings.PATH_TO_USERS_JSON
        users = read_users(source_json)
        users = filter_users_data(users)

        source_csv = settings.PATH_TO_BOOKS_CSV
        books = read_books(source_csv)
        books = filter_books_data(books)
        books = books_keys_to_lower_case(books)

        books_by_users = distribute_books_by_users(users, books)

        save_path = settings.PATH_TO_RESULT
        save_books_by_users(books_by_users, save_path)
    except DZ4Exception as e:
        print(e.error)


if __name__ == '__main__':
    main()
