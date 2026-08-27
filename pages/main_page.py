from selenium.webdriver.common.by import By

# Локаторы главной страницы: обе кнопки «Заказать» и два логотипа.
class MainPage:

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

    def __init__(self, driver):
        self.driver = driver

    def close_cookie_banner(self):
        self.driver.find_element(*self.COOKIE_BUTTON).click()

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def click_scooter_logo(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()