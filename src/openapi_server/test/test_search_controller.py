# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.post_book_request import PostBookRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSearchController(BaseTestCase):
    """SearchController integration test stubs"""

    def test_get_search_book(self):
        """Test case for get_search_book

        search book
        """
        query_string = [('title', 'title_example'),
                        ('isbn', 'isbn_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/search',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
