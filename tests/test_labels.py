import allure
from selene import browser, have


def test_issue_title_is_visible_lambda():
    repo = "goncharrov-a/lesson_10"
    expected_title = "Example_issue"

    with allure.step("Открыть страницу Issues репозитория"):
        browser.open(f"https://github.com/{repo}/issues")

    with allure.step(f"Открыть Issue с названием '{expected_title}'"):
        browser.all('[data-testid="issue-pr-title-link"]').element_by(
            have.exact_text(expected_title)
        ).click()

    with allure.step("Проверить заголовок внутри Issue"):
        browser.element('[data-testid="issue-title"]').should(
            have.exact_text(expected_title)
        )
