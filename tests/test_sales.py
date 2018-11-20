"""test_sales.py"""

import json
from tests.base_test import TestBase
from . import PRODUCT_LIST, SALE, ADMIN_USER, LOGIN_ADMIN, USER, LOGIN_USER

class TestSale(TestBase):
    """class to test sales_views/routes"""

    def test_post_sale_with_missing_id(self):
        """test method to check for empty id"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/sales', json=dict(product_id="", quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('product id or quantity missing', str(response.data))
    
    def test_post_sale_with_quantity(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/sales', json=dict(product_id=1, quantity=""),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('product id or quantity missing', str(response.data))

    def test_sale_when_product_id_has_letters(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/sales', json=dict(product_id="boy", quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should be a number', str(response.data))

    def test_sale_when_quantity_has_letters(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/sales', json=dict(product_id=1, quantity="bag"),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should be a number', str(response.data))

    def test_post_sale(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/sales', json=dict(product_id=1, quantity=2),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Sale made successfully', str(response.data))  

    def test_post_sale_when_product_not_found(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/sales', json=dict(product_id=3, quantity=2),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product not found', str(response.data))
        
    def test_post_sale_with_wrong_data(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/sales', json=dict(product_id=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Wrong input data', str(response.data))

    def test_post_when_admin(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(ADMIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/sales', json=dict(product_id=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Please sign in as attendant', str(response.data))

    def test_get_all_sales_when_no_sale(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(ADMIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.get('/api/v2/sales', headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 200)
        self.assertIn('no sales have been made yet', str(response.data))

    def test_get_sales_when_admin_and_posted(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/sales', json=dict(product_id=1, quantity=2),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.get('/api/v2/sales', headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']} )
        self.assertEqual(response.status_code, 200)
        self.assertIn('All sales retrieved', str(response.data))
        
    def test_get_sales_when_not_admin(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/sales', json=dict(product_id=1, quantity=2),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.get('/api/v2/sales', headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']} )
        self.assertEqual(response.status_code, 401)
        self.assertIn('Please sign in as admin', str(response.data))

    def test_get_sale_when_no_sale(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(ADMIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.get('/api/v2/sales/1', headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 404)
        self.assertIn('Sale not found', str(response.data))

    def test_get_sale_when_sale(self):
        """test method to check for empty quantity"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/sales', json=dict(product_id=1, quantity=2),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json')
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.get('/api/v2/sales/1', headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sale retrieved', str(response.data))

    def test_post_on_url_sale_unallowed(self):
        """test method to post on url"""
        response = self.client.post('/api/v2/sales/1', json=dict(product_id=1), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Unallowed route', str(response.data))

    def test_post_on_url_unallowed(self):
        """test method to post on url"""
        response = self.client.post('/api/v2/sales/', json=dict(product_id=1), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Unallowed route', str(response.data))

    def test_get_on_wrong_url(self):
        """test method to get on wrong url"""
        response = self.client.get('/api/v2/sales/', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Unallowed route', str(response.data))
