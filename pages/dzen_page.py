from pages.base_page import BasePage


# Проверка перехода на страницу Дзена после клика по логотипу Яндекса
class DzenPage(BasePage):

    def is_opened(self):
        self.wait_for_url_contains("ya.ru")
        return "ya.ru" in self.get_current_url()