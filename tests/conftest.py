import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.attachments import attach_screenshot, attach_page_source, attach_logs


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
        attach_page_source("Page source")
        attach_logs("Browser console logs")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)
