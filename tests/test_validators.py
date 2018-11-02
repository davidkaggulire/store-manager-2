"""
module test_users
"""

import unittest
import json
from api.validators import Validators
from api import create_app
from . import USER, PRODUCT, LOGIN_USER, ADMIN_USER

class TestValidators(unittest.TestCase):
    """
    class that tests routes
    """
  
    def setUp(self):
        """
        setting up test data 
        """ 
        app = create_app("testing")
        self.client = app.test_client()
        self.validate = Validators()

    def test_validate_product(self):
        """test to ensure correct data"""
        self.assertEqual(self.validate.validate_input_number(PRODUCT['price']), None)
       
if __name__ == '__main__':
    unittest.main()
    