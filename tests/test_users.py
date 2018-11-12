"""
module test_users
"""

import json
from . import ADMIN_USER, LOGIN_ADMIN, USER, LOGIN_USER, USERS, INVALID_USER
from tests.base_test import TestBase


class TestUsers(TestBase):
    """
    class that tests routes
    """
    def test_creating_admin(self):
        """test method to create admin"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        self.assertEqual(response.status_code, 201)

    def test_creating_admin_exists(self):
        """test method to check if admin exists"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        self.assertEqual(response.status_code, 201)
        self.assertIn('Username {} already exists'.format(ADMIN_USER['username']), str(response.data))

    def test_create_admin_with_missing_fields(self):
        """test method to check if a certain field is missing"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(INVALID_USER))
        self.assertEqual(response.status_code, 400)
        self.assertIn('wrong input data', str(response.data))

    def test_create_admin_with_missing_firstname(self):
        """test method to check for firstname"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='', lastname='david', username='dave', password='password'))
        self.assertIn('firstname required', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_missing_lastname(self):
        """test method to check for lastname"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david', lastname='', username='dave', password='password'))
        self.assertIn('lastname required', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_missing_username(self):
        """test method to check for missing name"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david', lastname='kaggs', username='', password='password'))
        self.assertIn('username required', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_missing_password(self):
        """test method to check for password"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david', lastname='kaggs', username='dave', password=''))
        self.assertIn('password required', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_numbers_name(self):
        """test method to check firstname for numbers"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david123', lastname='kaggs', username='dave', password='david'))
        self.assertIn('input should not have digits', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_alphanumeric_name(self):
        """test method to check firstname for alphanumerics"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david@@@', lastname='kaggs', username='dave', password='david'))
        self.assertIn('input should contain alphabet letters only', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_spaces_name(self):
        """test method to check firstname for spaces"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david   ', lastname='kaggs', username='dave', password='david'))
        self.assertIn('input should not have empty spaces', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_numbers_lastname(self):
        """test method to lastname for numbers"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david', lastname='kaggs123', username='dave', password='david'))
        self.assertIn('input should not have digits', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_alphanumeric_lastname(self):
        """test method to test lastname for alphanumeric"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david', lastname='kaggs***', username='dave', password='david'))
        self.assertIn('input should contain alphabet letters only', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_spaces_lastname(self):
        """test method to check lastname for spaces"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david', lastname='kaggs  ', username='dave', password='david'))
        self.assertIn('input should not have empty spaces', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_numbers_username(self):
        """test method to check username for numbers"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david', lastname='kaggs', username='dave123', password='david'))
        self.assertIn('input should not have digits', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_alphanumeric_username(self):
        """test method to check username for alphanumeric"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', 
        json=dict(firstname='david', lastname='kaggs', username='dave###', password='david'))
        self.assertIn('input should contain alphabet letters only', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_spaces_username(self):
        """test method to check username for spaces"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david', lastname='kaggs', username='dave   ', password='david'))
        self.assertIn('input should not have empty spaces', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_numbers_password(self):
        """test method to check password for numbers"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david', lastname='kaggs', username='dave', password='david'))
        self.assertIn('password length should be equal or greater than 6', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_alphanumeric_password(self):
        """test method for adminpassword with alphanumeric"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', 
        json=dict(firstname='david', lastname='kaggs', username='dave', password='david123'))
        self.assertIn('password should contain alphanumeric characters', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_create_admin_with_digits_password(self):
        """test method for admin password with digits"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json',
        json=dict(firstname='david', lastname='kaggs', username='dave', password='david***'))
        self.assertIn('password should contain a digit', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_creating_user(self):
        """test method to create attendant"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        msg = json.loads(response.data.decode())
        self.assertIn('User created successfully', msg['message'])
        self.assertEqual(response.status_code, 201)

    def test_missing_field_firstname_user(self):
        """test method to check firstname if attendant"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USERS[0]),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('firstname required', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_missing_field_lastname_user(self):
        """test method to check lastname if attendant"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USERS[1]),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('lastname required', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_missing_field_username_user(self):
        """test method to check username if attendant"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USERS[2]),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('username required', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_missing_field_password_user(self):
        """test method to check password if attendant"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USERS[3]),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('password required', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_with_missing_fields(self):
        """test method check missing field if attendant"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(INVALID_USER),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('wrong input data', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_firstname_with_digits(self):
        """test method to check firstname for digits"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave123', lastname='david', username='david', password='david123!'),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('input should not have digits but letters', str(response.data))
        self.assertEqual(response.status_code, 400) 
    
    def test_signup_firstname_with_symbols(self):
        """test method to check firstname for symbols"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave**', lastname='david', username='david', password='david123!'),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('input should contain alphabet letters only', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_firstname_with_spaces(self):
        """test method to check firstname for spaces"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave   ', lastname='david', username='david', password='david123!'),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('input should not have empty spaces', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_lastname_with_digits(self):
        """test method to check lastname for digits"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave', lastname='david123', username='david', password='david123!'),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('input should not have digits but letters', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_lastname_with_symbols(self):
        """test method to check lastname for symbols"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave', lastname='david**', username='david', password='david123!'),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('input should contain alphabet letters only', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_lastname_with_spaces(self):
        """test method to check lastname for spaces"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave', lastname='david  ', username='david', password='david123!'),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('input should not have empty spaces', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_username_with_digits(self):
        """test method to check lastname"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave', lastname='david', username='david123', password='david123!'),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('input should not have digits but letters', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_username_with_symbols(self):
        """test method to check username for symbols"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave', lastname='david', username='david**', password='david123!'),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('input should contain alphabet letters only', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_username_with_spaces(self):
        """test method to check username for spaces"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave', lastname='david', username='david   ', password='david123!'), 
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('input should not have empty spaces', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_password_for_symbols(self):
        """test method to check password for symbols"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave', lastname='david', username='david', password='david123'),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('password should contain alphanumeric characters', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_password_for_length(self):
        """test method to check password length"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave', lastname='david', username='david', password='david'),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('password length should be equal or greater than 6', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_password_for_digit(self):
        """test method to check password length"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', json=dict(firstname='dave', lastname='david', username='david', password='david***'),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('password should contain a digit', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_when_attendant(self):
        """test method to create attendant if attendant"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers={'content_type': 'application/json', 
        'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_USER))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER), headers={'content_type': 'application/json', 
        'Authorization': 'Bearer ' + token['auth_token']})
        self.assertIn('Please sign in as admin', str(response.data))
        self.assertEqual(response.status_code, 401)

    def test_creating_user_when_exists(self):
        """test method to create name if name exists"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER),
        headers={'content_type': 'application/json', 'Authorization': "Bearer " + token['auth_token']})
        self.assertIn('Username {} already exists'.format(USER['username']), str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_login_admin_user(self):
        """test method to login admin_user"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        self.assertIn('User successfully logged in', msg['message'])
        self.assertEqual(response.status_code, 201)

    def test_login_admin_user_missing_field(self):
        """test method to login admin_user with missing field"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', json=dict(password="hello"))
        msg = json.loads(response.data.decode())
        self.assertIn('wrong input data', msg['error'])
        self.assertEqual(response.status_code, 400)

    def test_login_admin_user_empty_username(self):
        """test method to login admin_user with empty username"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', json=dict(username='', password="hello"))
        msg = json.loads(response.data.decode())
        self.assertIn('username required', msg['message'])
        self.assertEqual(response.status_code, 400)

    def test_login_admin_user_empty_password(self):
        """test method to login password is empty"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', json=dict(username='don', password=''))
        msg = json.loads(response.data.decode())
        self.assertIn('password required', msg['message'])
        self.assertEqual(response.status_code, 400)

    def test_login_username_has_digits(self):
        """test method to login username has digits"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', json=dict(username='don1234', password='hello1234!'))
        msg = json.loads(response.data.decode())
        self.assertIn('input should not have digits but letters', msg['error'])
        self.assertEqual(response.status_code, 400)

    def test_login_password(self):
        """test login password is of required length"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', json=dict(username='don', password='hello'))
        msg = json.loads(response.data.decode())
        self.assertIn('password length should be equal or greater than 6', msg['error'])
        self.assertEqual(response.status_code, 400)

    def test_login_wrong_admin_user(self):
        """test method to check wrong_admin"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_USER))
        msg = json.loads(response.data.decode())
        self.assertIn('Wrong username or password, try again', msg['message'])
        self.assertEqual(response.status_code, 401)

    def test_login_normal_user(self):
        """test method to login normal user"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        print(msg)
        token = msg['user']
        print(token)
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER),
        headers={'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_USER))
        self.assertEqual(response.status_code, 201)
        self.assertIn('User successfully logged in', str(response.data))

    def test_login_normal_user_missing_field(self):
        """test method to login normal user with missing field"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        token = msg['user']
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER),
        headers={'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', content_type='application/json', json=dict(username='david'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('wrong input data', str(response.data))

    def test_login_normal_user_fail(self):
        """test method to login normal user fails"""
        response = self.client.post('/api/v2/auth/admin', content_type='application/json', data=json.dumps(ADMIN_USER))
        response = self.client.post('/api/v2/auth/login', content_type='application/json', data=json.dumps(LOGIN_ADMIN))
        msg = json.loads(response.data.decode())
        print(msg)
        token = msg['user']
        print(token)
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(USER),
        headers={'content_type': 'application/json', 'Authorization': 'Bearer ' + token['auth_token']})
        response = self.client.post('/api/v2/auth/login', content_type='application/json', json=dict(username='esther', password='esth123!'))
        self.assertEqual(response.status_code, 401)
        self.assertIn('Wrong username or password, try again', str(response.data))
