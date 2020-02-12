"""Модуль для тестирования openbrewerydb.org API."""
from .BaseTestAPI import BaseTestAPI
from .DataStore import PLUS


class TestOpenBreweryDB(BaseTestAPI):
    """Тесты для API сервиса openbrewerydb.org."""

    def test_autocomplete(self, autocomplete):
        """
        Тест полученных данных по autocomplete.

        - Проверяю корректность полученного ответа;

        :param autocomplete: Фикстура для запроса autocomplete.
            Словарь, содержащий
                url - путь для запроса,
                schema - json-схема, ожидая в полученном ответе.
        """
        self.get_and_validate_responce(autocomplete['fxt'])

    def test_per_page(self, per_page):
        """
        Тест полученных количество записей на странице.

        - Получаю ожидаемое количество записей;
            - Запрашивается менее 50 записей:
                - Да: Ожидается указанное количесво записей;
                - Нет: Возвращается число 50;
        - Проверяю корректность полученного ответа;
        - Получаю реальное количество записей;
        - Сравниваю ожидаемое и реальное количество записей.

        :param per_page: Фикстура для запроса per_page.
            Словарь, содержащий
               count - количество записей;
               fxt - Словарь с заросом и ожидаемой схемой json:
                   url - Путь запроса,
                   schema - json-схема, ожидая в полученном ответе.
        """
        expected_count = per_page['count'] if per_page['count'] < 50 else 50

        r = self.get_and_validate_responce(per_page['fxt'])
        real_count = len(r.json())

        assert expected_count == real_count,\
            'Ожидаемое количество записей не равно реальному.'

    def test_by_type(self, by_type):
        """
        Тест полученных количество записей на странице.

        - Формирую ожидаемое множество типов;
        - Проверяю корректность полученного ответа;
        - Получаю реальное множество типов;
        - Сравниваю ожидаемое и реальное множества типов.

        :param per_page: Фикстура для запроса by_type.
            Словарь, содержащий
               name - наименование типа;
               fxt - Словарь с заросом и ожидаемой схемой json:
                   url - Путь запроса,
                   schema - json-схема, ожидая в полученном ответе.
        """
        expected_names = set([by_type['name']])

        r = self.get_and_validate_responce(by_type['fxt'])
        real_names = set([row['brewery_type'] for row in r.json()])

        assert expected_names == real_names,\
            'Ожидаемые типы не совпадают с реальными.'

    def test_get_brewery(self, get_brewery):
        """
        Тест получения записи по иденитификатору.

        - Получаю ожидаемый идентификатор;
        - Проверяю корректность полученного ответа;
        - Получаю реальный идентификатор;
        - Сравниваю ожидаемый и реальный идентификатор.

        :param per_page: Фикстура для запроса get_brewery.
            Словарь, содержащий
               brewery_id - идентификатор;
               fxt - Словарь с заросом и ожидаемой схемой json:
                   url - Путь запроса,
                   schema - json-схема, ожидая в полученном ответе.
        """
        expected_brewery_id = get_brewery['brewery_id']
        r = self.get_and_validate_responce(get_brewery['fxt'])
        real_brewery_id = r.json().get('id')

        assert expected_brewery_id == real_brewery_id,\
            'Ожидаемый и полученный идентификаторы не совпадают.'

    def test_obdb_sort(self, obdb_sort):
        """
        Тест сортировки данных по идентификатору.

        - Получаю знак сортировки;
        - Проверяю корректность полученного ответа;
        - Получаю реальную последовательность записей;
        - Получаю ожидаемую последовательность записей.

        :param per_page: Фикстура для запроса obdb_sort.
            Словарь, содержащий
               sign - знак упорядочивания;
               fxt - Словарь с заросом и ожидаемой схемой json:
                   url - Путь запроса,
                   schema - json-схема, ожидая в полученном ответе.
        """
        sign = obdb_sort['sign']
        r = self.get_and_validate_responce(obdb_sort['fxt'])
        real_order = r.json()
        expected_order = self._sorted(sign, real_order)
        assert expected_order == real_order,\
            'Ожидаемая и полученная последовательность записей не совпадают.'

    @staticmethod
    def _sorted(sign, breweries):
        """
        Сортирует последовательность в зависимости от знака.

        :param sign: Знак сортировки. Пряма сортировка - пустая строка.
            Обратная сортировка знак "-".
        :param breweries: Последовательность записей.
        :return: Упорядоченная последовательность записей.
        """
        if sign == PLUS:
            result = sorted(breweries, key=lambda x: x['id'], reverse=False)
        else:
            result = sorted(breweries, key=lambda x: x['id'], reverse=True)

        return result
