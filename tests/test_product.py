"""
module test
"""

import json
from tests.base_test import TestBase
from api.models.db import Database
from api.controllers.user_controller import UserController
from api import create_app
from . import ADMIN_USER, LOGIN_ADMIN, USER, PRODUCT, EMPTY_PRODUCT, PRODUCT_LIST, SALE


class TestProducts(TestBase):
    """
    class that tests routes
    """
    def test_get_unexistent_product(self):
        """test method to get a product that doesnot exist"""
        self.client.post('/api/v2/products', json=dict(product_name="guitarbag", price=30000, category="bags", quantity=10, minimum_quantity=3, content_type='application/json'))
        product_id = {"id": 9}
        response = self.client.get('/api/v2/products/{}'.format(product_id['id']))
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product not found', str(response.data))

    def test_index_route(self):
        """test method for index route"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_on_url_product(self):
        """test method to post on url"""
        response = self.client.post('/api/v2/products/1', data=json.dumps(PRODUCT), 
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v2/products/', data=json.dumps(PRODUCT), 
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
    def test_post_products(self):
        """test method to post products without token"""
        response = self.client.post('/api/v2/products')
        self.assertEqual(response.status_code, 401)
        response = self.client.post('/api/v2/products',data=json.dumps(PRODUCT), 
        content_type='application/json')
        msg = json.loads(response.data.decode())
        self.assertIn("Missing Authorization Header", msg['msg'])
        self.assertEqual(response.status_code, 401)

    def test_post_product_if_admin(self):
        """test method to post product if admin"""
        
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='don', lastname='david', username='don', password='don1234!'))
        self.assertIn('message', str(response.data))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', json=dict(username='don', password='don1234!'))
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT),
        headers = {'content_type': 'application/json', 'Authorization': "Bearer "+ token['auth_token']})
        msg = json.loads(response.data.decode())
        self.assertIn('Product created successfully', msg["message"] )
        self.assertEqual(response.status_code, 201)


    def test_post_product_with_missing_field(self):
        response = self.client.post('/api/v2/products', json=dict(product_name='book'),
        content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('Missing Authorization Header', str(response.json))

    def test_post_empty_product(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v2/products', data=json.dumps(EMPTY_PRODUCT), 
        content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_post_product_name_empty_string(self):
        """test method if product name is empty"""
        response = self.client.post('/api/v2/products', json=dict(product_name=" ",
        price=30000, category="bags", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 401)
        # self.assertIn('product name should not have empty spaces', str(response.json))

    def test_post_product_name_has_digit(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/products', json=dict(product_name="hello1245",
        price=30000, category="bags", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 401)
        # self.assertIn('product name should not have digits but letters', str(response.json))

    def test_post_product_name_has_non_alphanumeric(self):
        """test method if product name has non alphanumeric characters"""
        response = self.client.post('/api/v2/products', json=dict(product_name="piano****",
        price=30000, category="bags", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('product name should not contain alphabet letters only', str(response.json))

    def test_post_price_is_a_number(self):
        """test method if price is a number"""
        response = self.client.post('/api/v2/products', json=dict(product_name="piano",
        price="hello", category="bags", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('price should be a number', str(response.json))

    def test_post_quantity_is_a_string(self):
        """test method if quantity is a number"""
        response = self.client.post('/api/v2/products', json=dict(product_name="piano",
        price=1000000, category="bags", quantity="hello", minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('quantity should be a number', str(response.json))

    def test_post_minimum_quantity_is_a_string(self):
        """test method if minimum_quantity is a number"""
        response = self.client.post('/api/v2/products', json=dict(product_name="piano",
        price=1000000, category="bags", quantity=5, minimum_quantity="hello", content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('quantity should be a number', str(response.json))

    def test_post_category_name_empty_string(self):
        """test method if product name is empty"""
        response = self.client.post('/api/v2/products', json=dict(product_name="guitar",
        price=30000, category=" ", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('category name should not have empty spaces', str(response.json))

    def test_post_category_name_has_digit(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/products', json=dict(product_name="guitar",
        price=30000, category="guitars1234", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('category name should not have digits but letters', str(response.json))

    def test_post_category_name_has_non_alphanumeric(self):
        """test method if category name has non alphanumeric characters"""
        response = self.client.post('/api/v2/products', json=dict(product_name="piano",
        price=30000, category="keyboards***((!!", quantity=10, minimum_quantity=3, content_type='application/json'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('product name should not contain alphabet letters only', str(response.json))

    def test_get_all_products(self):
        """test method to get all products """
        self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST), 
        content_type='application/json')
        response = self.client.get('/api/v2/products')
        self.assertEqual(response.status_code, 404)
        self.assertIn('No products found', str(response.json ))

    def test_get_a_product(self):
        """test method to get a single product"""
        self.client.post('/api/v2/products', data=json.dumps(PRODUCT), 
        content_type='application/json')
        response = self.client.get('/api/v2/products/1')
        self.assertEqual(response.status_code, 404)
