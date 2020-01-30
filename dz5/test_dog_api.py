"""Модуль для тестирования dog.ceo API."""
from functools import lru_cache

import requests

from .BaseTestAPI import BaseTestAPI
from .settings import DOG_API_LIST_ALL_BREEDS


class TestDogAPI(BaseTestAPI):
    """Тесты для API сервиса dog.ceo."""

    def test_random_img(self, api_random_img):
        """
        Тест получения случайного изображения.

        - Делаю запрос на получение изображения;
        - Проверяю корректность полученного ответа;
        - Получаю изображение, делая запрос на основе результата из
          предыдущего запроса;
        - Проверяю по Content-Type, что пришло изображение.

        :param api_random_img: Фикстура для запроса случайного изображения.
            Словарь, содержащий
                url - путь для запроса,
                schema - json-схема, ожидая в полученном ответе.
        """
        r = self.get_and_validate_responce(api_random_img)
        r_json = r.json()

        r_img = requests.get(r_json['message'])
        content_type = r_img.headers['Content-Type']
        assert content_type.startswith('image'),\
            'Вместо изображения получено другое содержимое.'

    def test_list_all_breeds(self, list_all_breeds):
        """
        Тест получения списка всех пород собак.

        - Делаю запрос на получение всех пород собак;
        - Проверяю корректность вернувшегося ответа.

        :param list_all_breeds: Фикстура для запроса получения списка всех
            пород собак. Словарь, содержащий
                url - путь для запроса,
                schema - json-схема, ожидая в полученном ответе.
        """
        self.get_and_validate_responce(list_all_breeds)

    def test_breed_random_img(self, breed_random_img):
        """
        Тест функции получения случайного изображения для выбранной породы.

        - Делаю запрос на получение случайного изображений для выбранной
          породы собак;
        - Проверяю корректность полученного ответа;
        - Проверяю наличие выбранной породы в полученном путя до изобаржений.

        :breed_ranfom_img: Фикстура для запроса получения случайного
            изображения для выбранной породы собак.
            Словарь, содержащий:
               breed - порода собак;
               fxt - Словарь с заросом и ожидаемой схемой json:
                   url - Путь запроса,
                   schema - json-схема, ожидая в полученном ответе.
        """
        r = self.get_and_validate_responce(breed_random_img['fxt'])
        breed_img = r.json()['message']
        breed = breed_random_img['breed']

        assert breed_img.find(breed) != -1,\
            'В полученном пути нет наименования выбранной породы.'

    def test_by_breed(self, by_breed):
        """
        Тест функции получения списка изображений для выбранной породы собак.

        - Делаю запрос на получение списка изображений для выбранной породы
          собак;
        - Проверяю корректность полученного ответа;
        - Проверяю наличие выбранной породы во всех полученных путя до
          изобаржений.

        :by_breed: Фикстура для запроса получения списка изображений
             для выбранной породы собак.
             Словарь, содержащий:
                breed - порода собак;
                fxt - Словарь с заросом и ожидаемой схемой json:
                    url - путь запроса,
                    schema - json-схема, ожидая в полученном ответе.
        """
        r = self.get_and_validate_responce(by_breed['fxt'])
        list_breed_img = r.json()['message']
        breed = by_breed['breed']

        assert all(
            [breed_img.find(breed) != -1 for breed_img in list_breed_img]
        ), 'Есть путь в котором нет наименования выбранной породы.'

    def test_by_sub_breed(self, by_sub_breed):
        """
        Тест функции получения подгрупп пород собак.

        - Делаю запрос на получение определённой подгруппы пород собак;
        - Проверяю корректность полученного ответа;
        - Получаю список всех пород и подгрупп пород собак;
        - Сравниваю занчения по выбранной подгруппе пород собак из двух
          источников.

        :by_sub_breed: Фикстура для запроса получения подгрупп пород собак.
             Словарь, содержащий:
                sub_breed - название подгруппы пород;
                fxt - Словарь с заросом и ожидаемой схемой json:
                    url - путь для запроса,
                    schema - json-схема, ожидая в полученном ответе.
        """
        r_by_sub_breed = self.get_and_validate_responce(by_sub_breed['fxt'])
        sub_breed = r_by_sub_breed.json()['message']

        all_breeds = self._all_breeds()
        sub_breed_from_all = all_breeds.get(by_sub_breed['sub_breed'])

        assert sub_breed_from_all == sub_breed,\
            'Списки подгрупп собак не совпадает.'

    @staticmethod
    @lru_cache(maxsize=8)
    def _all_breeds():
        """
        Получает словарь всех пород собак.

        Т.к. вызов метода подразумевает запрос на сервер, и аргументы вызова
        метода не меняются, реализовано кеширование результа работы метода.
        :return: Словарь всех пород собак.
        """
        return requests.get(DOG_API_LIST_ALL_BREEDS).json()['message']
