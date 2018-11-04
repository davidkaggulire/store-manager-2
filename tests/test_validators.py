"""
module test_users
"""

import unittest
import re
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
        with app.app_context():    
            self.client = app.test_client()
            self.validate = Validators()

    def test_validate_product(self):
        
        """test to ensure correct data"""
        self.assertEqual(self.validate.validate_input_number(PRODUCT['price']), None)
        # self.assertRegex(self.validate.validate_input_number(str(PRODUCT['price'])), r'\d')
       
if __name__ == '__main__':
    unittest.main()
    