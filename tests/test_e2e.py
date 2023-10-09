import time
import pytest
from argparse import Action

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.CheckoutPage import CheckoutPage
from page_objects.ConfirmPage import ConfirmPage
from page_objects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_item()
        log.info("getting all the cart titles")
        assert self.driver.current_url == "https://rahulshettyacademy.com/angularpractice/shop"
        # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        # checkout_page = CheckoutPage(self.driver)
        products = checkout_page.get_cart_title()
        i = -1
        for product in products:
            i += 1
            product_text = product.text
            log.info(product_text)
            # print(checkout_page.get_product_footer())
            if product_text == "Blackberry":
                checkout_page.get_product_footer()[i].click()
        self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight)")
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkout_page.checkout_items_p().click()
        self.driver.get_screenshot_as_file("checkout.png")
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        confirm_page = checkout_page.checkout_items_s()
        log.info("Entering country name as ind")
        # confirm_page = ConfirmPage(self.driver)
        # self.driver.find_element(By.ID, "country").send_keys("ind")
        confirm_page.select_location().send_keys("ind")
        self.verify_link_presence("India")
        confirm_page.selected_location().click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirm_page.term_checked().click()
        # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        confirm_page.submit_cart().click()
        # we can write without tag name as it is optional and use to make unique
        # success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        success_text = confirm_page.order_submission_message().text
        log.info("Test received from application is " + success_text)
        assert "Success! Thank you!" in success_text
        time.sleep(3)
        self.driver.close()