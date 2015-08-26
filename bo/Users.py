from utils import RandomUtils


class User():
    def __init__(self, login, password, email, first_name, last_name, account_id):
        self.login = login
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password


class UserBuilder(object):

    LOGIN = RandomUtils.get_random_string()
    PASSWORD = RandomUtils.get_random_string()
    INVALID_PASSWORD = RandomUtils.get_random_string()
    EMAIL = LOGIN + '@clarabridge.net'
    FIRST_NAME = 'First Name' + LOGIN
    LAST_NAME = 'Last Name' + LOGIN
    ACCOUNT_ID = 0

    @staticmethod
    def get_default_user(login=LOGIN, password=PASSWORD, email=EMAIL, first_name=FIRST_NAME, last_name=LAST_NAME,
                         account_id=ACCOUNT_ID):
        user = User(login, password, email, first_name, last_name, account_id)
        return user

    @staticmethod
    def get_user_with_invalid_password(invalid_password=INVALID_PASSWORD):
        user = UserBuilder.get_default_user()
        user.set_password(invalid_password)
        return user