"""Тесты методов Строки."""
import re


class TestStringMethodsWoutItemArgs:
    """
    Тесты методов строки.

    Проверяются методы для которых не нужны дополнительные параметры, кроме
    самой строки.
    """

    ord_A = ord('A')
    ord_Z = ord('Z')
    ord_a = ord('a')
    ord_z = ord('z')

    def test_isalpha(self, input_string):
        """
        Тест метода isalpha.

        - Получаю ожидаемую строку;
        - Провожу операцию isalpha;
        - Проверяю равенство полученной и ожидаемой строк.

        :param input_string: Исходная строка.
        """
        expected_value = self._isalpha(input_string)
        result_value = input_string.isalpha()

        assert expected_value == result_value,\
            'Ожидаемая и полученная сроки различаются.'

    def test_islower(self, input_string):
        """
        Тест метода islower.

        - Получаю ожидаемую строку;
        - Провожу операцию islower;
        - Проверяю равенство полученной и ожидаемой строк.

        :param input_string: Исходная строка.
        """
        expected_value = self._islower(input_string)
        result_value = input_string.islower()

        assert expected_value == result_value,\
            'Ожидаемая и полученная сроки различаются.'

    def test_upper(self, input_string):
        """
        Тест метода upper.

        - Получаю ожидаемую строку;
        - Провожу операцию upper;
        - Проверяю равенство полученной и ожидаемой строк.

        :param input_string: Исходная строка.
        """
        expected_string = self._upper(input_string)
        result_string = input_string.upper()

        assert expected_string == result_string,\
            'Ожидаемая и полученная сроки различаются.'

    @property
    def _delta_a_A(self):
        """Возвращает разницу между кодам символов 'a' и 'A'."""
        return self.ord_a - self.ord_A

    def _isalpha(self, input_string):
        """
        Проверяет состоит ли исходная строка из букв.

        :param input_string: Исходная строка.
        :return: True или False.
        """
        result = False
        for s in input_string:
            ord_s = ord(s)
            print('ord_s: ', ord_s)
            if ord_s < self.ord_A or ord_s > self.ord_z:
                break
        else:
            if input_string:
                result = True

        return result

    def _islower(self, input_string):
        """
        Проверяет состоит ли исходная строка из символов в нижнем регистре.

        :param input_string: Исходная строка.
        :return: True или False.
        """
        counter_not_alpha_symbols = 0
        result = False
        for s in input_string:
            ord_s = ord(s)
            if self.ord_A <= ord_s <= self.ord_Z:
                break
            elif ord_s < self.ord_A or ord_s > self.ord_z:
                counter_not_alpha_symbols += 1
        else:
            if input_string:
                result = True

        if counter_not_alpha_symbols == len(input_string):
            result = False

        return result

    def _upper(self, input_string):
        """
        Возвращает исходную строку в верхнем регистре.

        :param input_string: Исходная строка.
        :return: Исходная строка в верхнем регистре.
        """
        result_lst = []
        for s in input_string:
            add_to_result = s
            ord_s = ord(s)
            if self.ord_a <= ord_s <= self.ord_z:
                ord_S = ord_s - self._delta_a_A
                add_to_result = chr(ord_S)
            else:
                add_to_result = s
            result_lst.append(add_to_result)

        return ''.join(result_lst)


class TestStringMethodsWithItemArgs:
    """
    Тесты методов строки.

    Проверяются методы для которых нужны дополнительные параметры, кроме самой
    строки.
    """

    def test_endswith(self, input_string, input_str_value):
        """
        Тест метода endswith.

        - Получаю ожидаемый результат;
        - Провожу операцию endswith;
        - Проверяю равенство полученного и ожидаемого результата.

        :param input_string: Исходная строка.
        :param input_str_value: Строка-шаблон.
        """
        expected_value = self._endswith(input_string, input_str_value)
        result_value = input_string.endswith(input_str_value)

        assert expected_value == result_value,\
            'Ожидаемая и полученная сроки различаются.'

    def test_split(self, input_string, input_str_value):
        """
        Тест метода split.

        - Получаю ожидаемый результат;
        - Провожу операцию split;
        - Если возникал ошибка ValueError:
            - Да:
                - Проверяю равенство input_str_value == "";
            - Нет:
                - Проверяю равенство полученного и ожидаемого результата.

        :param input_string: Исходная строка.
        :param input_str_value: Строка-шаблон.
        """
        expected_list = self._split(input_string, input_str_value)
        try:
            result_list = input_string.split(input_str_value)
        except ValueError:
            assert input_str_value == '',\
                'Сгенерирована ошибка ValueError, хотя input_str_value != "" '
        else:
            assert expected_list == result_list,\
                'Ожидаемая и полученная сроки различаются.'

    def test_startswith(self, input_string, input_str_value):
        """
        Тест метода startswith.

        - Получаю ожидаемый результат;
        - Провожу операцию startswith;
        - Проверяю равенство полученного и ожидаемого результата.

        :param input_string: Исходная строка.
        :param input_str_value: Строка-шаблон.
        """
        expected_value = self._startswith(input_string, input_str_value)
        result_value = input_string.startswith(input_str_value)

        assert expected_value == result_value,\
            'Ожидаемая и полученная сроки различаются.'

    @staticmethod
    def _endswith(input_string, templ):
        """
        Проверяет заканчивается ли строка input_string шаблоном templ.

        :param input_string: Исходная строка.
        :param templ: Строка-шаблон.
        :return: True или False.
        """
        len_input_string = len(input_string)
        len_templ = len(templ)
        if len_templ > len_input_string:
            return False

        if not templ:
            return True

        end_input_string = input_string[-len(templ):]

        if end_input_string == templ:
            return True
        else:
            return False

    @staticmethod
    def _split(input_string, templ):
        """
        Проводит разбиение строки input_string по разделителю input_str_value.

        Результат возвращается в виде списка подстрок.

        :param input_string: Исходная строка.
        :param templ: Строка-шаблон.
        :return: Список подстрок.
        """
        return re.split(templ, input_string)

    @staticmethod
    def _startswith(input_string, templ):
        """
        Проверяет начинает ли строка input_string с шаблона templ.

        :param input_string: Исходная строка.
        :param templ: Строка-шаблон.
        :return: True или False.
        """
        len_input_string = len(input_string)
        len_templ = len(templ)
        if len_templ > len_input_string:
            return False

        if not templ:
            return True

        end_input_string = input_string[:len(templ)]

        if end_input_string == templ:
            return True
        else:
            return False
