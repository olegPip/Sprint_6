import pytest
from selenium import webdriver


# Создание и закрытие браузера Firefox
@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")

    browser = webdriver.Firefox(options=options)

    yield browser

    browser.quit()
