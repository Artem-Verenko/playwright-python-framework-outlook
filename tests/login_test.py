import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.outlook_main_page import OutlookMainPage
from pages.start_advertising_page import StartAdvertisingPage


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.start_advertising_page = StartAdvertisingPage(page)
        self.login_page = LoginPage(page)
        self.outlook_main_page = OutlookMainPage(page)

    @pytest.mark.smoke
    def test_valid_login(self, page_with_screenshot_on_failure):
        page = page_with_screenshot_on_failure
        page.goto(self.start_advertising_page.BASE_URL)
        self.start_advertising_page.sign_in_button_locator.click()
        self.login_page.login("TestUserArtemV@outlook.com", "!@#qwe#@!")
        expect(self.outlook_main_page.account_manager_locator).to_be_visible()

    @pytest.mark.smoke
    def test_invalid_password_login(self, page_with_screenshot_on_failure):
        page = page_with_screenshot_on_failure
        page.goto(self.start_advertising_page.BASE_URL)
        self.start_advertising_page.sign_in_button_locator.click()
        self.login_page.login_field_locator.click()
        self.login_page.login_field_locator.fill("wrong_email@")
        self.login_page.next_button_locator.click()
        page.wait_for_load_state()
        expect(self.login_page.invalid_email_message_locator).to_be_visible()
        self.login_page.login_field_locator.click()
        self.login_page.login_field_locator.fill("TestUserArtemV@outlook.com")
        self.login_page.next_button_locator.click()
        self.login_page.password_field_locator.click()
        self.login_page.password_field_locator.fill("invalid_password")
        self.login_page.sign_in_button_locator.click()
        page.wait_for_load_state()
        expect(self.login_page.invalid_password_message_locator).to_be_visible()
        self.login_page.password_field_locator.click()
        self.login_page.password_field_locator.fill("!@#qwe#@!")
        self.login_page.sign_in_button_locator.click()
        self.login_page.no_button_locator.click()
        expect(self.outlook_main_page.account_manager_locator).to_be_visible()

