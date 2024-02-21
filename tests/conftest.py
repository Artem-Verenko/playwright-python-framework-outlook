import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def set_up(page: Page):
    page.set_default_timeout(5000)
    yield page
    page.close()


