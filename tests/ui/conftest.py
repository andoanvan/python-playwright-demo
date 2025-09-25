"""Pytest configuration and fixtures."""

import os
import platform
from datetime import datetime

import allure
import pytest

from configs.configs import Configs


@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    """Set the title of the html report."""
    report.title = "Test Automation Report"


def pytest_configure(config):
    """Add environment info to HTML report."""
    # Create reports directory
    os.makedirs("reports", exist_ok=True)

    # Add environment info
    config.stash["metadata"] = {
        "Project Name": "Python Demo",
        "Environment": os.getenv("ACTIVE_ENV", "dev"),
        "Base URL": Configs.get().BASE_URL,
        "Python Version": platform.python_version(),
        "Platform": platform.platform(),
        "Headless": str(not bool(config.getoption("--headed"))),
    }


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
