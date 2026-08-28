from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from urls import TestUrls


# Проверка переходов по логотипам.
class TestNavigation:

    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.go_to(TestUrls.BASE_URL)
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == TestUrls.BASE_URL

    # Тест проверяет открытие Дзена в новом окне.
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)

        main_page.go_to(TestUrls.BASE_URL)

        original_window = main_page.get_current_window()

        main_page.click_yandex_logo()
        main_page.switch_to_new_window(original_window)

        dzen_page = DzenPage(driver)

        assert dzen_page.is_opened()
