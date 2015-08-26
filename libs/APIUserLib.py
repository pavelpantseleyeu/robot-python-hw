from Utils import CmpUtils
import json
import requests
from globalConfig.GlobalConfig import GlobalConfig


class UserAPI(CmpUtils):
    def create_user(self, user):

        """Executes the create user method of the User API Service
        The Create User method allows creating a user account with specified parameters.
        It returns the user with added userId on successful creation, fails when the requested user is not created.

        """

        url = self._get_url('http://{host}:{port}/mobile/rest/users', GlobalConfig.get_test_environment().host,
                            GlobalConfig.get_test_environment().port)
        headers = {'Content-Type': 'application/json'}
        payload = {
            'login': user.login,
            'password': user.password,
            'email': user.email,
            'firstName': user.firstName,
            'lastName': user.lastName,
            'enabled': user.enabled,
            'accountAdmin': user.accountAdmin,
            'liteUser': user.liteUser,
            'engageUser': user.engageUser,
            'accountId': user.accountId,
            'company': user.company,
            'jobTitle': user.jobTitle,
            'phone': user.phone,
            'address1': user.address1,
            'address2': user.address2,
            'country': user.country,
            'state': user.state,
            'zip': user.zip,
            'collaborateLogin': user.collaborateLogin,
            'autoRefreshEnabled': user.autoRefreshEnabled,
            'autoRefreshInterval': user.autoRefreshInterval
        }

        r = requests.put(url, data=json.dumps(payload),
                         auth=(GlobalConfig.get_test_environment().user, GlobalConfig.get_test_environment().password),
                         headers=headers)

        if r.status_code == 201:
            resp = r.json()
            user.userId = resp["userId"]
            return user
        raise Exception("Error Code, %i %s" % (r.status_code, r.text))

    def delete_user(self, user):
        """
        The Delete User method allows deleting a user by specified userId. It returns the status of user deletion.

        """
        url = self._get_url('http://{host}:{port}/mobile/rest/users/', GlobalConfig.get_test_environment().host,
                            GlobalConfig.get_test_environment().port)
        url += str(user.userId)

        r = requests.delete(url, auth=(GlobalConfig.get_test_environment().user,
                                       GlobalConfig.get_test_environment().password))

        if r.status_code == 202:
            resp = r.json()
            return resp["status"]

        raise Exception("Error Code, %i %s" % (r.status_code, r.text))