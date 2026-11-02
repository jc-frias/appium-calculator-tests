from pytest_html import extras
from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest
import os



@pytest.fixture
def driver():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'CelularADB',
        'appPackage': 'com.google.android.calculator',
        'appActivity': 'com.android.calculator2.Calculator',
        'forceAppLaunch': True
    })

    driver_instance = webdriver.Remote('http://127.0.0.1:4723', options=options)
    yield driver_instance  # Cede el control a la prueba
    driver_instance.quit()  # Limpieza garantizada

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs["driver"]
        nombre = f"{item.name}.png"
        os.makedirs("Screenshot_Tests", exist_ok=True)
        ruta = os.path.join("Screenshot_Tests", nombre)
        driver.save_screenshot(ruta)

        foto = driver.get_screenshot_as_base64()
        lista_extras = getattr(report, "extras", [])
        lista_extras.append(extras.png(foto))
        report.extras = lista_extras

        print(f"Foto guardada en {ruta}")

