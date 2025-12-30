from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage

def test_complete_purchase_flow(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product_to_cart()
    products.go_to_cart()

    checkout = CheckoutPage(driver)
    checkout.complete_checkout("Ben", "Tennyson", "12345")

    assert "inventory" in driver.current_url