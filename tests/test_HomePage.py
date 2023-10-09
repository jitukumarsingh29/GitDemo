import time

from selenium.webdriver.support.select import Select

from page_objects.HomePage import HomePage
from test_data.HomePageData import HomePageData
from utilities.BaseClass import BaseClass
import pytest


class TestHomePage(BaseClass):
    def test_form_submission(self, get_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        log.info("The first name is " + get_data["name"] )
        home_page.get_name().send_keys(get_data["name"])
        home_page.get_email().send_keys(get_data["email"])
        home_page.get_password().send_keys(get_data["password"])
        home_page.get_checkbox().click()
        home_page.get_dropdown()
        self.select_option_by_text(home_page.get_dropdown(), get_data["gender"])
        # select.select_by_visible_text("Male")
        time.sleep(3)
        home_page.get_radio().click()
        home_page.get_submit().click()
        time.sleep(3)
        message = home_page.get_message().text
        log.info("The submission message is displayed as: " + message)
        assert "success" in message
        self.driver.refresh()

    # @pytest.fixture(params=HomePageData.test_home_page_data)  # this line of code is to get data from list object
    # below line adding to get data from excel
    @pytest.fixture(params=HomePageData.get_test_excel_data("TestCase2"))
    def get_data(self, request):
        return request.param
