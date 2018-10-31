"""sales_views.py"""

from flask import jsonify, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from api import app
from api.models.db import Database
from api.models.user import User
from api.user_operations import UserOperations
from api.product_actions import ProductActions
from api.sales_actions import Sales_Controller
from api.validators import Validators

@app.route('/api/v2/sales', methods=['POST'])
def post_sale():
    """method to post a sale"""
    form_data = request.get_json(force=True)
    if not form_data:
      return jsonify({'message': "Missing field in request"}), 400
    product_name = form_data['product_name']
    price = form_data['price']
    quantity = form_data['quantity']

    valid_product_name = Validators.validate_input_string(product_name)
    if valid_product_name:
        return valid_product_name
    valid_price = Validators.validate_input_number(price)
    if valid_price:
        return valid_price
    valid_quantity = Validators.validate_input_number(quantity)
    if valid_quantity:
        return valid_quantity
    
    check_product = ProductActions.check_product_name(product_name)
    if check_product:
        Sales_Controller.create_sale(product_name, price, quantity)
        message = {
            "message": "Sale made successfully",
            "sale": {
                "product_name": "{}".format(product_name),
            }
        }
        return jsonify(message),201
    return jsonify({"error": "Product not found"})