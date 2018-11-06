"""test_sales.py"""

import json
from tests.base_test import TestBase
from . import PRODUCT_LIST, SALE

class TestSale(TestBase):
    """class to test sales_views/routes"""
    def test_creating_sale(self):
        """test for creating a sale"""
        pass
    

    def test_post_sale_with_missing_field(self):
        """testing method for an empty sale"""
        response = self.client.post('/api/v2/sales')
        self.assertEqual(response.status_code, 400)
        self.client.post('/api/v1/products', data=json.dumps(PRODUCT_LIST[0]),
        content_type="application/json")
        response = self.client.post('/api/v2/sales', json=dict(product_name=''),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('field missing', str(response.data))

    def test_sale_name_is_empty(self):
        """testing for sale name being empty string"""
        response = self.client.post('/api/v2/sales', json=dict(product_id="",quantity=3), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_sale_id_has_letters(self):
        """testing for sale name having digits """
        response = self.client.post('/api/v2/sales', json=dict(product_id="", \
        quantity=3), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_sale_id_has_non_alphanumeric_characters(self):
        """testing for sale name having non_alphanumeric_characters """
        response = self.client.post('/api/v2/sales', json=dict(product_id="guitar***", \
        quantity=3, price=30000), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_sale_quantity_is_string(self):
        """testing for quantity is a number"""
        response = self.client.post('/api/v2/sales', json=dict(product_name="guitar", \
        quantity="hello"), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_a_sale(self):
        """test method to post sales """
        response = self.client.post('/api/v2/sales')
        self.assertEqual(response.status_code, 400)
        self.client.post('/api/v1/products', data=json.dumps(PRODUCT_LIST[0]),
        content_type="application/json")
        response = self.client.post('/api/v2/sales', json=dict(product_name='piano', quantity=1, price=1000000),
        content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Sale made successfully', str(response.data))
        response = self.client.post('/api/v2/sales', json=dict(product_name='bag', quantity=1, price=30000),
        content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product not in store', str(response.data))
        
    def test_get_all_sales(self):
        """test method to get all available sales"""
        self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]),
        content_type="application/json")
        self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[1]),
        content_type="application/json")
        response = self.client.get('/api/v2/sales')
        self.assertEqual(response.status_code, 401)
        # self.assertIn('no sales have been made yet', str(response.data))

    def test_get_specific_sale(self):
        """test method to get specific sale"""
        self.client.post('/ap2/v2/products', data=json.dumps(PRODUCT),
        content_type="application/json")
        self.client.post('/api/v2/sales', data=json.dumps(SALE),
        content_type='application/json')
        response = self.client.get('/api/v2/sales/1')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Sale not found', str(response.data))

    def test_get_unexistent_sale(self):
        """test method to get a sale that doesnot exist"""
        self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]),
        content_type="application/json")
        response = self.client.get('/api/v2/sales/5')
        self.assertIn('Sale not found', str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_post_on_url_sale_unallowed(self):
        """test method to post on url"""
        response = self.client.post('/api/v2/sales/1', json=dict(product_id=1),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Unallowed route', str(response.data))
