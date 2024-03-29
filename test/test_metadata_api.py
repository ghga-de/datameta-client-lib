"""
    DataMeta

    DataMeta  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: leon.kuchenbecker@uni-tuebingen.de
    Generated by: https://openapi-generator.tech
"""


import unittest

import datameta_client_lib
from datameta_client_lib.api.metadata_api import MetadataApi  # noqa: E501


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_meta_data_set(self):
        """Test case for create_meta_data_set

        Create a New MetaDataSet  # noqa: E501
        """
        pass

    def test_create_meta_datum(self):
        """Test case for create_meta_datum

        Create a New MetaDatum  # noqa: E501
        """
        pass

    def test_delete_metadata_set(self):
        """Test case for delete_metadata_set

        Delete Not-Submitted Metadataset  # noqa: E501
        """
        pass

    def test_get_meta_data(self):
        """Test case for get_meta_data

        Get metadata definitions  # noqa: E501
        """
        pass

    def test_get_meta_data_set(self):
        """Test case for get_meta_data_set

        Get Details for a MetaDataSet  # noqa: E501
        """
        pass

    def test_get_meta_data_sets(self):
        """Test case for get_meta_data_sets

        Query metadatasets  # noqa: E501
        """
        pass

    def test_update_meta_datum(self):
        """Test case for update_meta_datum

        Update a MetaDatum  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
