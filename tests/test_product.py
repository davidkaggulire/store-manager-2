"""
module test
"""

import json
from tests.base_test import TestBase
from . import ADMIN_USER, LOGIN_ADMIN, USER, PRODUCT, EMPTY_PRODUCT, PRODUCT_LIST, SALE, LOGIN_USER


class TestProducts(TestBase):
    """
    class that tests routes
    """
    def test_index_route(self):
        """test method for index route"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to Store Manager', str(response.data))

    def test_post_on_url_product(self):
        """test method to post on url"""
        response = self.client.post('/api/v2/products/', data=json.dumps(PRODUCT), 
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Unallowed route', str(response.data))

    def test_post_id_on_route(self):
        """test to check post id on route"""
        response = self.client.post('/api/v2/products/1', data=json.dumps(PRODUCT), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Unallowed route', str(response.data))
        
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
        headers = {'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        msg = json.loads(response.data.decode())
        self.assertIn('Product created successfully', msg["message"] )
        self.assertEqual(response.status_code, 201)

    def test_post_product_if_attendant(self):
        """test method to post product if admin"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='don', lastname='david', username='don', password='don1234!'))
        self.assertIn('message', str(response.data))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', json=dict(username='don', password='don1234!'))
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER),
        headers = {'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_USER))
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT),
        headers = {'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        msg = json.loads(response.data.decode())
        self.assertIn('Please sign in as admin', msg["message"] )
        self.assertEqual(response.status_code, 401)

    def test_post_product_if_already_exists(self):
        """test method to post product if admin"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='don', lastname='david', username='don', password='don1234!'))
        self.assertIn('message', str(response.data))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', json=dict(username='don', password='don1234!'))
        msg = json.loads(response.data.decode("utf-8"))
        token = msg["user"]
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT),
        headers = {'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT),
        headers = {'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        msg = json.loads(response.data.decode())
        self.assertIn('Product {} already exists'.format(PRODUCT['product_name']), msg["message"] )
        self.assertEqual(response.status_code, 201)

    def test_post_product_with_missing_field(self):
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name='book'),
        headers={'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please input right data format', str(response.json))

    def test_post_empty_product_name(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(EMPTY_PRODUCT), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('all fields required', str(response.json))

    def test_post_empty_product_category(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name='book', category="", price="", quantity="", minimum_quantity=""), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('all fields required', str(response.json))

    def test_post_empty_product_price(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name='book', category="scholar", price="", quantity=3, minimum_quantity=6), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('all fields required', str(response.json))

    def test_post_empty_product_quantity(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name='book', category="scholar", price=1000, quantity="", minimum_quantity=6), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('all fields required', str(response.json))

    def test_post_empty_product_minimum_quantity(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name='book', category="scholar", price=1000, quantity=3, minimum_quantity=""), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('all fields required', str(response.json))

    def test_post_product_name_has_digit(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name="pen1245",price=30000, category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should not have digits but letters', str(response.json))

    def test_post_product_name_has_alphanumeric(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name="book**$$",price=30000, category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should contain alphabet letters', str(response.json))

    def test_post_product_name_has_spaces(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name="    ",price=30000, category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should not have empty spaces', str(response.json))

    def test_post_price_is_a_string(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name="book",price="30000", category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should be a number', str(response.json))

    def test_post_quantity_is_a_string(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name="book",price=30000, category="bags", quantity="10", minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should be a number', str(response.json))
    
    def test_post_minimumquantity_is_a_string(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name="book",price=30000, category="bags", quantity=10, minimum_quantity="3"),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should be a number', str(response.json))

    def test_post_category_name_has_digit(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name="pen",price=30000, category="scholar123", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should not have digits but letters', str(response.json))

    def test_post_category_name_has_alphanumeric(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name="book",price=30000, category="scholar**", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should contain alphabet letters', str(response.json))

    def test_post_category_name_has_spaces(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', json=dict(product_name="book",price=30000, category="scholar  ", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should not have empty spaces', str(response.json))

    def test_get_all_products(self):
        """test method to get all products """
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), headers={'content_type': 'application/json', 
        'Authorization': 'Bearer ' + token['auth_token']})
        self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[1]), headers={'content_type': 'application/json', 
        'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.get('/api/v2/products')
        self.assertEqual(response.status_code, 200)
        self.assertIn('All products', str(response.data))

    def test_get_all_products_when_no_product_exists(self):
        """test method to check for products"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        response = self.client.get('/api/v2/products')
        self.assertEqual(response.status_code, 404)
        self.assertIn('No products found', str(response.data))

    def test_get_a_product(self):
        """test method to get all products """
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[0]), headers={'content_type': 'application/json', 
        'Authorization': 'Bearer ' + token['auth_token']})
        self.client.post('/api/v2/products', data=json.dumps(PRODUCT_LIST[1]), headers={'content_type': 'application/json', 
        'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.get('/api/v2/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product retrieved successfully', str(response.data))

    def test_get_unexistent_product(self):
        """test method to get a product that doesnot exist"""
        self.client.post('/api/v2/products', json=dict(product_name="guitarbag", price=30000, category="bags", quantity=10, minimum_quantity=3, content_type='application/json'))
        response = self.client.get('/api/v2/products/9')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product not found', str(response.data))

    def test_get_on_wrong_url(self):
        """test to check for get on wrong url"""
        response = self.client.get('/api/v2/products/')
        self.assertIn('Unallowed route', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_update_product_with_missing_field(self):
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name='book'),
        headers={'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Wrong data format', str(response.json))

    def test_update_empty_product_name(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', data=json.dumps(EMPTY_PRODUCT), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('all fields required', str(response.json))

    def test_update_empty_product_category(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name='book', category="", price="", quantity="", minimum_quantity=""), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('all fields required', str(response.json))

    def test_update_empty_product_price(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/2', json=dict(product_name='book', category="scholar", price="", quantity=3, minimum_quantity=6), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('all fields required', str(response.json))

    def test_update_empty_product_quantity(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name='book', category="scholar", price=1000, quantity="", minimum_quantity=6), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('all fields required', str(response.json))

    def test_update_empty_product_minimum_quantity(self):
        """test method to check for empty fields"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name='book', category="scholar", price=1000, quantity=3, minimum_quantity=""), 
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('all fields required', str(response.json))

    def test_update_product_name_has_digit(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen1245",price=30000, category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should not have digits but letters', str(response.json))

    def test_update_product_name_has_alpha(self):
        """test method if product name has alphanumeric"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen@@@",price=30000, category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should contain alphabet letters only', str(response.json))

    def test_update_product_name_has_spaces(self):
        """test method if product name has spaces"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen   ",price=30000, category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should not have empty spaces', str(response.json))

    def test_update_price_name_is_string(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen",price="30000", category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should be a number', str(response.json))

    def test_update_quantity_is_string(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen",price=30000, category="bags", quantity="10", minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should be a number', str(response.json))

    def test_update_minimumquantity_is_string(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen",price=30000, category="bags", quantity=10, minimum_quantity="3"),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should be a number', str(response.json))

    def test_update_category_has_spaces(self):
        """test method if product name has spaces"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen",price=30000, category="bags  ", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should not have empty spaces', str(response.json))

    def test_update_category_has_digits(self):
        """test method if product name has digits"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen",price=30000, category="bags1234", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should not have digits but letters', str(response.json))

    def test_update_category_has_alpha(self):
        """test method if product name has alpha"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen",price=30000, category="bags***", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})        
        self.assertEqual(response.status_code, 400)
        self.assertIn('input should contain alphabet letters only', str(response.json))

    def test_update_if_admin_no_pdt_posted(self):
        """test to update if admin with no product yet"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen",price=30000, category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product not found', str(response.json))

    def test_update_if_attendant(self):
        """test to update if attendant"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), 
        headers = {'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_USER), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen",price=30000, category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Please sign in as admin', str(response.json))

    def test_update_if_admin(self):
        """test to update if admin"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT),headers = {'content_type': 'application/json',
        'Authorization': "Bearer " + token['auth_token']})
        response = self.client.put('/api/v2/products/1', json=dict(product_name="pen",price=30000, category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 201)
        self.assertIn('product updated', str(response.json))

    def test_update_if_on_wrong_route(self):
        """test to update on wrong route"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT),headers = {'content_type': 'application/json',
        'Authorization': "Bearer " + token['auth_token']})
        response = self.client.put('/api/v2/products', json=dict(product_name="pen",price=30000, category="bags", quantity=10, minimum_quantity=3),
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 400)
        self.assertIn('unallowed route', str(response.json))

    def test_delete_product(self):
        """test to delete a product"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT),headers = {'content_type': 'application/json',
        'Authorization': "Bearer " + token['auth_token']})
        response = self.client.delete('/api/v2/products/1',
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 200)
        self.assertIn('deleted successfully', str(response.json))

    def test_delete_product_if_not_found(self):
        """test to delete a product"""
        response = self.client.post('/api/v2/auth/admin', data=json.dumps(ADMIN_USER), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(LOGIN_ADMIN), content_type='application/json', )
        msg = json.loads(response.data.decode("utf-8"))
        token = msg['user']
        response = self.client.post('/api/v2/products', data=json.dumps(PRODUCT),headers = {'content_type': 'application/json',
        'Authorization': "Bearer " + token['auth_token']})
        response = self.client.delete('/api/v2/products/3',
        headers = {'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        self.assertEqual(response.status_code, 404)
        self.assertIn('product not found', str(response.json))
