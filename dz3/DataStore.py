"""
Модуль, где генерируются тестовые данные.
"""
from random import choice, randint
from string import ascii_letters, digits, punctuation

MIN_COUNT_ITEMS = 1
MAX_COUNT_ITEMS = 20


class DataStore:
    """
    Класс, в котором хранятся и генерируются тестовые данные.
    """
    @property
    def input_dict(self):
        """
        Генерирует список со случайно заполненными словарями.
        """
        keys_letters = self._get_hashable_values()
        values_letters = self._get_values()

        return [
            {
                choice(keys_letters): choice(values_letters) 
                for _ in range(randint(0, 10)) 
            } for _ in range(randint(MIN_COUNT_ITEMS, MAX_COUNT_ITEMS))
        ]

    @property
    def input_list(self):
        """
        Генерирует список со случайно заполненными списками.
        """
        letters = self._get_values()

        return [
            [choice(letters) for _ in range(randint(0, 20))]
            for _ in range(randint(MIN_COUNT_ITEMS, MAX_COUNT_ITEMS))
        ]

    @property
    def input_set(self):
        """
        Генерирует список со случайно заполненными множествами.
        """
        letters = self._get_hashable_values()

        return [
            {choice(letters) for _ in range(randint(0, 20))}
            for _ in range(randint(MIN_COUNT_ITEMS, MAX_COUNT_ITEMS))
        ]

    @property
    def input_value(self):
        """
        Генерирует список со случайными значениями.
        """
        values = self._get_values()

        return [
            choice(values) for _ in range(
                randint(MIN_COUNT_ITEMS, MAX_COUNT_ITEMS))
        ]

    def _get_values(self):
        """
        Возвращает список с hashable значениями и не только.
        """
        hashable_values = self._get_hashable_values()

        return hashable_values + [
            [], {}, set(), [1, 2, 3, 3], {1: 2, 3: 4}, set([1, 2, 3, 4, 5])]

    @staticmethod
    def _get_hashable_values():
        """
        Возвращает список с hashable значениями.
        """
        return list(ascii_letters + digits +  punctuation) + [None, (1, 2)]

