"""Pytest configuration and fixtures."""

from datetime import datetime

import allure
import pytest

from configs.configs import Configs


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Generate test report."""
    outcome = yield
    rep = outcome.get_result()

    # Take screenshot on test failure
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"reports/screenshots/{item.name}_{now}.png"
            page.screenshot(path=file_name)
            print(f"Screenshot saved: {file_name}")
            allure.attach(
                file_name,
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG,
            )
