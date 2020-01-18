"""Модуль, где генерируются тестовые данные."""
from random import choice, randint
from string import ascii_letters, digits, punctuation


class DataStore:
    """Класс, в котором хранятся и генерируются тестовые данные."""

    MIN_COUNT_IN_STRUCT = 0
    MAX_COUNT_IN_STRUCT = 20
    MIN_COUNT_ITEMS = 1
    MAX_COUNT_ITEMS = 50

    @property
    def input_dict(self):
        """Генерирует список со случайно заполненными словарями."""
        keys_letters = self._hash_values()
        values_letters = self._values()

        return [
            {
                choice(keys_letters): choice(values_letters)
                for _ in self._range_count_in_struct()
            } for _ in self._range_count_items()
        ]

    @property
    def input_item(self):
        """Генерирует список кортежей с двумя элементами."""
        keys = self._hash_values()
        values = self._values()

        return [
            (choice(keys), choice(values)) for _ in self._range_count_items()
        ]

    @property
    def input_list(self):
        """Генерирует список со случайно заполненными списками."""
        letters = self._values()

        return [
            [
                choice(letters) for _ in self._range_count_in_struct()
            ] for _ in self._range_count_items()
        ]

    @property
    def input_set(self):
        """Генерирует список со случайно заполненными множествами."""
        letters = self._hash_values()

        return [
            {
                choice(letters) for _ in self._range_count_in_struct()
            } for _ in self._range_count_items()
        ]

    @property
    def input_string(self):
        """Генерирует список случайных строк."""
        return self._lst_random_string()

    @property
    def input_str_value(self):
        """Генерирует список случайных строк."""
        return self._lst_random_string()

    @property
    def input_hash_value(self):
        """Генерирует список со случайными hashable значениями."""
        values = self._hash_values()

        return [choice(values) for _ in self._range_count_items()]

    @property
    def input_value(self):
        """Генерирует список со случайными значениями."""
        values = self._values()

        return [choice(values) for _ in self._range_count_items()]

    def _lst_random_string(self, with_punctuation=False):
        """
        Генерирует список случайных строк.

        :params with_punctuation: Возвращаемая строка может содержать символы
            пунктуации.
        :return: Список случайных строк
        """
        letters = (
            self._letters()
            if with_punctuation else self._letters_wout_punctuation()
        )

        return [
            ''.join([
                choice(letters) for _ in self._range_count_in_struct()
            ]) for _ in self._range_count_items()
        ]

    def _range_count_items(self):
        """Генератор количества структур данных."""
        return range(randint(self.MIN_COUNT_ITEMS, self.MAX_COUNT_ITEMS))

    def _range_count_in_struct(self):
        """Генератор количества элементов внутри структуры данных."""
        return range(
            randint(self.MIN_COUNT_IN_STRUCT, self.MAX_COUNT_IN_STRUCT))

    def _values(self):
        """Возвращает список с hashable значениями и не только."""
        hash_values = self._hash_values()

        return hash_values + [
            [], {}, set(), [1, 2, 3, 3], {1: 2, 3: 4}, set([1, 2, 3, 4, 5])]

    def _hash_values(self):
        """Возвращает список с hashable значениями."""
        return (
                list(self._letters())
                + ['', None, (1, 2)]
                + list(map(int, digits))
        )

    def _letters(self):
        """Строка с различными символами."""
        return self._letters_wout_punctuation() + punctuation

    @staticmethod
    def _letters_wout_punctuation():
        """Строка с символами, без символов пунктуации."""
        return ascii_letters + digits
