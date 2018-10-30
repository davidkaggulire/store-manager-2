"""user_views.py"""

from flask import jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from api import app
from api.models.db import Database
from api.models.user import User
from api.db_operations import UserOperations
from api.validators import Validators

db = Database()
db.create_user_table()
app.config['JWT_SECRET_KEY'] = 'dkaggs12345'
jwt = JWTManager(app)

@app.route('/api/v2/auth/signup', methods=['POST'])
# @jwt_required
def signup():
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
      user = User(firstname, lastname, username, password)
      operations = UserOperations.check_username(user.username)
      if operations:
        error = {
          "error": "Username {} already exists.".format(user.username)
        }
        return jsonify(error), 200
        
      db.create_user(firstname, lastname, username, password)
      message = {
        "message": "User created successfully",
        "user":{
          "username": "{}".format(username),
          "first name":"{}".format(firstname)
        }
      }

      return jsonify(message), 201
    return valid_data


@app.route('/api/v2/auth/login', methods=['POST'])
def login():
  form_data = request.get_json(force=True)
  if not form_data:
    return jsonify({'message': "Missing field in request"}), 400

  username = form_data['username']
  password = form_data['password']

  if not username:
    return jsonify({'message': "Missing username or email"}), 400
  if not password:
    return jsonify({'message': "Missing password"}), 400

  
  
  valid_username = UserOperations.check_username(username)
  valid_password = UserOperations.check_password(password, username)
  if valid_username and valid_password:
    message = {
      "message": "User successfully logged in",
      "user":{
        "username": username
      }
    }
    return jsonify(message), 201
  else:
    error = {
      "error": "Wrong password or username try again"
    }
    return jsonify(error), 401
 