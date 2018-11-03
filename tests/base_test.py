"""
module test_users
"""

import unittest
import json
from api.models.db import Database
from api import create_app
from . import ADMIN_USER, LOGIN_ADMIN, USER, PRODUCT, LOGIN_USER

class TestBase(unittest.TestCase):
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

    def login_user(self):
        """method to login a user"""
        response = self.client.post('/api/v2/login', content_type='application/json', 
        data=json.dumps(LOGIN_USER))
        reply = json.loads(response.data.decode())
        return reply

    def tearDown(self):
       self.db.drop_table_products()
       self.db.drop_table_sales()
       self.db.drop_table_user()
if __name__ == '__main__':
    unittest.main()
    