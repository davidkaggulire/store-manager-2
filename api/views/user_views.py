"""user_views.py"""

import datetime
from flask import jsonify, request, Blueprint
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from flasgger import swag_from
from api.controllers.user_controller import UserController
from api.validators import Validators

userpage = Blueprint('userpage', __name__)


@userpage.route('/api/v2/auth/signup', methods=['POST'])
@jwt_required
@swag_from('../swagger/users/signup.yml')
def signup():
    """
    method to signup a user
    """
    user_identity = get_jwt_identity()
    if user_identity['role'] == 'admin':
        # try:
        form_data = request.get_json(force=True)
        firstname = form_data['firstname']
        lastname = form_data['lastname']
        username = form_data['username']
        password = form_data['password']

        if firstname == '':
            return jsonify({"error": "firstname required"}), 400
        if lastname == '':
            return jsonify({"error": "lastname required"}), 400
        if username == '':
            return jsonify({"error": "username required"}), 400
        if password == '':
            return jsonify({"error": "password required"}), 400

        valid_first = Validators.validate_input_string(firstname)
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

        user = UserController()
        operations = user.correct_username(username)
        if operations:
            return jsonify({"message": "Username {} already exists. Choose another".format(username)}), 400
        # calling method to create user
        user.register_user(firstname, lastname, username, password)
        message = {
            "message": "User created successfully",
            "user": {
                "username": "{}".format(username),
                "first name": "{}".format(firstname)
            }
        }
        return jsonify(message), 201
        # except Exception:
            # return jsonify({"error": "wrong input data"}), 405
    else:
        return jsonify({"message": "Please sign in as admin"}), 401


@userpage.route('/api/v2/auth/login', methods=['POST'])
@swag_from('../swagger/users/login.yml')
def login():
    """route to login a user"""
    try:
        expires = datetime.timedelta(days=1)
        form_data = request.get_json(force=True)
        username = form_data['username']
        password = form_data['password']
        if username == '':
            return jsonify({'message': "username required"}), 400
        if password == '':
            return jsonify({'message': "password required"}), 400

        valid_user = Validators.validate_input_string(username)
        valid_pass = Validators.validate_password(password)
        if valid_user:
                return valid_user
        if valid_pass:
            return valid_pass

        user = UserController()
        valid_username = user.correct_username(username)
        valid_password = user.correct_password(password, username)
        if valid_username and valid_password:
            identity = dict(username=valid_username.get('username'), role=valid_username.get('role'), id=valid_username.get('user_id'))
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
            return jsonify({"message": "Wrong username or password, try again"}), 401
    except Exception:
        return jsonify({"error": "wrong input data"}), 400


@userpage.route('/api/v2/auth/admin', methods=['POST'])
@swag_from('../swagger/users/create_admin.yml')
def create_admin():
    """
    method to signup a user
    """
    try:
        form_data = request.get_json(force=True)
        firstname = form_data['firstname']
        lastname = form_data['lastname']
        username = form_data['username']
        password = form_data['password']

        if firstname == '':
            return jsonify({"error": "firstname required"}), 400
        if lastname == '':
            return jsonify({"error": "lastname required"}), 400
        if username == '':
            return jsonify({"error": "username required"}), 400
        if password == '':
            return jsonify({"error": "password required"}), 400

        valid_first = Validators().validate_input_string(firstname)
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

        user = UserController()
        operations = user.correct_username(username)
        if operations:
            return jsonify({"message": "Username {} already exists.".format(username)}), 400
        # calling method to create admin user
        user.register_admin(firstname, lastname, username, password)
        message = {
            "message": "User created successfully",
            "user": {
                "username": "{}".format(username),
                "first name": "{}".format(firstname)
            }
        }

        return jsonify(message), 201
    except Exception:
        return jsonify({"error": "wrong input data"}), 405
