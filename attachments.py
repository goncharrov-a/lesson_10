import json

import allure
from allure import attachment_type
from selene import browser


def test_issue_attachments():
    repo = "goncharrov-a/lesson_10"
    issue_number = 1
    issue_title = "Example_issue"

    with allure.step("Открыть страницу Issue в репозитории"):
        browser.open(f"https://github.com/{repo}/issues/{issue_number}")

    with allure.step("Приложить скриншот страницы Issue"):
        screenshot = browser.driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="Issue screenshot",
            attachment_type=attachment_type.PNG,
        )

    with allure.step("Приложить HTML-код страницы Issue"):
        html = browser.driver.page_source
        allure.attach(
            html,
            name="Issue page source",
            attachment_type=attachment_type.HTML,
        )

    with allure.step("Приложить JSON с метаданными Issue"):
        metadata = {
            "repository": repo,
            "issue_number": issue_number,
            "issue_title": issue_title,
        }
        allure.attach(
            json.dumps(metadata, indent=2, ensure_ascii=False),
            name="Issue metadata",
            attachment_type=attachment_type.JSON,
        )
