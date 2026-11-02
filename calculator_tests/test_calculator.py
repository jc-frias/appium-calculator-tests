# test_calculator.py
import pytest
from calculator_page import CalculatorPage


@pytest.mark.parametrize("first, second, expected",
                         [(25,55,80),
                          (1,1,2),
                          (0,0,0)])
def test_calculator(driver, first, second, expected):
    calculator_page = CalculatorPage(driver)

    calculator_page.add(first, second)

    actual_result = calculator_page.get_result()

    assert actual_result == str(expected) , f"Error: Incorrect result. Expected {expected}; got {actual_result}"

