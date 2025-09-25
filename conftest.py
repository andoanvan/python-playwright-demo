"""Pytest configuration and fixtures."""

import os

import pytest


def pytest_addoption(parser):
    """Add command line options."""
    parser.addoption(
        "--env", action="store", default="dev", help="Environment: dev/staging/prod"
    )


@pytest.fixture(scope="session", autouse=True)
def init_config(request):
    """Initialize test configuration."""
    env = request.config.getoption("--env")
    os.environ["ACTIVE_ENV"] = env
