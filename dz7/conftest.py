"""Настройки фикстур для dz7."""
import pytest
from selenium import webdriver

from .constants import (
    BROWSER_CHOICE_ERROR, BrowserName, HEADLESS, OPENCART_PATH)


def pytest_addoption(parser):
    """Добавляет ключи browser и url при вызове pytest."""
    parser.addoption(
        '--url', action='store', default=OPENCART_PATH, help='URL')

    parser.addoption(
        '--browser',
        action='store',
        default=BrowserName.FIREFOX,
        help='Browser'
    )


@pytest.fixture
def browser_and_url(request):
    """Передаёт браузер и URL opencart в тесты.

    Args:
        request: Стандартная фикстура pytest.

    Raises:
        AssertionError: Если указан браузер, который не является
            ни Firefox, ни Chrome.

    Returns:
        tuple: Веб-драйвер, URL opencart.
    """
    browser_name = request.config.getoption('--browser')
    url = request.config.getoption('--url')

    if browser_name == BrowserName.CHROME:
        options = webdriver.ChromeOptions()
        options.add_argument(HEADLESS)
        wd = webdriver.Chrome(
            options=options, executable_path='chromedriver_80')
    elif browser_name == BrowserName.FIREFOX:
        options = webdriver.FirefoxOptions()
        options.add_argument(HEADLESS)
        wd = webdriver.Firefox(options=options)
    else:
        assert False, BROWSER_CHOICE_ERROR

    request.addfinalizer(wd.quit)

    return wd, url
