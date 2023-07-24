# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.post_book_request import PostBookRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestBookController(BaseTestCase):
    """BookController integration test stubs"""

    def test_delete_book_info(self):
        """Test case for delete_book_info

        delete book info
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/books/{book_id}'.format(book_id='book_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_book_info(self):
        """Test case for get_book_info

        get book info
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/books/{book_id}'.format(book_id='book_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_book_info(self):
        """Test case for patch_book_info

        patch book info
        """
        post_book_request = openapi_server.PostBookRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v0/books/{book_id}'.format(book_id='book_id_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(post_book_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_book(self):
        """Test case for post_book

        post book info
        """
        post_book_request = openapi_server.PostBookRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v0/books',
            method='POST',
            headers=headers,
            data=json.dumps(post_book_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
