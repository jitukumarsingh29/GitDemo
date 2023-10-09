from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver
    delivery_location = (By.ID, "country")
    final_location = (By.LINK_TEXT, "India")
    term_check = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    order_complete_text = (By.CLASS_NAME, "alert-success")

    def select_location(self):
        return self.driver.find_element(*ConfirmPage.delivery_location)

    def selected_location(self):
        return self.driver.find_element(*ConfirmPage.final_location)

    def term_checked(self):
        return self.driver.find_element(*ConfirmPage.term_check)

    def submit_cart(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def order_submission_message(self):
        return self.driver.find_element(*ConfirmPage.order_complete_text)

