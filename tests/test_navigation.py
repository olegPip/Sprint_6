from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from urls import TestUrls

# Проверка логотипа Яндекса, в новом окне через редирект главной страницы Дзена.
class TestNavigation:

    def test_scooter_logo_opens_main_page(self, driver):
        driver.get(TestUrls.BASE_URL)

        main_page = MainPage(driver)

        main_page.click_scooter_logo()

        assert driver.current_url == TestUrls.BASE_URL

    # Тест упадет если ввести URL: https://dzen.ru/, так как сайт реализован иначе.
    def test_yandex_logo_opens_dzen(self, driver):
        driver.get(TestUrls.BASE_URL)

        main_page = MainPage(driver)

        original_window = driver.current_window_handle
        windows_before = driver.window_handles

        main_page.click_yandex_logo()

        WebDriverWait(driver, 8).until(
            lambda driver:
            len(driver.window_handles) > len(windows_before)
        )

        for window in driver.window_handles:
            if window != original_window:
                driver.switch_to.window(window)
                break

        dzen_page = DzenPage(driver)

        assert dzen_page.is_opened()