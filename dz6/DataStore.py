"""Модуль для формирования данных для тестов."""
import json


def get_data():
    """Получает данные для тестов."""
    with open('DataStore.json', 'r') as f:
        data = json.load(f)

    return data
