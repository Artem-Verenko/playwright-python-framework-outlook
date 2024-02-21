from playwright.sync_api import Page


class SendMassageForm:
    def __init__(self, page: Page):
        self.page = page
        self.to_field_locator = page.locator('div[aria-label="To"]')
        self.person_field_locator = page.locator('[class^="personaContainer"]')
        self.subject_field_locator = page.get_by_placeholder("Add a subject")
        self.message_body_field_locator = page.get_by_label("Message body, press Alt+F10")
        self.send_button_locator = page.get_by_title("Send (Ctrl+Enter)")

    def send_massage(self, email: str, subject: str, message: str):
        self.to_field_locator.click()
        self.to_field_locator.fill(email)
        self.person_field_locator.click()
        self.subject_field_locator.click()
        self.subject_field_locator.fill(subject)
        self.message_body_field_locator.click()
        self.message_body_field_locator.fill(message)
        self.send_button_locator.click()
        return self
