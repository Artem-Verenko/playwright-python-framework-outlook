from playwright.sync_api import Page


class OutlookMainPage:
    def __init__(self, page: Page):
        self.page = page
        self.account_manager_locator = page.locator("#meInitialsButton")
        self.new_massage_locator = page.locator('button[aria-label="New mail"]')
        self.sent_items_locator = page.get_by_text("Sent Items")
