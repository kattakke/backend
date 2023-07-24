# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.auth_login_request import AuthLoginRequest  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_delete_user_info(self):
        """Test case for delete_user_info

        delete user info
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3/users/{user_id}'.format(user_id='user_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_info(self):
        """Test case for get_user_info

        get user info
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3/users/{user_id}'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_shelf(self):
        """Test case for get_user_shelf

        get user shelf
        """
        query_string = [('title', 'title_example'),
                        ('tag', 'tag_example'),
                        ('isbn', 'isbn_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3/users/{user_id}/shelf'.format(user_id='user_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_user_info(self):
        """Test case for patch_user_info

        patch user info
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3/users/{user_id}'.format(user_id='user_id_example'),
            method='PATCH',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_register(self):
        """Test case for user_register

        register
        """
        auth_login_request = openapi_server.AuthLoginRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3/users',
            method='POST',
            headers=headers,
            data=json.dumps(auth_login_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
