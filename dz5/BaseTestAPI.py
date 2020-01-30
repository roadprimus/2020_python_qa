"""Модуль, содержащий базовый класс для тестов API."""
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import requests

from .settings import Pair


class BaseTestAPI:
    """Базовый класс для тесов в dz5."""

    def test_open(self, api_path):
        """
        Тест открытия сервиса.

        - Произвожу get-запрос с сервису;
        - Проверяю, чтобы статус ответа был корректным.
        """
        r = requests.get(api_path)
        assert r.ok, 'Вернулся некорректный ответ.'

    def get_and_validate_responce(self, fxt):
        """
        Получает responce и проверяет его на корректность.

        :param fxt: Фикстура, которая представляет собой словарь с ключами:
            url - путь для запроса случайного изображения,
            schema - json-схема, которую ожидаю получить в ответе от сервера.
        :return: Объект responce.
        """
        r = requests.get(fxt['url'])

        json_pair = Pair(fxt['schema'], r.json())
        self.validate_responce_correct(r, json_pair)

        return r

    def validate_responce_correct(self, responce, json_pair):
        """
        Проверяет корректность ответа от сервера.

        - Проверяет статус ответа сервера;
        - Проверяет правильность структуры полученного json.

        :param responce: Ответ от сервера.
        :param json_pair: Пара проверяемый json и ожидаемый его формат.
        """
        self.validate_responce_ok(responce)
        self.validate_json_schema(json_pair)

    @staticmethod
    def validate_json_schema(pair):
        """
        Валидация схемы json.

        :param json_pair: Пара проверяемый json и ожидаемый его формат.
        :return: True или False.
        """
        result = True
        try:
            validate(instance=pair.real, schema=pair.expected)
        except ValidationError:
            result = False

        assert result, 'Полученная json-схема не соответствует ожидаемой.'

    @staticmethod
    def validate_responce_ok(responce):
        """
        Проверка, что статус ответа подходящий.

        :param responce: Ответ от сервера.
        """
        assert responce.ok, 'Вернулся некорректный ответ.'
