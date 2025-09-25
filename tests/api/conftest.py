"""Pytest configuration and fixtures."""

import os
import platform

import pytest

from configs.configs import Configs


@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    """Set the title of the html report."""
    report.title = "Test Automation Report"


def pytest_configure(config):
    """Add environment info to HTML report."""
    # Create reports directory
    os.makedirs("reports/html", exist_ok=True)

    # Add environment info
    config.stash["metadata"] = {
        "Project Name": "Python Demo",
        "Environment": os.getenv("ACTIVE_ENV", "dev"),
        "Base URL": Configs.get().IP_STACK_BASE_URL,
        "Python Version": platform.python_version(),
        "Platform": platform.platform(),
        "Headless": str(not bool(config.getoption("--headed"))),
    }


def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)
    metadata.pop("Python", None)
