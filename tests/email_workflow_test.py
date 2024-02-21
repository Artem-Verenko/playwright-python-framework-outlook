import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.outlook_main_page import OutlookMainPage
from pages.send_massage_form import SendMassageForm
from pages.sent_items_page import SentItemsPage
from pages.start_advertising_page import StartAdvertisingPage


class TestEmailWorkflow:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.start_advertising_page = StartAdvertisingPage(page)
        self.login_page = LoginPage(page)
        self.outlook_main_page = OutlookMainPage(page)
        self.send_massage_form = SendMassageForm(page)
        self.sent_items_page = SentItemsPage(page)

    @pytest.mark.regression
    def test_send_verify_and_delete_email(self, page_with_screenshot_on_failure):
        page = page_with_screenshot_on_failure
        page.goto(self.start_advertising_page.BASE_URL)
        self.start_advertising_page.sign_in_button_locator.click()
        self.login_page.login("TestUserArtemV@outlook.com", "!@#qwe#@!")
        expect(self.outlook_main_page.account_manager_locator).to_be_visible()
        self.outlook_main_page.new_massage_locator.click()
        self.send_massage_form.send_massage("artem.verenco@gmail.com", "Test massage", "test")
        self.outlook_main_page.sent_items_locator.click()
        self.sent_items_page.verify_test_email()

