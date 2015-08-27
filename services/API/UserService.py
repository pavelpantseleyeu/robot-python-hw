from bo.Users import UserBuilder
from libs.APIUserLib import UserAPI


class UserService():

    def __init__(self):
        pass

    def create_user_api(self, user=None):
        if user is None:
            user = UserBuilder().get_default_user()
        return UserAPI.create_user(user)

    def delete_user_api(self, user):
        return UserAPI.delete_user(user)