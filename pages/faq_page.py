from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FAQPage(BasePage):

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
        question = self.find_element(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            question
        )

        try:
            self.wait.until(
                lambda driver: question.is_enabled()
                and question.is_displayed()
            )
            question.click()
        except Exception:
            self.driver.execute_script(
                "arguments[0].click();",
                question
            )

    def is_question_expanded(self, question_text):
        locator = self.get_question(question_text)
        question = self.find_element(locator)
        return question.get_attribute("aria-expanded") == "true"

    def is_answer_visible(self, question_text):
        locator = self.get_answer(question_text)

        try:
            return self.wait.until(
                lambda driver: self.find_element(locator).is_displayed()
            )
        except Exception:
            return False

    def get_answer_text(self, question_text):
        locator = self.get_answer(question_text)
        answer = self.find_element(locator)
        return answer.text
