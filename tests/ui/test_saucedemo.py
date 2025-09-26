"""Test suite for SauceDemo application."""

import pytest
from playwright.sync_api import Page

from configs.configs import Configs
from pages.pages.home_page import HomePage
from pages.pages.login_page import LoginPage
from tests.ui.test_base import BaseTest


class TestSauceDemo(BaseTest):
    """Test cases for SauceDemo application."""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup runs before each test."""
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.login_page.goto(Configs().BASE_URL)

    def test_login(self):
        """Test the login functionality."""
        self.login_page.login()
        self.home_page.verify_page_title(
            "Swag Labs"
        ).verify_burger_button_visible().verify_shopping_cart_button_visible()
