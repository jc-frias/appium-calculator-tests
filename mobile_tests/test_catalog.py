# test_catalog.py
import pytest
from catalog_page import CatalogPage
from product_details_page import ProductDetailsPage



def test_catalog(driver):
    catalog_page = CatalogPage(driver)

    product_name = catalog_page.get_product_name(0)
    catalog_page.open_product(0)

    product_details_page = ProductDetailsPage(driver)
    details_name = product_details_page.get_product_name()

    assert product_name == details_name, f"Product name does not match, got: {details_name}; Expected: {product_name}"


