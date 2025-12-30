from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_checkout_with_empty_cart(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.slow()

    checkout_btns = driver.find_elements(By.ID, "checkout")
    assert len(checkout_btns) == 0