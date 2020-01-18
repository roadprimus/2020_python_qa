"""Тесты методов Словаря."""


class TestDictMethodsWoutItemArgs:
    """
    Тесты методов словаря.

    Проверяются методы для которых не нужны дополнительные параметры, кроме
    самого словаря.
    """

    def test_clear(self, input_dict):
        """
        Тест метода clear.

        - Получаю ожидаемый словарь;
        - Провожу операцию clear;
        - Проверяю равенство ожидаемого и полученного словарей.

        :param input_dict: Исходный словарь.
        """
        expected_dict = {}

        input_dict.clear()

        assert expected_dict == input_dict,\
            'Ожидаемый и полученный списки различаются.'

    def test_values(self, input_dict):
        """
        Тест метода values.

        - Получаю ожидаемый словарь;
        - Провожу операцию values;
        - Проверяю равенство ожидаемых и полученных значений.

        :param input_dict: Исходный словарь.
        """
        expected_values = [v for k, v in input_dict.items()]

        result_values = list(input_dict.values())

        assert expected_values == result_values,\
            'Ожидаемый и полученный результат различаются.'

    def test_keys(self, input_dict):
        """
        Тест метода keys.

        - Получаю ожидаемый словарь;
        - Провожу операцию keys;
        - Проверяю равенство ожидаемых и полученных значений.

        :param input_dict: Исходный словарь.
        """
        expected_keys = [k for k, v in input_dict.items()]

        result_keys = list(input_dict.keys())

        assert expected_keys == result_keys,\
            'Ожидаемый и полученный результат различаются.'


class TestDictMethodsWithItemArgs:
    """
    Тесты методов словаря.

    Проверяются методы для которых нужны дополнительные параметры, кроме
    самого словаря.
    """

    def test_pop(self, input_dict, input_hash_value):
        """
        Тест метода pop.

        - Сохраняю начальную длину исходного словаря;
        - Получаю ожидаемый словарь и значение по удаляемому ключу в этом
          словаре;
        - Провожу операцию pop;
        - Если возникла ошибка KeyError:
            - Да:
                - Проверяю равенство длины исходного словаря и полученного;
            - Нет:
                - Проверяю равенство полученного и ожидаемого словарей.
                - Проверяю равенство полученного и ожидаемого значения,
                  которые хранились по этому ключу в полученном и ожидаемом
                  словарях.

        :param input_dict: Исходный словарь.
        :param input_hash_value: Удаляемое значение.
        """
        initial_len = len(input_dict)
        expected_dict, expected_value = (
            self._get_dict_after_pop(input_dict, input_hash_value))

        try:
            result_value = input_dict.pop(input_hash_value)
        except KeyError:
            assert len(input_dict) == initial_len,\
                'Длина словаря не должна была измениться.'
        else:
            assert input_dict == expected_dict,\
                'Полученный и ожидаемый словари не совпадают.'
            assert result_value == expected_value,\
                'Полученное и ожидаемое значение по ключу не совпадают.'

    def test_update(self, input_dict, input_item):
        """
        Тест метода update.

        - Получаю ожидаемый словарь;
        - Провожу операцию update;
        - Проверяю равенство полученного и ожидаемого словарей.

        :param input_dict: Исходный словарь.
        :param input_item: Кортеж, пара ключ-значение.
        """
        expected_dict = self._get_dict_after_update(input_dict, input_item)

        input_dict.update(dict([input_item]))

        assert input_dict == expected_dict,\
            'Полученный и ожидаемый словари не совпадают.'

    @staticmethod
    def _get_dict_after_pop(input_dict, pop_key):
        """
        Имитация стандартного метода pop в словаре.

        Возвращает исходный словарь без ключа pop_key и значение, которо было
        в исходном словаре по этому ключу.

        :param input_dict: Исходный словарь.
        :param pop_key: Удаляемый ключ.
        :return: Исходный словарь без ключа pop_key и значение, которое было
            в исходном словаре по этому ключу.
        """
        result = input_dict.copy()
        for key, value in result.items():
            if key == pop_key:
                break
        else:
            return result, None

        del result[key]

        return result, value

    @staticmethod
    def _get_dict_after_update(input_dict, item):
        """
        Возвращает исходный словарь с добавленной парой ключ-значение.

        :param input_dict: Исходный словарь.
        :param item: Ключ-значение, которые нужно добвать в исходный словарь.
        :return: Исходный словарь с добавленной парой ключ-значение. Если
            ключ уже был в словаре, то его значение перезапишется.
        """
        result = input_dict.copy()
        result[item[0]] = item[1]

        return result
