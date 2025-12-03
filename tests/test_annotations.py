import allure
from selene import browser, have

from utils.attachments import (
    attach_screenshot,
    attach_page_source,
    attach_json
)


@allure.epic("Веб-интерфейс GitHub")
@allure.feature("GitHub Issues")
@allure.story("Просмотр информации об Issue")
@allure.title("Проверка отображения Issue в GitHub")
@allure.description("Тест проверяет корректное отображение заголовка Issue в веб-интерфейсе GitHub.")
@allure.tag("UI", "GitHub", "Issue", "Smoke")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://github.com/goncharrov-a/lesson_10", name="Repository")
@allure.testcase("TC-1", "Проверка отображения Issue title")
@allure.issue("BUG-1024", "Неправильное отображение Issue title")
@allure.label("owner", "goncharrov-a")
@allure.label("layer", "ui")
@allure.label("component", "issues")
@allure.label("tcType", "functional")
def test_issue_title_is_visible_full():
    repo = "goncharrov-a/lesson_10"
    expected_title = "Example_issue"
    issue_number = 1

    with allure.step("Открыть список Issues репозитория"):
        browser.open(f"https://github.com/{repo}/issues")

    with allure.step(f"Открыть Issue с заголовком '{expected_title}'"):
        browser.all('[data-testid="issue-pr-title-link"]').element_by(
            have.exact_text(expected_title)
        ).click()

    with allure.step("Проверить заголовок внутри Issue"):
        browser.element('[data-testid="issue-title"]').should(
            have.exact_text(expected_title)
        )

    with allure.step("Добавить вложения Issue"):
        attach_screenshot("Issue screenshot")
        attach_page_source("Issue page source")
        attach_json(
            {"repository": repo, "issue": issue_number, "title": expected_title},
            "Metadata"
        )