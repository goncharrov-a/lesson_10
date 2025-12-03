import json

import allure
from selene import browser


def attach_screenshot(name="Screenshot"):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(png, name=name, attachment_type=allure.attachment_type.PNG)


def attach_page_source(name="Page Source"):
    html = browser.driver.page_source
    allure.attach(html, name=name, attachment_type=allure.attachment_type.HTML)


def attach_logs(name="Browser Console Logs"):
    try:
        logs = browser.driver.get_log("browser")
        text = "\n".join(str(l) for l in logs)
        allure.attach(text, name=name, attachment_type=allure.attachment_type.TEXT)
    except Exception:
        pass


def attach_json(data: dict, name="JSON Data"):
    try:
        json_str = json.dumps(data, indent=2, ensure_ascii=False)
        allure.attach(json_str, name=name, attachment_type=allure.attachment_type.JSON)
    except Exception:
        allure.attach(str(data), name=name, attachment_type=allure.attachment_type.TEXT)
