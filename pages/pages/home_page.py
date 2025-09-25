import allure
from playwright.sync_api import Page, expect

from core.page.base_page import BasePage
from pages.locators.home_page_locators import HomePageLocators


class HomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Verify home page displays correctly")
    def verify_home_page_displays(self):
        expect(self.page.locator(HomePageLocators.PAGE_TITLE_LBL)).to_have_text(
            "Swag La"
        )
        expect(self.page.locator(HomePageLocators.BUGER_BTN)).to_be_visible()
        expect(self.page.locator(HomePageLocators.SHOPPING_CART_BTN)).to_be_visible()
        return self

    @allure.step("Verify page title is '{expected_title}'")
    def verify_page_title(self, expected_title: str):
        """Verify the page title matches the expected title.

        Args:
            expected_title (str): The expected title of the page.

        Returns:
            HomePage: The current instance for method chaining.
        """
        self.expect_element_text(HomePageLocators.PAGE_TITLE_LBL, expected_title)
        return self

    @allure.step("Verify burger button is visible")
    def verify_burger_button_visible(self):
        """Verify the burger button is visible on the page.

        Returns:
            HomePage: The current instance for method chaining.
        """
        self.expect_element_visible(HomePageLocators.BUGER_BTN)
        return self

    @allure.step("Verify shopping cart button is visible")
    def verify_shopping_cart_button_visible(self):
        """Verify the shopping cart button is visible on the page.

        Returns:
            HomePage: The current instance for method chaining.
        """
        self.expect_element_visible(HomePageLocators.SHOPPING_CART_BTN)
        return self
