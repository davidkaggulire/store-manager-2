"""
module test_users
"""

import unittest
from api.models.db import Database
from api import create_app


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

    def tearDown(self):
        self.db.drop_table_products()
        self.db.drop_table_sales()
        self.db.drop_table_user()


if __name__ == '__main__':
    unittest.main()
