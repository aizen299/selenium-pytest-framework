from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_cart_persists_after_navigation(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.slow()

    driver.find_element(By.ID, "item_4_title_link").click()
    driver.slow()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.slow()

    cart_item = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )

    assert "Backpack" in cart_item.text