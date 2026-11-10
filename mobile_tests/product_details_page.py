# product_details_page.py
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from base_page import BasePage

NAME_ELEMENT = "com.saucelabs.mydemoapp.android:id/productTV"
PRODUCT_NAME = (AppiumBy.ID, NAME_ELEMENT)

class ProductDetailsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)


    def get_product_name(self):
        return self.get_text(PRODUCT_NAME)