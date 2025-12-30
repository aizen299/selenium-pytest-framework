from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_checkout_missing_postal_code(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product_to_cart()
    products.go_to_cart()

    driver.find_element(By.ID, "checkout").click()
    driver.slow()

    driver.find_element(By.ID, "first-name").send_keys("Ben")
    driver.slow()

    driver.find_element(By.ID, "last-name").send_keys("10")
    driver.slow()

    driver.find_element(By.ID, "continue").click()
    driver.slow()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    assert "postal code" in error.text.lower()