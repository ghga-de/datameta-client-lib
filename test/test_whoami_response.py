"""
    DataMeta

    DataMeta  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: leon.kuchenbecker@uni-tuebingen.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import datameta_client_lib
from datameta_client_lib.model.identifier import Identifier
from datameta_client_lib.model.whoami_response_group import WhoamiResponseGroup
globals()['Identifier'] = Identifier
globals()['WhoamiResponseGroup'] = WhoamiResponseGroup
from datameta_client_lib.model.whoami_response import WhoamiResponse


class TestWhoamiResponse(unittest.TestCase):
    """WhoamiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWhoamiResponse(self):
        """Test WhoamiResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WhoamiResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
