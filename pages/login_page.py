from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.login_field_locator = page.get_by_placeholder("Email, phone, or Skype")
        self.next_button_locator = page.get_by_role("button", name="Next")
        self.password_field_locator = page.get_by_placeholder("Password")
        self.sign_in_button_locator = page.get_by_role("button", name="Sign in")
        self.no_button_locator = page.get_by_role("button", name="No")
        self.invalid_password_message_locator = page.get_by_text("Your account or password is")
        self.invalid_email_message_locator = page.locator("#usernameError")

    def login(self, email: str, password: str):
        self.login_field_locator.click()
        self.login_field_locator.fill(email)
        self.next_button_locator.click()
        self.password_field_locator.click()
        self.password_field_locator.fill(password)
        self.sign_in_button_locator.click()
        self.no_button_locator.click()
        return self
