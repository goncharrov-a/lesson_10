# conftest.py

import pytest
from selene import browser, Config
from selenium.webdriver import ChromeOptions


@pytest.fixture(autouse=True)
def setup_browser():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    browser.config = Config(
        driver_options=options,
        timeout=6.0,
        window_width=1920,
        window_height=1080,
    )

    yield

    browser.quit()
