import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setting_browser():
    browser.config.window_height = 1080  # Height of browser's window
    browser.config.window_width = 1920  # Width of browser's window
    yield
    browser.quit()  # Close browser
    print('Browser is closed!')
