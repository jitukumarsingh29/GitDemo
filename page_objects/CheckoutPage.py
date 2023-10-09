from selenium.webdriver.common.by import By

from page_objects.ConfirmPage import ConfirmPage


class CheckoutPage:
    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    def __init__(self, driver):
        self.driver = driver
    product_title = (By.CSS_SELECTOR, ".card-title a")
    # product_header = (By.XPATH, "div/h4/a")
    product_footer = (By.CSS_SELECTOR, ".card-footer button")
    product_checkout_p = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    product_checkout_s = (By.XPATH, "//button[@class='btn btn-success']")

    def get_cart_title(self):
        return self.driver.find_elements(*CheckoutPage.product_title)

    # def get_product_header(self):
    #   return self.driver.find_elements(*CheckoutPage.product_header)

    def get_product_footer(self):
        return self.driver.find_elements(*CheckoutPage.product_footer)

    def checkout_items_p(self):
        return self.driver.find_element(*CheckoutPage.product_checkout_p)

    def checkout_items_s(self):
        # return self.driver.find_element(*CheckoutPage.product_checkout_s)
        self.driver.find_element(*CheckoutPage.product_checkout_s).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page