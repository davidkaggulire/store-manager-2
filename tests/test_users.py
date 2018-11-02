"""
module test_users
"""

import unittest
import json
from api.models.db import Database
from api import create_app
from . import ADMIN_USER, LOGIN_ADMIN, USER, PRODUCT, EMPTY_PRODUCT, LOGIN_USER
from tests.base_test import BaseTest

class TestingUsers(BaseTest):
    """
    class that tests routes
    """
  
    def setUp(self):
        """
        setting up test data 
        """ 
        app = create_app("testing")
        self.client = app.test_client()
        self.db = Database()
        self.db.create_products_table()
        self.db.create_sales_table()
        self.db.create_user_table()

    def test_creating_admin(self):
        """test method to post product if admin"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        data=json.dumps(ADMIN_USER))
        self.assertEqual(response.status_code, 201)

    def test_creating_user(self):
        """test method to post product if attendant"""
        response = self.client.post('/api/v2/auth/signup', content_type='application/json',
        data=json.dumps(USER))
        self.assertEqual(response.status_code, 401)

    def test_login_user(self):
        """test method to post product if attendant"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json',
        data=json.dumps(USER))
        self.assertEqual(response.status_code, 401)

    def tearDown(self):
       self.db.drop_table_products()
       self.db.drop_table_sales()
       self.db.drop_table_user()
if __name__ == '__main__':
    unittest.main()
    