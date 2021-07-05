"""
    DataMeta

    DataMeta  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: leon.kuchenbecker@uni-tuebingen.de
    Generated by: https://openapi-generator.tech
"""


import unittest

import datameta_client_lib
from datameta_client_lib.api.files_api import FilesApi  # noqa: E501


class TestFilesApi(unittest.TestCase):
    """FilesApi unit test stubs"""

    def setUp(self):
        self.api = FilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_file(self):
        """Test case for create_file

        Create a New File  # noqa: E501
        """
        pass

    def test_delete_file(self):
        """Test case for delete_file

        Delete Not-Submitted File  # noqa: E501
        """
        pass

    def test_get_file(self):
        """Test case for get_file

        Get Details for A File  # noqa: E501
        """
        pass

    def test_update_file(self):
        """Test case for update_file

        Update File Details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
