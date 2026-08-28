import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# Локаторы для формы заказа.
class OrderPage(BasePage):

    NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Имя']"
    )

    SURNAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Фамилия']"
    )

    ADDRESS_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )

    METRO_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Станция метро']"
    )

    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[text()='Далее']"
    )

    DATE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )

    RENT_PERIOD = (
        By.CSS_SELECTOR,
        ".Dropdown-control"
    )

    BLACK_COLOR = (
        By.ID,
        "black"
    )

    GREY_COLOR = (
        By.ID,
        "grey"
    )

    COMMENT_INPUT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]"
        "//button[text()='Заказать']"
    )

    CONFIRM_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]["
        ".//div[contains(text(), 'Хотите оформить заказ?')]"
        "]//button[text()='Да']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]["
        ".//div[contains(text(), 'Заказ оформлен')]"
        "]//div[contains(text(), 'Заказ оформлен')]"
    )

    @allure.step("Заполнить персональные данные: имя, фамилия, адрес и телефон")
    def fill_personal_data(
        self,
        name,
        surname,
        address,
        phone
    ):
        self.fill_form(self.NAME_INPUT, name)
        self.fill_form(self.SURNAME_INPUT, surname)
        self.fill_form(self.ADDRESS_INPUT, address)

        self.click_element(self.METRO_INPUT)

        metro_option = (
            By.CSS_SELECTOR,
            ".select-search__option"
        )

        self.click_element(metro_option)

        self.fill_form(self.PHONE_INPUT, phone)

    @allure.step("Нажать кнопку «Далее»")
    def click_next(self):
        self.click_element(self.NEXT_BUTTON)

    @allure.step("Заполнить данные аренды: дата, срок, цвет и комментарий")
    def fill_rental_data(
        self,
        date,
        comment,
        color
    ):
        self.click_element(self.DATE_INPUT)

        self.fill_form(self.DATE_INPUT, date)
        self.press_enter()

        self.click_element(self.RENT_PERIOD)

        rent_period_option = (
            By.XPATH,
            "//div[@role='option' and normalize-space()='сутки']"
        )

        self.click_element(rent_period_option)

        if color == "black":
            self.click_element(self.BLACK_COLOR)
        elif color == "grey":
            self.click_element(self.GREY_COLOR)

        self.fill_form(self.COMMENT_INPUT, comment)

    @allure.step("Нажать кнопку «Заказать»")
    def click_order(self):
        self.click_element(self.ORDER_BUTTON)

    @allure.step("Подтвердить оформление заказа")
    def confirm_order(self):
        self.click_element(self.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверить, что заказ успешно оформлен")
    def is_order_created(self):
        return self.find_element(self.SUCCESS_MESSAGE).is_displayed()