"""
module test
"""

import unittest
import json
from api import app

class TestingApi(unittest.TestCase):
    """
    class that tests routes
    """
    def create_app(self):
        """initialize the app"""
        app.config.from_object('config.TestingConfig')
        return app

    def setUp(self):
        """
        setting up test data 
        """
        self.client = app.test_client()

        self.products = [
            {
                "product_name": "piano",
                "category": "keyboards",
                "price": 1000000,
                "quantity": 10,
                "minimum_quantity": 3,
            },
            {
                "product_name": "guitar",
                "category": "guitars",
                "price": 500000,
                "quantity": 10,
                "minimum_quantity": 2,
            }
        ]

        self.empty_product = {
            "product_name": "",
            "category": "",
            "price": "",
            "quantity": "",
            "minimum_quantity": ""
        }

        self.sale = {
            "product_name": "piano",
            "quantity": 1,
            "price": 1000000
        }

        self.empty_sale = {
            "product_name": ""
        }

        self.sales_list =[
             {
                "attendant_id": 1,
                "category": "guitars",
                "price": 500000,
                "product_name": "electric guitar",
                "quantity": 2,
                "sale_id": 2
            },
            {
                "attendant_id": 1,
                "category": "bags",
                "price": 30000,
                "product_name": "pianobag",
                "quantity": 5,
                "sale_id": 1
            }
        ]
# test for products
    def test_get_unexistent_product(self):
        """test method to get a product that doesnot exist"""
        self.client.post('/api/v1/products', data=json.dumps(self.products[0]), 
        content_type='application/json')
        response = self.client.get('/api/v1/products/90')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product not found', str(response.data))

    def test_index_route(self):
        """test method for index route"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_on_url_product(self):
        """test method to post on url"""
        response = self.client.post('/api/v1/products/1', data=json.dumps(self.products[0]), 
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v1/products/', data=json.dumps(self.products[0]), 
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
    def test_post_products(self):
        """test method to post products"""
        response = self.client.post('/api/v1/products')
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v1/products',data=json.dumps(self.products[0]), 
        content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Product added successfully', str(response.data))
    
    def test_post_product_with_missing_field(self):
        response = self.client.post('/api/v1/products', json=dict(product_name='piano'),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing input field', str(response.json))

    def test_post_empty_product(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v1/products', data=json.dumps(self.empty_product), 
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_product_name_empty_string(self):
        """test method if product name is empty"""
        response = self.client.post('/api/v1/products', json=dict(product_name=" ", \
        price=30000, category="bags", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('product name should not have empty spaces', str(response.json))

    def test_post_product_name_has_digit(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v1/products', json=dict(product_name="hello1245", \
        price=30000, category="bags", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('product name should not have digits but letters', str(response.json))

    def test_post_product_name_has_non_alphanumeric(self):
        """test method if product name has non alphanumeric characters"""
        response = self.client.post('/api/v1/products', json=dict(product_name="piano****", \
        price=30000, category="bags", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('product name should not contain alphabet letters only', str(response.json))

    def test_post_price_is_a_number(self):
        """test method if price is a number"""
        response = self.client.post('/api/v1/products', json=dict(product_name="piano", \
        price="hello", category="bags", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('price should be a number', str(response.json))

    def test_post_quantity_is_a_number(self):
        """test method if quantity is a number"""
        response = self.client.post('/api/v1/products', json=dict(product_name="piano", \
        price=1000000, category="bags", quantity="hello", minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('quantity should be a number', str(response.json))

    def test_post_minimum_quantity_is_a_number(self):
        """test method if minimum_quantity is a number"""
        response = self.client.post('/api/v1/products', json=dict(product_name="piano", \
        price=1000000, category="bags", quantity=5, minimum_quantity="hello", content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('quantity should be a number', str(response.json))

    def test_post_category_name_empty_string(self):
        """test method if product name is empty"""
        response = self.client.post('/api/v1/products', json=dict(product_name="guitar", \
        price=30000, category=" ", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('category name should not have empty spaces', str(response.json))

    def test_post_category_name_has_digit(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v1/products', json=dict(product_name="guitar", \
        price=30000, category="guitars1234", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('category name should not have digits but letters', str(response.json))

    def test_post_category_name_has_non_alphanumeric(self):
        """test method if category name has non alphanumeric characters"""
        response = self.client.post('/api/v1/products', json=dict(product_name="piano", \
        price=30000, category="keyboards***((!!", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('product name should not contain alphabet letters only', str(response.json))

    def test_get_all_products(self):
        """test method to get all products """
        self.client.post('/api/v1/products', data=json.dumps(self.products[0]), 
        content_type='application/json')
        response = self.client.get('/api/v1/products')
        self.assertEqual(response.status_code, 200)

    def test_get_a_product(self):
        """test method to get a single product"""
        self.client.post('/api/v1/products', data=json.dumps(self.products[0]), 
        content_type='application/json')
        response = self.client.get('/api/v1/products/1')
        self.assertEqual(response.status_code, 200)

# tests for sales
    def test_post_sale_with_missing_field(self):
        """testing method for an empty sale"""
        response = self.client.post('/api/v1/sales')
        self.assertEqual(response.status_code, 400)
        self.client.post('/api/v1/products', data=json.dumps(self.products[0]),
        content_type="application/json")
        response = self.client.post('/api/v1/sales', json=dict(product_name=''),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('field missing', str(response.data))

    def test_sale_name_is_empty(self):
        """testing for sale name being empty string"""
        response = self.client.post('/api/v1/sales', json=dict(product_name=" ", \
        quantity=3, price=30000), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_sale_name_has_digits(self):
        """testing for sale name having digits """
        response = self.client.post('/api/v1/sales', json=dict(product_name="guitar123", \
        quantity=3, price=30000), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_sale_name_has_non_alphanumeric_characters(self):
        """testing for sale name having non_alphanumeric_characters """
        response = self.client.post('/api/v1/sales', json=dict(product_name="guitar***", \
        quantity=3, price=30000), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_sale_quantity_is_number(self):
        """testing for quantity is a number"""
        response = self.client.post('/api/v1/sales', json=dict(product_name="guitar", \
        quantity="hello", price=30000), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_sale_price_is_number(self):
        """testing for price is a number"""
        response = self.client.post('/api/v1/sales', json=dict(product_name="guitar", \
        quantity=1, price="hello"), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_a_sale(self):
        """test method to post sales """
        response = self.client.post('/api/v1/sales')
        self.assertEqual(response.status_code, 400)
        self.client.post('/api/v1/products', data=json.dumps(self.products[0]),
        content_type="application/json")
        response = self.client.post('/api/v1/sales', json=dict(product_name='piano', quantity=1, price=1000000),
        content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Sale made successfully', str(response.data))
        response = self.client.post('/api/v1/sales', json=dict(product_name='bag', quantity=1, price=30000),
        content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product not in store', str(response.data))
        
    def test_get_all_sales(self):
        """test method to get all available sales"""
        self.client.post('/api/v1/products', data=json.dumps(self.products[0]),
        content_type="application/json")
        self.client.post('/api/v1/products', data=json.dumps(self.products[1]),
        content_type="application/json")
        response = self.client.get('/api/v1/sales')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_sale(self):
        """test method to get specific sale"""
        self.client.post('/api/v1/products', data=json.dumps(self.products[0]),
        content_type="application/json")
        self.client.post('/api/v1/sales', data=json.dumps(self.sale),
        content_type='application/json')
        response = self.client.get('/api/v1/sales/1')
        self.assertEqual(response.status_code, 200)

    def test_get_unexistent_sale(self):
        """test method to get a sale that doesnot exist"""
        self.client.post('/api/v1/products', data=json.dumps(self.products[1]),
        content_type="application/json")
        response = self.client.get('/api/v1/sales/5')
        self.assertIn('Sale not found', str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_post_on_url_sale_unallowed(self):
        """test method to post on url"""
        response = self.client.post('/api/v1/sales/1', json=dict(product_name='piano'),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Unallowed ', str(response.data))

    def tearDown(self):
        self.products.clear()
        self.sales_list.clear()

if __name__ == '__main__':
    unittest.main()
    