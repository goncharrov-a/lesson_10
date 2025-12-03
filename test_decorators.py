import allure
from selene import browser, have


@allure.step("Открыть страницу Issues репозитория: {repo}")
def open_issues_page(repo):
    browser.open(f"https://github.com/{repo}/issues")


@allure.step("Открыть Issue с заголовком: {title}")
def open_issue_by_title(title):
    browser.all('[data-testid="issue-pr-title-link"]').element_by(have.exact_text(title)).click()


@allure.step("Проверить отображение заголовка Issue: {expected_title}")
def should_have_issue_title(expected_title):
    browser.element('[data-testid="issue-title"]').should(have.exact_text(expected_title))


def test_issue_title_is_visible():
    repo = "goncharrov-a/lesson_10"
    expected_title = "Example_issue"

    open_issues_page(repo)
    open_issue_by_title(expected_title)
    should_have_issue_title(expected_title)
