import unittest
import json
from api.models.db import Database
from api import create_app

class TestDatabase(unittest.TestCase):
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

    def test_create_admin(self):
        """test to create admin"""
        self.db.create_admin('don', 'kaggulire', 'don', 'don1234!')
        find_user = self.db.check_username('don')
        self.assertEqual(find_user['username'], 'don')

    def test_create_user(self):
        """test to create user"""
        self.db.create_admin('david', 'kaggulire', 'dkaggs', 'dkaggs123!')
        find_user = self.db.check_username('dkaggs')
        self.assertEqual(find_user['username'], 'dkaggs')

    def test_create_product(self):
        """create product"""
        self.db.create_product('book', 'scholastic', 1000, 2, 1)
        find_product = self.db.check_product_name('book')
        self.assertEqual(find_product['product_name'], 'book')

    def test_get_all_products(self):
        """get all products"""
        self.db.create_product('book', 'scholastic', 1000, 2, 1)
        self.db.create_product('pen', 'scholastic', 500, 2, 1)
        get_all = self.db.get_products()
        self.assertIsInstance(get_all, list)

    def test_get_product(self):
        """get_single_product"""
        self.db.create_product('book', 'scholastic', 1000, 2, 1) 
        get_one = self.db.get_single_product(1)
        self.assertIsInstance(get_one, tuple)

    def test_update_product(self):
        """update_product_test"""
        self.db.create_product('book', 'scholastic', 1000, 2, 1)
        self.db.update_product(1, 'pen', 'scholastic', 500, 1, 1)
        find_product = self.db.check_product_name('pen')
        self.assertEqual(find_product['product_name'], 'pen')
    
    def test_delete_product(self):
        """test for deleting product"""
        self.db.create_product('book', 'scholastic', 1000, 2, 1)
        self.db.get_single_product(1)
        delete = self.db.delete_product(1)
        self.db.check_product_name('book')
        self.assertIs(delete, None)

    def test_make_sale(self):
        """test for checking a sale"""
        self.db.create_sale('book', 2, 2000, 2, 1)
        get_sale = self.db.get_single_sale(1)
        self.assertEqual(get_sale[1], 'book')

    def test_sale_dict(self):
        """testing for getting one singlesale"""
        self.db.create_sale('book', 2, 2000, 2, 1)
        get_sale = self.db.get_single_sale(1)
        self.assertIsInstance(get_sale, tuple)

    def test_get_many_sale(self):
        """testing for many sales"""
        self.db.create_sale('book', 2, 2000, 2, 1)
        self.db.create_sale('pen', 2, 200, 2, 1)
        get_all_sales = self.db.get_sales()
        self.assertIsInstance(get_all_sales, list)

    def tearDown(self):
        self.db.drop_table_products()
        self.db.drop_table_sales()
        self.db.drop_table_user()

if __name__ == '__main__':
    unittest.main()
    