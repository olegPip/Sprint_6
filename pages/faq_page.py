from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FAQPage:

    def __init__(self, driver):
        self.driver = driver
        # Инициализируем ожидание (максимум 8 секунд)
        self.wait = WebDriverWait(driver, 8)

    def get_question(self, question_text):
        return (
            By.XPATH,
            f"//div[@data-accordion-component='AccordionItemButton'"
            f" and normalize-space()='{question_text}']"
        )

    def get_answer(self, question_text):
        return (
            By.XPATH,
            "//div[@data-accordion-component='AccordionItem']"
            f"[.//div[@data-accordion-component='AccordionItemButton'"
            f" and normalize-space()='{question_text}']]"
            "//div[@data-accordion-component='AccordionItemPanel']"
        )

    def click_question(self, question_text):
        locator = self.get_question(question_text)

        # 1. Ждем, пока элемент появится в DOM-дереве страницы
        question = self.wait.until(EC.presence_of_element_located(locator))

        # 2. Центрируем элемент на экране, чтобы убрать перекрытие картинкой самоката
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            question
        )

        # 3. Ждем, пока элемент станет окончательно кликабельным после скролла
        self.wait.until(EC.element_to_be_clickable(locator))

        try:
            question.click()
        except Exception:
            # Резервный вариант: если нативный клик все еще перехвачен, кликаем через JavaScript напрямую
            self.driver.execute_script("arguments[0].click();", question)

    def is_question_expanded(self, question_text):
        locator = self.get_question(question_text)
        question = self.wait.until(EC.presence_of_element_located(locator))
        return question.get_attribute("aria-expanded") == "true"

    def is_answer_visible(self, question_text):
        locator = self.get_answer(question_text)
        try:
            # Проверяем видимость элемента с помощью ожиданий
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except Exception:
            return False

    def get_answer_text(self, question_text):
        locator = self.get_answer(question_text)
        # Ждем, пока текст ответа полностью отобразится (анимация раскладывания завершится)
        answer = self.wait.until(EC.visibility_of_element_located(locator))
        return answer.text
