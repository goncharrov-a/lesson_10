import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.attachments import (
    attach_screenshot,
    attach_page_source,
    attach_logs,
    attach_json
)


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.base_url = "https://github.com"
    browser.config.timeout = 6.0

    yield

    if request.node.rep_call.failed:
        attach_screenshot("Failure screenshot")
        attach_page_source("Failure page source")
        attach_logs("Browser console logs")
        attach_json(
            {"test": request.node.name, "status": "failed"},
            "Failure metadata"
        )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook к rep_call фикстуры."""
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)
