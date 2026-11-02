# calculator_page.py
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver


from base_page import BasePage


class CalculatorPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    SUM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "plus")
    EQUAL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "equals")
    RESULT = (AppiumBy.ID, 'com.google.android.calculator:id/result_final')



    def press_number(self, number):
        for digit in str(number):
            NUMERO = (AppiumBy.ACCESSIBILITY_ID, f"{digit}")
            self.hacer_clic(NUMERO)


    def get_result(self):
        result = self.obtener_texto(self.RESULT)
        return result

    def add(self, first, second):
        self.press_number(first)
        self.hacer_clic(self.SUM_BUTTON)
        self.press_number(second)
        self.hacer_clic(self.EQUAL_BUTTON)