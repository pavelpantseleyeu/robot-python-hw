def bb28():
    return TestEnvironment('http://', 'blackbox28.clarabridge.net', '80', 'admin', 'admin')


class GlobalConfig():
    def __init__(self):
        pass

    @staticmethod
    def get_test_environment():
        return bb28()

    PAGE_LOAD_TIMEOUT = 30
    IMPLYCITLY_WAIT = 30
    BROWSER = 'Firefox'
    LOGIN_URL = get_test_environment().protocol + get_test_environment().host + ':' + get_test_environment().port + "/cmp/login"


class TestEnvironment():
    def __init__(self, protocol, host, port, user, password):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.user = user
        self.password = password