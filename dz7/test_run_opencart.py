"""Тест открытия opencart."""
from selenium.common.exceptions import NoSuchElementException

from .constants import H1, H1_TEXT, OPENCART_ERROR


def test_run_opencart(browser_and_url):
    """Тест открытия opencart в выбранном браузере.

    - Получаю веб-драйвер и адрес opencart;
    - Отправляю запрос на opencart;
    - Получаю элемент h1 на возвращённой странице;
        - Если такого элемента нет на странице, то тест не пройден;
    - Сравниваю текст в полученном h1 и ожидаемый.

    Args:
        browser_and_url (tuple): кортеж, состоящий из веб-драйвера и
            и url opencart.
    """
    browser, url = browser_and_url
    browser.get(url)
    try:
        element = browser.find_element_by_css_selector(H1)
    except NoSuchElementException:
        assert False, OPENCART_ERROR

    assert element.text == H1_TEXT, OPENCART_ERROR
