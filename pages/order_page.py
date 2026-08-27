from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Локаторы для формы заказа.
class OrderPage:

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

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8)

    def fill_personal_data(
        self,
        name,
        surname,
        address,
        phone
    ):
        self.driver.find_element(
            *self.NAME_INPUT
        ).send_keys(name)

        self.driver.find_element(
            *self.SURNAME_INPUT
        ).send_keys(surname)

        self.driver.find_element(
            *self.ADDRESS_INPUT
        ).send_keys(address)

        self.driver.find_element(
            *self.METRO_INPUT
        ).click()

        metro_option = (
            By.CSS_SELECTOR,
            ".select-search__option"
        )

        self.wait.until(
            EC.element_to_be_clickable(metro_option)
        ).click()

        self.driver.find_element(
            *self.PHONE_INPUT
        ).send_keys(phone)

    def click_next(self):
        self.driver.find_element(
            *self.NEXT_BUTTON
        ).click()

    def fill_rental_data(
            self,
            date,
            comment,
            color
    ):
        self.driver.find_element(
            *self.DATE_INPUT
        ).click()

        self.driver.find_element(
            *self.DATE_INPUT
        ).send_keys(date)

        self.driver.find_element(
            *self.DATE_INPUT
        ).send_keys("\ue007")

        self.wait.until(
            EC.element_to_be_clickable(
                self.RENT_PERIOD
            )
        ).click()

        rent_period_option = (
            By.XPATH,
            "//div[@role='option' and normalize-space()='сутки']"
        )

        self.wait.until(
            EC.visibility_of_element_located(
                rent_period_option
            )
        ).click()

        if color == "black":
            self.driver.find_element(
                *self.BLACK_COLOR
            ).click()
        elif color == "grey":
            self.driver.find_element(
                *self.GREY_COLOR
            ).click()

        self.driver.find_element(
            *self.COMMENT_INPUT
        ).send_keys(comment)


    def click_order(self):
        self.driver.find_element(
            *self.ORDER_BUTTON
        ).click()

    def confirm_order(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.CONFIRM_ORDER_BUTTON
            )
        ).click()

    def is_order_created(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        ).is_displayed()