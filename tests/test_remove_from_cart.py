from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_remove_item_from_cart(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.slow()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.slow()

    remove_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-bike-light"))
    )
    remove_btn.click()
    driver.slow()

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0