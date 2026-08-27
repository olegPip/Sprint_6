from selenium.webdriver.support.ui import WebDriverWait

# Проверка перехода на страницу дзен, после клика по логотипу Яндекса
class DzenPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8)

    def is_opened(self):
        self.wait.until(
            lambda driver: "ya.ru" in driver.current_url
        )
        # При клике на логотип Яндекса, в новом окне через редирект откроется не главная страница Дзена а страница Яндекс.
        return "ya.ru" in self.driver.current_url