import pytest
from playwright.sync_api import Page, expect

from pages.start_advertising_page import StartAdvertisingPage


class TestLendingPageVisual:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.start_advertising_page = StartAdvertisingPage(page)

    def test_visual_lending(self, page, assert_snapshot):
        page.goto('https://outlook.live.com/')
        expect(self.start_advertising_page.sign_in_button_locator).to_be_visible()
        assert_snapshot(page.screenshot())




