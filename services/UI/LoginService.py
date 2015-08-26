from bo.Users import UserBuilder
from pages import LoginPage
from pages import NavigatorPage


def login():
    LoginPage.open_login_page()
    LoginPage.login_in(UserBuilder.get_default_user())


def login_with_incorrect_password():
    LoginPage.open_login_page()
    LoginPage.login_in(UserBuilder.get_default_user(password='incorrect_password'))


def check_is_user_first_name_present():
    assert NavigatorPage.get_user_first_name() == UserBuilder.get_default_user().first_name, \
        'User first name is not presented'


def check_is_login_error_message_present():
    assert True == LoginPage.is_login_error_message_present(), 'Login Error message is not presented'
