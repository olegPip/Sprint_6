import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import TestUrls
from datetime import datetime, timedelta

# Проверка формы оформления заказа.
class TestOrder:

    @pytest.mark.parametrize(
        "name, surname, address, phone, comment, color",
        [
            (
                "Иван",
                "Петров",
                "Москва, улица Ленина, дом 10",
                "89991234567",
                "Позвонить перед доставкой",
                "black",
            ),
            (
                "Анна",
                "Смирнова",
                "Москва, улица Тверская, дом 15",
                "89997654321",
                "Оставить у подъезда",
                "grey",
            ),
        ],
    )
    def test_create_order(
        self,
        driver,
        name,
        surname,
        address,
        phone,
        comment,
        color,
    ):
        driver.get(TestUrls.BASE_URL)

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.close_cookie_banner()
        main_page.click_order_button()

        order_page.fill_personal_data(
            name,
            surname,
            address,
            phone,
        )

        order_page.click_next()

        delivery_date = (
                datetime.now() + timedelta(days=1)
        ).strftime("%d.%m.%Y")

        order_page.fill_rental_data(
            delivery_date,
            comment,
            color,
        )

        order_page.click_order()
        order_page.confirm_order()

        assert order_page.is_order_created()