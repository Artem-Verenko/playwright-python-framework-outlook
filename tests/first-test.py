from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.microsoft.com/en-us/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook?deeplink=%2fowa%2f&sdf=0")
    page.get_by_label("Sign in to your account").click()
    page.get_by_placeholder("Email, phone, or Skype").click()
    page.get_by_placeholder("Email, phone, or Skype").fill("TestUserArtemV@outlook.com")
    page.get_by_role("button", name="Next").click()
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("!@#qwe#@!")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="No").click()
    page.get_by_text("Inbox").first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
