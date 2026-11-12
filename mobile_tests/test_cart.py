# test_cart.py

from catalog_page import CatalogPage
from cart_page import CartPage

EXPECTED_EMPTY_CART_TEXT = "No Items"


def test_empty_cart(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_cart()

    cart_page = CartPage(driver)
    empty_cart_text = cart_page.get_empty_cart_text()


    assert empty_cart_text == EXPECTED_EMPTY_CART_TEXT, \
        f"Text does not match, got: {empty_cart_text}; Expected: {EXPECTED_EMPTY_CART_TEXT}"