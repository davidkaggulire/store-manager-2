"""
module test_users
"""

import unittest
import json
from api.models.db import Database
from api import create_app
from . import ADMIN_USER, LOGIN_ADMIN, USER, PRODUCT, EMPTY_PRODUCT, LOGIN_USER
from tests.base_test import TestBase

class TestUsers(TestBase):
    """
    class that tests routes
    """

    def test_creating_admin(self):
        """test method to post product if admin"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        data=json.dumps(ADMIN_USER))
        self.assertEqual(response.status_code, 201)

    def test_creating_user(self):
        """test method to post product if attendant"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json',
        data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        print(token)
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER),
        headers = {'content_type': 'application/json', 'Authorization': "Bearer "+ token['auth_token']})
        msg = json.loads(response.data.decode())
        self.assertIn('User created successfully', msg['message'])
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        """test method to post product if attendant"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json',
        data=json.dumps(USER))
        self.assertEqual(response.status_code, 401)

