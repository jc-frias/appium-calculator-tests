# base_page.py

from appium.webdriver.webdriver import WebDriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def hacer_clic(self, locator: tuple):
        try:
            elemento = self.wait.until(EC.element_to_be_clickable(locator))
            elemento.click()
        except TimeoutException:
            raise Exception(f" Error del Framework: Pasaron 10 segundos y no se pudo dar clic en {locator}") from None

    def obtener_texto(self, locator: tuple) -> str:
        elemento = self.wait.until(EC.visibility_of_element_located(locator))
        return elemento.text

    def elemento_existe(self, locator: tuple) -> bool:
        return len(self.driver.find_elements(*locator)) > 0

    def go_back(self):
        self.driver.back()
