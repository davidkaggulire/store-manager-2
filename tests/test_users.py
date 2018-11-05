"""
module test_users
"""

import json
from . import ADMIN_USER, LOGIN_ADMIN, USER, LOGIN_USER
from tests.base_test import TestBase


class TestUsers(TestBase):
    """
    class that tests routes
    """

    def test_creating_admin(self):
        """test method to post product if admin"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        self.assertEqual(response.status_code, 201)

    def test_creating_user(self):
        """test method to post product if attendant"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        headers = {'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']}
        response = self.client.post('/api/v2/auth/signup', headers, data=json.dumps(USER))
        msg = json.loads(response.data.decode())
        self.assertIn('User created successfully', msg['message'])
        self.assertEqual(response.status_code, 201)

    def test_login_admin_user(self):
        """test method to login admin_user"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        self.assertIn('User successfully logged in', msg['message'])
        self.assertEqual(response.status_code, 201)

    def test_login_wrong_admin_user(self):
        """test method to check wrong_admin"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_USER))
        msg = json.loads(response.data.decode())
        self.assertIn('Wrong username or password, try again', msg['error'])
        self.assertEqual(response.status_code, 401)
