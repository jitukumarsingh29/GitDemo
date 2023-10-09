from selenium.webdriver.common.by import By

from page_objects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    radio = (By.ID, "inlineRadio1")
    submit = (By.XPATH, "//input[@type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")

    def shop_item(self):
        # return self.driver.find_element(*HomePage.shop)
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
        # putting start * will make shop variable as tuple
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def get_radio(self):
        return self.driver.find_element(*HomePage.radio)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_message(self):
        return self.driver.find_element(*HomePage.success_message)
