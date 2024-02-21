import pytest
from playwright.sync_api import Page
import os


@pytest.fixture(autouse=True)
def set_up(page: Page):
    page.set_default_timeout(5000)
    yield page
    page.close()


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "record_video_dir": "videos/"}


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "record_video_dir": "videos/"}


@pytest.fixture(scope="function")
def page_with_screenshot_on_failure(page, request):
    page.set_default_timeout(5000)
    yield page
    if request.node.rep_call.failed:
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
        page.screenshot(path=f"screenshots/{request.node.nodeid.replace('/', '_').replace(':', '_').replace('[', '_').replace(']', '_')}.png")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        setattr(item, "rep_call", report)
