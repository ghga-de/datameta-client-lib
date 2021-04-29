"""
    DataMeta

    DataMeta  # noqa: E501

    The version of the OpenAPI document: 0.14.0
    Contact: leon.kuchenbecker@uni-tuebingen.de
    Generated by: https://openapi-generator.tech
"""


import unittest

import datameta_client_lib
from datameta_client_lib.api.remote_procedure_calls_api import RemoteProcedureCallsApi  # noqa: E501


class TestRemoteProcedureCallsApi(unittest.TestCase):
    """RemoteProcedureCallsApi unit test stubs"""

    def setUp(self):
        self.api = RemoteProcedureCallsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bulk_delete_staged_files(self):
        """Test case for bulk_delete_staged_files

        Bulk-delete Staged Files  # noqa: E501
        """
        pass

    def test_bulk_delete_staged_meta_data_sets(self):
        """Test case for bulk_delete_staged_meta_data_sets

        Bulk-delete Staged MetaDataSets  # noqa: E501
        """
        pass

    def test_get_user_information(self):
        """Test case for get_user_information

        [Not RESTful]: Returns information about the authenticated user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
