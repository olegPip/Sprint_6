from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8)

    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def fill_form(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def go_to(self, url):
        self.driver.get(url)

    def get_element_text(self, locator):
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except Exception:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_windows(self):
        return self.driver.window_handles

    def switch_to_new_window(self, original_window):
        self.wait.until(
            lambda driver: len(driver.window_handles) > 1
        )

        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

    def wait_for_url_contains(self, text):
        self.wait.until(
            lambda driver: text in self.get_current_url()
        )

    def press_enter(self):
        self.driver.switch_to.active_element.send_keys("\ue007")