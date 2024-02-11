from selene import browser, be, have


def test_find_success(setting_browser):
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_find_nothing(setting_browser):
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('d\gfbnjg3').press_enter()
    browser.element('[id="botstuff"]').should(have.text('ничего не найдено'))
