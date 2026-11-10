# base_page.py
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator: tuple):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise Exception(f" Framework Error: 10 seconds passed and it could not be clicked. {locator}") from None

    def get_text(self, locator: tuple) -> str:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def element_exists(self, locator: tuple) -> bool:
        return len(self.driver.find_elements(*locator)) > 0

    def go_back(self):
        self.driver.back()
