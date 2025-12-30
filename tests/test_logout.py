from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_logout(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.slow()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bm-menu"))
    )

    logout = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )

    logout.click()
    driver.slow()

    assert "saucedemo.com" in driver.current_url