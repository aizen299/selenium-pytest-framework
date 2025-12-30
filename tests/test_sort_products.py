from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.login_page import LoginPage

def test_sort_products_low_to_high(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("lohi")
    driver.slow()

    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    price_values = [float(p.text.replace("$", "")) for p in prices]

    assert price_values == sorted(price_values)