# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.auth_login_request import AuthLoginRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_auth_login(self):
        """Test case for auth_login

        Returns me
        """
        auth_login_request = openapi_server.AuthLoginRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/api/v3/auth/login',
            method='POST',
            headers=headers,
            data=json.dumps(auth_login_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_logout(self):
        """Test case for auth_logout

        logout
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3/auth/logout',
            method='PATCH',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_me(self):
        """Test case for auth_me

        Returns me
        """
        headers = { 
            'Accept': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/api/v3/auth/me',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
