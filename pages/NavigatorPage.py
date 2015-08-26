from globalConfig.GlobalConfig import GlobalConfig
from ui.Browser import Browser

USER_FIRST_NAME_LOCATOR = "//div[@id='GButtonUserMenu']"


def get_user_first_name():
    user_first_name = Browser.get_test_from_element(USER_FIRST_NAME_LOCATOR)
    return user_first_name


class NavigatorPage(object):
    def __init__(self):
        self.user_first_name = get_user_first_name()