from playwright.sync_api import Page


class OutlookMainPage:
    def __init__(self, page: Page):
        self.page = page
        self.account_manager_locator = page.get_by_label("Account manager for Artem V")