import pytest

from utils.attachments import (
    attach_screenshot,
    attach_page_source,
    attach_json
)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Авто добавление аттача, при падении."""
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        attach_screenshot("Failure screenshot")
        attach_page_source("Failure page source")
        attach_json({"test": item.name, "status": "failed"}, "Failure metadata")
