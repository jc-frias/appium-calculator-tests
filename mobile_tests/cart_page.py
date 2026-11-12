# cart_page.py
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from base_page import BasePage

NO_ITEM_ELEMENT = "com.saucelabs.mydemoapp.android:id/noItemTitleTV"
NO_ITEM_LOCATOR = (AppiumBy.ID, NO_ITEM_ELEMENT)



class CartPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)


    def get_empty_cart_text(self):
        return self.get_text(NO_ITEM_LOCATOR)