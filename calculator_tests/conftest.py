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
        file_name = f"{item.name}.png"
        os.makedirs("Screenshot_Tests", exist_ok=True)
        path = os.path.join("Screenshot_Tests", file_name)
        driver.save_screenshot(path)

        screenshot_base64 = driver.get_screenshot_as_base64()
        extra_items = getattr(report, "extras", [])
        extra_items.append(extras.png(screenshot_base64))
        report.extras = extra_items

        print(f"Screenshot saved in {path}")

