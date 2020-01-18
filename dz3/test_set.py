"""Тесты методов множества."""
from itertools import combinations


class TestSetMethodsWoutItemArgs:
    """
    Тесты методов множества.

    Проверяются методы для которых не нужны дополнительные параметры, кроме
    самого множества.
    """

    def test_clear(self, input_set):
        """
        Тест метода clear.

        - Получаю ожидаемый множество;
        - Провожу операцию clear;
        - Проверяю равенство ожидаемого и полученного множества.

        :param input_set: Исходное множество.
        """
        expected_set = set()

        input_set.clear()

        assert expected_set == input_set,\
            'Ожидаемое и полученное множества различаются.'

    def test_pop(self, input_set):
        """
        Тест метода pop.

        - Получаю длину исходного множества;
        - Если длина исходного множества больше нуля:
            - Да:
                - Получаю список всевозможных множеств на основе исходного
                  множества, в которых не хватает одного элемента;
            - Нет:
                - Список всевозможных множеств состоит из пустого множества.
                  В случае пустого исходного множества метод pop сгенерирует
                  ошибку. Исходное множество не изменится, оно останется
                  равным пустому множеству, которое, в свою очередь, находится
                  в списке всевозможных множеств.
        - Провожу операцию pop;
        - Проверяю есть ли полученное множество среди вариантов возможных
          множеств.

        :param input_set: Исходное множество.
        """
        len_input_set = len(input_set)
        if len_input_set:
            expected_sets = list(
                map(set, combinations(input_set, len_input_set - 1)))
        else:
            expected_sets = [set()]

        try:
            input_set.pop()
        except KeyError:
            pass

        assert input_set in expected_sets,\
            'Полученного множества нет среди ожидаемых множеств.'


class TestSetMethodsWithItemArgs:
    """
    Тесты методов множества.

    Проверяются методы для которых нужны дополнительные параметры, кроме
    самого множества.
    """

    def test_add(self, input_set, input_value):
        """
        Тест метода add.

        - Сохраняю начальную длину исходного множества;
        - Получаю ожидаемое множество;
        - Провожу операцию add;
        - Если возникло исключение:
            - Да:
                - Проверяю длину полученного множества, она не должна
                  изменитья;
            - Нет:
                - Проевряю совпадение полученного и ожидаемого множеств;

        :param input_set: Исходное множество.
        :param input_value: Добавляемое значение во множество.
        """
        initial_len = len(input_set)
        expected_set = self._get_set_with_added_item(input_set, input_value)

        try:
            input_set.add(input_value)
        except TypeError:
            assert initial_len == len(input_set),\
                'Длина результирующего множества изменилась.'
        else:
            assert input_set == expected_set,\
                'Полученное множество не совпадает с ожидаемым множеством.'

    def test_discard(self, input_set, input_value):
        """
        Тест метода discard.

        - Получаю ожидаемое множество;
        - Провожу операцию discard;
        - Проверяю равенство полученного и ожидаемого множеств.

        :param input_set: Исходное множество.
        :param input_value: Удаляемый элемент множества.

        """
        expected_set = self._discard_item_from_set(input_set, input_value)

        try:
            input_set.discard(input_value)
        except TypeError:
            pass

        assert input_set == expected_set,\
            'Различаются ожидаемое и полученное множества.'

    def test_remove(self, input_set, input_value):
        """
        Тест метода remove.

        - Сохраняю начальную длину исходного множества;
        - Получаю ожидаемое множества;
        - Провожу над исходным множеством операцию remove;
        - Если возникает исключение TypeError или KeyError:
            - Да:
                - Проверяю равенство длин исходного списка и полученного;
            - Нет:
                - Сравниваю ожидаемое и полученное множества;
                - Проверяю уменьшение длины списка на 1.

        :param input_set: Исходноем множество.
        :param input_value: Удаляемое значение из множества.
        """
        initial_len = len(input_set)
        expected_set = self._get_set_wout_rm_value(input_set, input_value)

        try:
            input_set.remove(input_value)
        except (TypeError, KeyError):
            assert len(input_set) == initial_len,\
                'Длина списка не должна была измениться.'
        else:
            assert expected_set == input_set,\
                'Результат не совпал с ожиданием.'
            assert len(input_set) == initial_len - 1,\
                'Не пройден тест длины списка.'

    @staticmethod
    def _discard_item_from_set(input_set, item):
        """
        Удаляет элемент из множества, если он находится во множестве.

        :param input_set: Исходное множество.
        :param item: Элемент, которых нужно удалить из исходного множества.
        :return: Результирующее множество, в котором удалён элемент item, если
            он был в этом множестве.
        """
        try:
            result = input_set - set([item])
        except TypeError:
            result = input_set

        return result

    @staticmethod
    def _get_set_with_added_item(input_set, item):
        """
        Функция имитирует добавление элемента во множество.

        :param input_set: Исходное множество.
        :param item: Элемент, которых нужно добавить в исходное множество.
        :return: Результирующее множество, в которое добавлен новый элемент.
        """
        try:
            hash(item)
        except TypeError:
            result = input_set
        else:
            result = input_set | set([item])

        return result

    @staticmethod
    def _get_set_wout_rm_value(input_set, item):
        """
        Удаляет элемент из множества, если такой элемент есть в нём.

        :param input_set: Исходное множество.
        :param item: Элемент, которых нужно удалить из исходного множества.
        :return: Результирующее множество, из которого удалён элемент item,
            если он там был.
        """
        try:
            hash(item)
        except TypeError:
            return input_set

        return input_set - set([item]) if item in input_set else input_set
