
from appium.webdriver.common.appiumby import AppiumBy
from base_page import BasePage
from appium.webdriver.webdriver import WebDriver

ELEMENT_CLICKABLE = "com.saucelabs.mydemoapp.android:id/productIV"
PRODUCTS = (AppiumBy.ID, ELEMENT_CLICKABLE)
ELEMENT_TEXT = "com.saucelabs.mydemoapp.android:id/titleTV"
PRODUCTS_NAME = (AppiumBy.ID, ELEMENT_TEXT)
CART_RESOURCE_ID = "com.saucelabs.mydemoapp.android:id/cartIV"
CART_ELEMENT = (AppiumBy.ID, CART_RESOURCE_ID)


class CatalogPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)


    def open_product(self, index):
        products = self.get_elements(PRODUCTS)
        product = products[index]
        product.click()

    def get_product_name(self, index):
        names = self.get_elements(PRODUCTS_NAME)
        name = names[index]
        return name.text

    def open_cart(self):
        self.click_element(CART_ELEMENT)