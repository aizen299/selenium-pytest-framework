import os
from datetime import datetime

def capture_screenshot(driver, test_name):
    os.makedirs("reports/screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(
        f"reports/screenshots/{test_name}_{timestamp}.png"
    )