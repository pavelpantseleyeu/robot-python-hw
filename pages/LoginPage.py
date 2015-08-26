from globalConfig.GlobalConfig import GlobalConfig
from ui.Browser import Browser

USERNAME_TEXTBOX_LOCATOR = "//input[@id='j_username']"
PASSWORD_TEXTBOX_LOCATOR = "//input[@id='j_password']"
LOGIN_BUTTON_LOCATOR = "//button[@type='submit']"
LOGIN_ERROR_MESSAGE_LOCATOR = "//font[@color='red']"


def open_login_page():
    Browser.open(GlobalConfig.LOGIN_URL)


def login_in(user):
    Browser.type(USERNAME_TEXTBOX_LOCATOR, user.login)
    Browser.type(PASSWORD_TEXTBOX_LOCATOR, user.password)
    Browser.submit(LOGIN_BUTTON_LOCATOR)


def is_login_error_message_present():
    return Browser.is_present(LOGIN_ERROR_MESSAGE_LOCATOR)