"""
    DataMeta

    DataMeta  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: leon.kuchenbecker@uni-tuebingen.de
    Generated by: https://openapi-generator.tech
"""


import unittest

import datameta_client_lib
from datameta_client_lib.api.user_api import UserApi  # noqa: E501


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_registration_settings(self):
        """Test case for get_registration_settings

        Get details for the registration view  # noqa: E501
        """
        pass

    def test_post_registration(self):
        """Test case for post_registration

        Create a new user registration request  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
