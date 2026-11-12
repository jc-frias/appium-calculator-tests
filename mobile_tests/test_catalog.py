# test_catalog.py

import pytest
from catalog_page import CatalogPage
from product_details_page import ProductDetailsPage


@pytest.mark.parametrize("index",[0,
                                  pytest.param(1, marks=pytest.mark.xfail(
                                      reason="App crashes when opening second item", strict=True)),
                                  2,3])
def test_catalog(driver, index):
    catalog_page = CatalogPage(driver)

    product_name = catalog_page.get_product_name(index)
    catalog_page.open_product(index)

    product_details_page = ProductDetailsPage(driver)
    details_name = product_details_page.get_product_name()

    assert product_name == details_name, f"Product name does not match, got: {details_name}; Expected: {product_name}"


