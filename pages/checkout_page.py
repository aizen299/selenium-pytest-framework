from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    CHECKOUT = (By.ID, "checkout")
    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    BACK_HOME = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def complete_checkout(self, first, last, postal):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT)).click()
        self.driver.slow()

        self.driver.find_element(*self.FIRST).send_keys(first)
        self.driver.slow()

        self.driver.find_element(*self.LAST).send_keys(last)
        self.driver.slow()

        self.driver.find_element(*self.POSTAL).send_keys(postal)
        self.driver.slow()

        self.driver.find_element(*self.CONTINUE).click()
        self.driver.slow()

        self.wait.until(EC.element_to_be_clickable(self.FINISH)).click()
        self.driver.slow()

        self.wait.until(EC.element_to_be_clickable(self.BACK_HOME)).click()
        self.driver.slow()