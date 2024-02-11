import pytest
from selene import browser, be, have


@pytest.fixture(scope="function")
def open_browser(setting_browser):
    browser.open('https://google.com')  # Open browser
    print('Browser is opened!')


def test_find_success(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_find_nothing(open_browser):
    browser.element('[name="q"]').should(be.blank).type('d\gfbnjg3').press_enter()
    browser.element('[id="botstuff"]').should(have.text('ничего не найдено'))
