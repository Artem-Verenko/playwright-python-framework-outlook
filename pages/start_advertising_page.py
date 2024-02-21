from playwright.sync_api import Page


class StartAdvertisingPage:

    BASE_URL: str = "https://outlook.live.com/"

    def __init__(self, page: Page):
        self.page = page
        self.sign_in_button_locator = page.get_by_label("Sign in to your account")