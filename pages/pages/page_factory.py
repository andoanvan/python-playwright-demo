"""Page factory module for managing page objects."""

from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage


class Pages:
    """Factory class for creating and managing page objects."""

    def __init__(self, page: Page):
        self._page = page
        # Initialize pages on demand
        self._login_page = None
        self._home_page = None

    @property
    def login_page(self) -> LoginPage:
        """Get login page instance.

        Returns:
            LoginPage: The login page object
        """
        if not self._login_page:
            self._login_page = LoginPage(self._page)
        return self._login_page

    @property
    def home_page(self) -> HomePage:
        """Get home page instance.

        Returns:
            HomePage: The home page object
        """
        if not self._home_page:
            self._home_page = HomePage(self._page)
        return self._home_page
