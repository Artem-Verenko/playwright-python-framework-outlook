

class SentItemsPage:
    def __init__(self, page):
        self.page = page
        self.select_a_conversation_locator = page.get_by_label("Select a conversation")
        self.delete_button_locator = page.get_by_title("Delete", exact=True)
        self.ok_button_locator = page.locator("svg").nth(3)
        self.nothing_in_sent_label_locator = page.get_by_text("Nothing in Sent")

    def verify_test_email(self):
        self.select_a_conversation_locator.click()
        self.page.wait_for_timeout(1000)
        self.delete_button_locator.click()
        self.page.wait_for_timeout(2000)
        try:
            self.ok_button_locator.click()
        except:
            pass

