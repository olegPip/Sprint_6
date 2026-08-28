import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# Локаторы главной страницы: обе кнопки «Заказать» и два логотипа.
class MainPage(BasePage):

    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Заказать']"
    )

    SCOOTER_LOGO = (
        By.CLASS_NAME,
        "Header_LogoScooter__3lsAR"
    )

    YANDEX_LOGO = (
        By.XPATH,
        "//a[contains(@class, 'Header_LogoYandex')]"
    )

    COOKIE_BUTTON = (
        By.ID,
        "rcc-confirm-button"
    )

    @allure.step("Закрыть баннер с cookie")
    def close_cookie_banner(self):
        self.click_element(self.COOKIE_BUTTON)

    @allure.step("Нажать кнопку «Заказать»")
    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)
