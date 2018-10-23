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
                "minimum_quantity": 3
            },
            {
                "product_name": "electric guitar",
                "category": "guitars",
                "price": 50000,
                "quantity": 10,
                "minimum_quantity": 2
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
            "product_name": "piano"
        }

        self.empty_sale = {
            "product_name": ""
        }

        self.sales_list =[
             {
                "attendant_id": 1,
                "category": "guitars",
                "price": 50000,
                "product_id": 2,
                "product_name": "electric guitar",
                "quantity": 10,
                "sale_id": 2
            },
            {
                "attendant_id": 1,
                "category": "bags",
                "price": 30000,
                "product_id": 1,
                "product_name": "piano bag",
                "quantity": 10,
                "sale_id": 1
            }
        ]

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

    def test_post_empty_product(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v1/products',data=json.dumps(self.empty_product), 
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing input fields', str(response.data))

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
        response = self.client.get('/api/v1/products/7')
        self.assertEqual(response.status_code, 404)

    def test_post_empty_sale(self):
        """testing method for an empty sale"""
        response = self.client.post('/api/v1/sales')
        self.assertEqual(response.status_code, 400)
        self.client.post('/api/v1/products', data=json.dumps(self.products[0]),
        content_type="application/json")
        response = self.client.post('/api/v1/sales', json=dict(product_name=''),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Product name missing', str(response.data))

    def test_post_a_sale(self):
        """test method to post sales """
        response = self.client.post('/api/v1/sales')
        self.assertEqual(response.status_code, 400)

        self.client.post('/api/v1/products', data=json.dumps(self.products[0]),
        content_type="application/json")
        response = self.client.post('/api/v1/sales', json=dict(product_name='piano'),
        content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Sale made successfully', str(response.data))
        response = self.client.post('/api/v1/sales', json=dict(product_name='guitar'),
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
        self.client.post('/api/v1/products', data=json.dumps(self.products[1]),
        content_type="application/json")
        response = self.client.get('/api/v1/sales/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('No sale has been made', str(response.data))

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
    