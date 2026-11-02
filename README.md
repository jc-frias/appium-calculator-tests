# Appium Calculator Tests

Learning project documenting my transition from manual QA to SDET. It automates tests for the Android Calculator app using **Python**, **Appium** and **pytest**. The tests open the app on an emulator, add numbers and validate the result. When a test fails, a screenshot is saved and embedded in the HTML report.

## Tech stack

- Python 3.13
- Appium 3.6.0 with the UiAutomator2 driver
- pytest 9.1.1 + pytest-html 4.2.0
- Android emulator (x86_64 system image, Android 16)

## Project structure

Everything lives in the `calculator_tests/` folder:

- `base_page.py`: base class with reusable actions (click, read text, wait)
- `calculator_page.py`: Page Object for the Calculator app
- `test_calculator.py`: parametrized tests
- `conftest.py`: driver fixture and failure screenshot hook

## Setup

1. Install Appium and the UiAutomator2 driver.
2. Start an Android emulator with the Calculator app installed.
3. Create a virtual environment and install dependencies from the repo root:

   pip install -r requirements.txt

## Run the tests

1. Start the Appium server: `appium`
2. From the `calculator_tests` folder:

   pytest --html=reporte.html