import pytest
from utils.driver_factory import get_driver
from utils.screenshot import capture_screenshot

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")
    driver.slow()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            capture_screenshot(driver, item.name)