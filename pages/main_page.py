from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


# Локаторы главной страницы: обе кнопки «Заказать» и два логотипа.
class MainPage(BasePage):

    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Заказать']"
    )

    SCOOTER_LOGO = (
        By.CSS_SELECTOR,
        "a.Header_LogoScooter__3lsAR"
    )

    YANDEX_LOGO = (
        By.CSS_SELECTOR,
        "a.Header_LogoYandex__3TSOI"
    )

    COOKIE_BUTTON = (
        By.ID,
        "rcc-confirm-button"
    )

    def close_cookie_banner(self):
        self.click_element(self.COOKIE_BUTTON)

    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON)

    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_windows(self):
        return self.driver.window_handles

    def switch_to_new_window(self, original_window):
        WebDriverWait(self.driver, 8).until(
            lambda driver: len(driver.window_handles) > 1
        )

        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break