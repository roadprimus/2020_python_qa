"""Тесты методов списка."""


class TestListMethodsWoutItemArgs:
    """
    Тесты методов списка.

    Проверяются методы для которых не нужны дополнительные параметры, кроме
    самого списка.
    """

    def test_clear(self, input_list):
        """
        Тест метода clear.

        - Получаю ожидаемый список;
        - Провожу операцию clear;
        - Проверяю равенство ожидаемого и полученного списков.

        :param input_list: Исходный список.
        """
        expected_list = []

        input_list.clear()

        assert expected_list == input_list,\
            'Ожидаемый и полученный списки различаются.'

    def test_reverse(self, input_list):
        """
        Тест метода reverse.

        - Получаю ожидаемый список;
        - Провожу операцию reverse;
        - Проверяю равенство ожидаемого и полученного списков.

        :param input_list: Исходный список.
        """
        expected_list = input_list[::-1]

        input_list.reverse()

        assert expected_list == input_list,\
            'Ожидаемый и полученный списки различаются.'


class TestListMethodsWithItemArgs:
    """
    Тесты методов списка.

    Проверяются методы для которых нужны дополнительные параметры, кроме
    самого списка.
    """

    def test_append(self, input_list, input_value):
        """
        Тест метода append.

        - Сохраняю начальную длину исходного списка;
        - Провожу операцию append;
        - Проверяю равенство добавляемого элемента и последнего элемента
          в полученном списке;
        - Проверяю увеличение длины списка на 1.

        :param input_list: Исходный список.
        :param input_value: Добавляемое значение в список.

        """
        initial_len = len(input_list)

        input_list.append(input_value)

        assert input_list[-1] == input_value,\
            'Значение не добавлено в конец списка.'
        assert len(input_list) == initial_len + 1,\
            'Не пройден тест длины списка.'

    def test_count(self, input_list, input_value):
        """
        Тест метода append.

        - Получаю ожидаемое количество элементов;
        - Провожу операцию count;
        - Проверяю равенство ожидаемого и полученного количества элементов.

        :param input_list: Исходный список.
        :param input_value: Добавляемое значение в список.

        """
        expected_count = self._count(input_list, input_value)

        result_count = input_list.count(input_value)

        assert expected_count == result_count,\
            'Различаются ожидаемое и полученное значения.'

    def test_remove(self, input_list, input_value):
        """
        Тест метода remove.

        - Сохраняю начальную длину исходного списка;
        - Получаю ожидаемый список (из исходного списка убраю первое
          вхождение удаляемого значения);
        - Провожу над исходным списком операцию remove;
        - Если возникает исключение ValueError:
            - Да:
                - Проверяю равенство длин исходного списка и ожидаемого;
            - Нет:
                - Сравниваю ожидаемый и полученный списки;
                - Проверяю уменьшение длины списка на 1.

        :param input_list: Исходный список.
        :param input_value: Удаляемое значение из списка.
        """
        initial_len = len(input_list)
        expected_list = self._remove(input_list, input_value)

        try:
            input_list.remove(input_value)
        except ValueError:
            assert len(expected_list) == initial_len,\
                'Длина списка не должна была измениться.'
        else:
            assert expected_list == input_list,\
                'Результат не совпал с ожиданием.'
            assert len(input_list) == initial_len - 1,\
                'Не пройден тест длины списка.'

    @staticmethod
    def _remove(lst, rm_value):
        """
        Имитация метода remove у списка.

        Функция возвращает список без первого встретившегося значения
        rm_value.

        :param lst: Список из которого нужно убрать первое вхождение
            rm_value.
        :param rm_value: Значение, первое вхождение которого удаляется из
            из результирующего списка.
        :return: Список, который идентичен списку lst, но в котором
            отсутствует одно первое вхождение rm_value.
        """
        list_wout_first_rm_value = []
        first_rm_value_removed = False

        for value in lst:
            if not first_rm_value_removed and value == rm_value:
                first_rm_value_removed = True
            else:
                list_wout_first_rm_value.append(value)

        return list_wout_first_rm_value

    @staticmethod
    def _count(lst, item):
        """
        Функция возвращает количество элементов item в списке lst.

        :param lst: Список в котором нужно определить количество элементов
            item.
        :param item: Значение, количество которых определяется в списе lst.
        :return: Количество элементов item в списке lst.
        """
        counter = 0
        for value in lst:
            if value == item:
                counter += 1

        return counter
