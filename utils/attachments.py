import json

import allure
from allure import attachment_type
from selene import browser


def attach_screenshot(name="Screenshot"):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(png, name=name, attachment_type=attachment_type.PNG)


def attach_page_source(name="Page Source"):
    html = browser.driver.page_source
    allure.attach(html, name=name, attachment_type=attachment_type.HTML)


def attach_json(data: dict, name="Metadata"):
    allure.attach(
        json.dumps(data, indent=2, ensure_ascii=False), name=name, attachment_type=attachment_type.JSON)
