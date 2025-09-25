"""Base page class for common page operations.
This class serves as a foundation for all page objects in the test framework,
providing common methods for interacting with web pages using Playwright.
"""

import allure
from playwright.sync_api import Page, expect
from typing_extensions import Literal


class BasePage:
    """Base page with common functionality.
    This class implements the Page Object Model pattern and contains methods
    that are common across all pages in the application.
    """

    def __init__(self, page: Page):
        """Initialize a new base page.

        Args:
            page (Page): The Playwright page object to interact with.
        """
        self.page = page

    def goto(self, url: str):
        """Navigate to a specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        self.page.goto(url)

    def get_title(self) -> str:
        """Get the current page title.

        Returns:
            str: The title of the current page.
        """
        allure.attach(name="Page Title", body=self.page.title())
        return self.page.title()

    def is_element_text(self, locator: str, text: str) -> bool:
        """Check if an element contains specific text.

        Args:
            locator (str): The locator string to find the element.
            text (str): The text to compare against the element's content.

        Returns:
            bool: True if the element's text matches, False otherwise.
        """
        allure.attach(
            name="Element Text Check",
            body=f"Checking if element '{locator}' has text: {text}",
        )
        return self.page.locator(locator).inner_text() == text

    def is_element_visible(self, locator: str) -> bool:
        """Check if an element is visible on the page.

        Args:
            locator (str): The locator string to find the element.

        Returns:
            bool: True if the element is visible, False otherwise.
        """
        allure.attach(
            name="Element Visibility Check",
            body=f"Checking visibility of element '{locator}'",
        )
        return self.page.locator(locator).is_visible()

    def take_screenshot(self, name: str = "screenshot") -> None:
        """Take a screenshot of the current page state.

        Args:
            name (str): The name for the screenshot file.
        """
        screenshot_path = f"{name}.png"
        self.page.screenshot(path=screenshot_path)
        allure.attach.file(
            screenshot_path, name=name, attachment_type=allure.attachment_type.PNG
        )

    def fill_input(self, locator: str, text: str) -> None:
        """Fill an input field with specified text.

        Args:
            locator (str): The locator string to find the input element.
            text (str): The text to fill into the input field.
        """
        self.page.fill(locator, text)
        allure.attach(
            name="Input Filled",
            body=f"Filled input '{locator}' with text: {text}",
        )

    def click_element(self, locator: str) -> None:
        """Click on an element specified by the locator.

        Args:
            locator (str): The locator string to find the element to click.
        """
        self.page.click(locator)
        allure.attach(
            name="Element Clicked",
            body=f"Clicked on element '{locator}'",
        )

    def get_element_text(self, locator: str) -> str:
        """Get the text content of an element.

        Args:
            locator (str): The locator string to find the element.

        Returns:
            str: The text content of the element.
        """
        text = self.page.locator(locator).inner_text()
        allure.attach(
            name="Element Text Retrieved",
            body=f"Text of element '{locator}': {text}",
        )
        return text

    def wait_for_element(self, locator: str, timeout: int = 5000) -> None:
        """Wait for an element to be visible on the page.

        Args:
            locator (str): The locator string to find the element.
            timeout (int): Maximum wait time in milliseconds. Default is 5000ms.
        """
        self.page.wait_for_selector(locator, state="visible", timeout=timeout)
        allure.attach(
            name="Element Waited",
            body=f"Waited for element '{locator}' to be visible within {timeout}ms",
        )

    def refresh_page(self) -> None:
        """Refresh the current page."""
        self.page.reload()
        allure.attach(name="Page Refreshed", body="The page has been refreshed.")

    def go_back(self) -> None:
        """Navigate back to the previous page."""
        self.page.go_back()
        allure.attach(
            name="Navigated Back", body="Navigated back to the previous page."
        )

    def go_forward(self) -> None:
        """Navigate forward to the next page."""
        self.page.go_forward()
        allure.attach(
            name="Navigated Forward", body="Navigated forward to the next page."
        )

    def get_current_url(self) -> str:
        """Get the current page URL.

        Returns:
            str: The current URL of the page.
        """
        current_url = self.page.url
        allure.attach(name="Current URL", body=current_url)
        return current_url

    def clear_input(self, locator: str) -> None:
        """Clear the text from an input field.

        Args:
            locator (str): The locator string to find the input element.
        """
        self.page.fill(locator, "")
        allure.attach(
            name="Input Cleared",
            body=f"Cleared input field '{locator}'",
        )

    def hover_over_element(self, locator: str) -> None:
        """Hover over an element specified by the locator.

        Args:
            locator (str): The locator string to find the element to hover over.
        """
        self.page.hover(locator)
        allure.attach(
            name="Element Hovered",
            body=f"Hovered over element '{locator}'",
        )

    def scroll_to_element(self, locator: str) -> None:
        """Scroll to an element specified by the locator.

        Args:
            locator (str): The locator string to find the element to scroll to.
        """
        self.page.locator(locator).scroll_into_view_if_needed()
        allure.attach(
            name="Scrolled to Element",
            body=f"Scrolled to element '{locator}'",
        )

    def select_option(self, locator: str, value: str) -> None:
        """Select an option from a dropdown or select element.

        Args:
            locator (str): The locator string to find the select element.
            value (str): The value of the option to select.
        """
        self.page.select_option(locator, value)
        allure.attach(
            name="Option Selected",
            body=f"Selected option '{value}' from element '{locator}'",
        )

    def get_element_count(self, locator: str) -> int:
        """Get the count of elements matching the locator.

        Args:
            locator (str): The locator string to find the elements.

        Returns:
            int: The count of matching elements.
        """
        count = self.page.locator(locator).count()
        allure.attach(
            name="Element Count",
            body=f"Count of elements matching '{locator}': {count}",
        )
        return count

    def clear_cookies(self) -> None:
        """Clear all cookies for the current page."""
        self.page.context.clear_cookies()
        allure.attach(name="Cookies Cleared", body="All cookies have been cleared.")

    def set_cookie(self, name: str, value: str) -> None:
        """Set a cookie for the current page.

        Args:
            name (str): The name of the cookie.
            value (str): The value of the cookie.
        """
        self.page.context.add_cookies(
            [{"name": name, "value": value, "url": self.page.url}]
        )
        allure.attach(
            name="Cookie Set", body=f"Set cookie '{name}' with value '{value}'."
        )

    def get_cookies(self) -> list:
        """Get all cookies for the current page.

        Returns:
            list: A list of cookies.
        """
        cookies = self.page.context.cookies()
        allure.attach(name="Cookies Retrieved", body=str(cookies))
        return cookies

    def wait_for_timeout(self, timeout: int) -> None:
        """Wait for a specified timeout.

        Args:
            timeout (int): Time to wait in milliseconds.
        """
        self.page.wait_for_timeout(timeout)
        allure.attach(name="Waited", body=f"Waited for {timeout} milliseconds.")

    def clear_and_fill_input(self, locator: str, text: str) -> None:
        """Clear an input field and fill it with specified text.

        Args:
            locator (str): The locator string to find the input element.
            text (str): The text to fill into the input field.
        """
        self.page.fill(locator, "")
        self.page.fill(locator, text)
        allure.attach(
            name="Input Cleared and Filled",
            body=f"Cleared and filled input '{locator}' with text: {text}",
        )

    def double_click_element(self, locator: str) -> None:
        """Double click on an element specified by the locator.

        Args:
            locator (str): The locator string to find the element to double click.
        """
        self.page.dblclick(locator)
        allure.attach(
            name="Element Double Clicked",
            body=f"Double clicked on element '{locator}'",
        )

    def right_click_element(self, locator: str) -> None:
        """Right click on an element specified by the locator.

        Args:
            locator (str): The locator string to find the element to right click.
        """
        self.page.click(locator, button="right")
        allure.attach(
            name="Element Right Clicked",
            body=f"Right clicked on element '{locator}'",
        )

    def type_text(self, locator: str, text: str, delay: int = 0) -> None:
        """Type text into an input field with an optional delay between keystrokes.

        Args:
            locator (str): The locator string to find the input element.
            text (str): The text to type into the input field.
            delay (int): Delay in milliseconds between each keystroke. Default is 0.
        """
        self.page.type(locator, text, delay=delay)
        allure.attach(
            name="Text Typed",
            body=f"Typed text '{text}' into input '{locator}' with delay {delay}ms",
        )

    def press_key(self, locator: str, key: str) -> None:
        """Press a specific key on an element.

        Args:
            locator (str): The locator string to find the element.
            key (str): The key to press (e.g., 'Enter', 'Tab').
        """
        self.page.press(locator, key)
        allure.attach(
            name="Key Pressed",
            body=f"Pressed key '{key}' on element '{locator}'",
        )

    def clear_and_type(self, locator: str, text: str, delay: int = 0) -> None:
        """Clear an input field and type text into it with an optional delay.

        Args:
            locator (str): The locator string to find the input element.
            text (str): The text to type into the input field.
            delay (int): Delay in milliseconds between each keystroke. Default is 0.
        """
        self.page.fill(locator, "")
        self.page.type(locator, text, delay=delay)
        allure.attach(
            name="Input Cleared and Typed",
            body=f"Cleared and typed text '{text}' into input '{locator}' with delay {delay}ms",
        )

    def wait_for_element_hidden(self, locator: str, timeout: int = 5000) -> None:
        """Wait for an element to be hidden on the page.

        Args:
            locator (str): The locator string to find the element.
            timeout (int): Maximum wait time in milliseconds. Default is 5000ms.
        """
        self.page.wait_for_selector(locator, state="hidden", timeout=timeout)
        allure.attach(
            name="Element Hidden Waited",
            body=f"Waited for element '{locator}' to be hidden within {timeout}ms",
        )

    def is_element_enabled(self, locator: str) -> bool:
        """Check if an element is enabled on the page.

        Args:
            locator (str): The locator string to find the element.

        Returns:
            bool: True if the element is enabled, False otherwise.
        """
        allure.attach(
            name="Element Enabled Check",
            body=f"Checked if element '{locator}' is enabled",
        )
        return self.page.locator(locator).is_enabled()

    def is_element_disabled(self, locator: str) -> bool:
        """Check if an element is disabled on the page.

        Args:
            locator (str): The locator string to find the element.

        Returns:
            bool: True if the element is disabled, False otherwise.
        """
        allure.attach(
            name="Element Disabled Check",
            body=f"Checked if element '{locator}' is disabled",
        )
        return self.page.locator(locator).is_disabled()

    def get_element_attribute(self, locator: str, attribute: str) -> str:
        """Get the value of a specific attribute from an element.

        Args:
            locator (str): The locator string to find the element.
            attribute (str): The name of the attribute to retrieve.

        Returns:
            str: The value of the attribute, or an empty string if not found.
        """
        allure.attach(
            name="Element Attribute Retrieved",
            body=f"Retrieved attribute '{attribute}' from element '{locator}'",
        )
        return self.page.locator(locator).get_attribute(attribute) or ""

    def get_element_value(self, locator: str) -> str:
        """Get the value of an input element.

        Args:
            locator (str): The locator string to find the input element.

        Returns:
            str: The value of the input element.
        """
        value = self.page.locator(locator).input_value()
        allure.attach(
            name="Element Value Retrieved",
            body=f"Value of input element '{locator}': {value}",
        )
        return value

    def clear_cookies_and_local_storage(self) -> None:
        """Clear all cookies and local storage for the current page."""
        self.page.context.clear_cookies()
        self.page.evaluate("() => localStorage.clear()")
        allure.attach(
            name="Cookies and Local Storage Cleared",
            body="All cookies and local storage have been cleared.",
        )

    def execute_script(self, script: str, *args) -> bool:
        """Execute a custom JavaScript script on the page.

        Args:
            script (str): The JavaScript code to execute.
            *args: Optional arguments to pass to the script.

        Returns:
            any: The result of the script execution.
        """
        result = self.page.evaluate(script, *args)
        allure.attach(
            name="Script Executed",
            body=f"Executed script: {script} with args: {args}. Result: {result}",
        )
        return result

    def reload_page(self) -> None:
        """Reload the current page."""
        self.page.reload()
        allure.attach(name="Page Reloaded", body="The page has been reloaded.")

    def wait_for_load_state(
        self,
        state: Literal["load", "domcontentloaded", "networkidle"],
        timeout: int = 5000,
    ) -> None:
        """Wait for the page to reach a specific load state.

        Args:
            state (str): The load state to wait for ('load', 'domcontentloaded', 'networkidle').
            timeout (int): Maximum wait time in milliseconds. Default is 5000ms.
        """
        self.page.wait_for_load_state(state=state, timeout=timeout)
        allure.attach(
            name="Load State Waited",
            body=f"Waited for page to reach load state '{state}' within {timeout}ms",
        )

    def take_full_page_screenshot(self, name: str = "full_page_screenshot") -> None:
        """Take a full-page screenshot of the current page state.

        Args:
            name (str): The name for the screenshot file.
        """
        screenshot_path = f"{name}.png"
        self.page.screenshot(path=screenshot_path, full_page=True)
        allure.attach.file(
            screenshot_path, name=name, attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            name="Full Page Screenshot Taken",
            body=f"Full page screenshot saved as '{screenshot_path}'",
        )

    def get_element_css_value(self, locator: str, property_name: str) -> str:
        """Get the value of a specific CSS property from an element.

        Args:
            locator (str): The locator string to find the element.
            property_name (str): The name of the CSS property to retrieve.

        Returns:
            str: The value of the CSS property.
        """
        value = self.page.locator(locator).evaluate(
            f"getComputedStyle(document.querySelector('{locator}')).getPropertyValue('{property_name}')"
        )
        allure.attach(
            name="Element CSS Value Retrieved",
            body=f"Value of CSS property '{property_name}' for element '{locator}': {value}",
        )
        return value

    def is_element_checked(self, locator: str) -> bool:
        """Check if a checkbox or radio button element is checked.

        Args:
            locator (str): The locator string to find the checkbox or radio button element.

        Returns:
            bool: True if the element is checked, False otherwise.
        """
        is_checked = self.page.locator(locator).evaluate("element => element.checked")
        allure.attach(
            name="Element Checked State Retrieved",
            body=f"Element '{locator}' checked state: {is_checked}",
        )
        return is_checked

    def check_element(self, locator: str) -> None:
        """Check a checkbox or radio button element.

        Args:
            locator (str): The locator string to find the checkbox or radio button element.
        """
        self.page.check(locator)
        allure.attach(
            name="Element Checked",
            body=f"Checked element '{locator}'",
        )

    def uncheck_element(self, locator: str) -> None:
        """Uncheck a checkbox element.

        Args:
            locator (str): The locator string to find the checkbox element.
        """
        self.page.uncheck(locator)
        allure.attach(
            name="Element Unchecked",
            body=f"Unchecked element '{locator}'",
        )

    def drag_and_drop(self, source_locator: str, target_locator: str) -> None:
        """Drag an element from source to target.

        Args:
            source_locator (str): The locator string to find the source element.
            target_locator (str): The locator string to find the target element.
        """
        self.page.drag_and_drop(source_locator, target_locator)
        allure.attach(
            name="Element Dragged and Dropped",
            body=f"Dragged element '{source_locator}' and dropped on '{target_locator}'",
        )

    def expect_element_text(self, locator: str, expected_text: str) -> None:
        """Assert that an element contains the expected text.

        Args:
            locator (str): The locator string to find the element.
            expected_text (str): The expected text to compare against the element's content.
        """
        expect(self.page.locator(locator)).to_have_text(expected_text)
        allure.attach(
            name="Element Text Assertion",
            body=f"Element '{locator}' contains expected text: '{expected_text}'",
        )

    def expect_element_visible(self, locator: str) -> None:
        """Assert that an element is visible on the page.

        Args:
            locator (str): The locator string to find the element.
        """
        expect(self.page.locator(locator)).to_be_visible()
        allure.attach(
            name="Element Visibility Assertion",
            body=f"Element '{locator}' is visible on the page",
        )

    def expect_element_hidden(self, locator: str) -> None:
        """Assert that an element is hidden on the page.

        Args:
            locator (str): The locator string to find the element.
        """
        expect(self.page.locator(locator)).to_be_hidden()
        allure.attach(
            name="Element Hidden Assertion",
            body=f"Element '{locator}' is hidden on the page",
        )

    def expect_element_enabled(self, locator: str) -> None:
        """Assert that an element is enabled on the page.

        Args:
            locator (str): The locator string to find the element.
        """
        expect(self.page.locator(locator)).to_be_enabled()
        allure.attach(
            name="Element Enabled Assertion",
            body=f"Element '{locator}' is enabled on the page",
        )

    def expect_element_disabled(self, locator: str) -> None:
        """Assert that an element is disabled on the page.

        Args:
            locator (str): The locator string to find the element.
        """
        expect(self.page.locator(locator)).to_be_disabled()
        allure.attach(
            name="Element Disabled Assertion",
            body=f"Element '{locator}' is disabled on the page",
        )

    def is_element_present(self, locator: str) -> bool:
        """Check if an element is present in the DOM.

        Args:
            locator (str): The locator string to find the element.

        Returns:
            bool: True if the element is present, False otherwise.
        """
        allure.attach(
            name="Element Presence Check",
            body=f"Checking presence of element '{locator}' in the DOM",
        )
        return self.page.locator(locator).count() > 0

    def is_element_interactable(self, locator: str) -> bool:
        """Check if an element is interactable (visible and enabled) on the page.

        Args:
            locator (str): The locator string to find the element.

        Returns:
            bool: True if the element is interactable, False otherwise.
        """
        allure.attach(
            name="Element Interactivity Check",
            body=f"Checking interactivity of element '{locator}' on the page",
        )
        return (
            self.page.locator(locator).count() > 0
            and self.page.locator(locator).is_visible()
            and self.page.locator(locator).is_enabled()
        )
