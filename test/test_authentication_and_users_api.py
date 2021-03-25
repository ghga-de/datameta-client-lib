"""
    DataMeta

    DataMeta  # noqa: E501

    The version of the OpenAPI document: 0.7.0
    Contact: leon.kuchenbecker@uni-tuebingen.de
    Generated by: https://openapi-generator.tech
"""


import unittest

import datameta_client_lib
from datameta_client_lib.api.authentication_and_users_api import AuthenticationAndUsersApi  # noqa: E501


class TestAuthenticationAndUsersApi(unittest.TestCase):
    """AuthenticationAndUsersApi unit test stubs"""

    def setUp(self):
        self.api = AuthenticationAndUsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_api_key(self):
        """Test case for create_api_key

        Create new API Key/Token  # noqa: E501
        """
        pass

    def test_delete_api_key(self):
        """Test case for delete_api_key

        Delete ApiKey by label  # noqa: E501
        """
        pass

    def test_get_user_api_keys(self):
        """Test case for get_user_api_keys

        All API keys for a user  # noqa: E501
        """
        pass

    def test_set_user_password(self):
        """Test case for set_user_password

        Update a user's password  # noqa: E501
        """
        pass

    def test_user_update_request(self):
        """Test case for user_update_request

        Update a user's credentials and status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
