"""user_views.py"""

import datetime
from flask import jsonify, request
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from api import app
from api.models.db import Database
from api.models.user import User
from api.user_operations import UserOperations
from api.validators import Validators

db = Database()
db.create_user_table()
db.create_products_table()
db.create_sales_table()

@app.route('/api/v2/auth/signup', methods=['POST'])
@jwt_required
def signup():
    """
    method to signup a user
    """
    user_identity = get_jwt_identity()
    if user_identity['role'] == 'admin':
      form_data = request.get_json(force=True)
      if not form_data:
        return jsonify({'message': "Missing field in request"}), 400
      firstname = form_data['firstname']
      lastname = form_data['lastname']
      username = form_data['username']
      password = form_data['password']
      valid_first= Validators.validate_input_string(firstname)
      valid_last = Validators.validate_input_string(lastname)
      valid_username = Validators.validate_input_string(username)
      valid_password = Validators.validate_password(password)
      if valid_first:
        return valid_first
      if valid_last:
        return valid_last
      if valid_username:
        return valid_username
      if valid_password:
        return valid_password
      
      user = User(firstname, lastname, username, password)
      operations = UserOperations.check_username(user.username)
      if operations:
        error = {
          "error": "Username {} already exists. Choose another".format(user.username)
        }
        return jsonify(error), 200
      # calling method to create user
      UserOperations.create_user(firstname, lastname, username, password)
      message = {
        "message": "User created successfully",
        "user": {
          "username": "{}".format(username),
          "first name": "{}".format(firstname)
        }
      }
      return jsonify(message), 201
    else:
      return jsonify({"error": "User not admin, please sign in as admin"}), 401 

@app.route('/api/v2/auth/login', methods=['POST'])
def login():
  """route to login a user"""
  if not request.is_json:
    return jsonify({'message': "Missing field in request"}), 400
  
  expires = datetime.timedelta(days=1)
  form_data = request.get_json(force=True)
  username = form_data['username']
  password = form_data['password']
    
  if not username:
    return jsonify({'message': "Missing username or email"}), 400
  if not password:
    return jsonify({'message': "Missing password"}), 400

  valid_username = UserOperations.check_username(username)
  identity = dict(username =valid_username.get('username') , role=valid_username.get('role'))
  print(identity)
  valid_password = UserOperations.check_password(password, username)
  if valid_username and valid_password:
    auth_token = create_access_token(identity=identity, expires_delta=expires)
    message = {
      "message": "User successfully logged in",
      "user": {
        "username": username,
        "auth_token": auth_token
      }
    }
    return jsonify(message), 201
  else:
    error = {
      "error": "Wrong password or username try again"
    }
    return jsonify(error), 401


@app.route('/api/v2/auth/admin', methods=['POST'])
# @jwt_required
def create_admin():
    """
    method to signup a user
    """
    form_data = request.get_json(force=True)
    if not form_data:
      return jsonify({'message': "Missing field in request"}), 400
    firstname = form_data['firstname']
    lastname = form_data['lastname']
    username = form_data['username']
    password = form_data['password']
    valid_data = Validators().validate_input_string(firstname)
    if valid_data:
      return valid_data
    user = User(firstname, lastname, username, password)
    operations = UserOperations.check_username(user.username)
    if operations:
      error = {
        "error": "Username {} already exists.".format(user.username)
      }
      return jsonify(error), 200
    # calling method to create admin user
    UserOperations().create_admin(firstname, lastname, username, password)
    message = {
      "message": "User created successfully",
      "user": {
        "username": "{}".format(username),
        "first name": "{}".format(firstname)
      }
    }

    return jsonify(message), 201
    
