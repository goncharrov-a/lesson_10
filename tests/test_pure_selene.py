from selene import browser, have


def test_issue_title_is_visible_short():
    repo = "goncharrov-a/lesson_10"
    expected_title = "Example_issue"
    browser.open(f"https://github.com/{repo}/issues")
    browser.all('[data-testid="issue-pr-title-link"]').element_by(
        have.exact_text(expected_title)
    ).click()
    browser.element('[data-testid="issue-title"]').should(
        have.exact_text(expected_title)
    )
