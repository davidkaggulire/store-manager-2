"""product_views.py"""

from flask import jsonify, request, make_response, Blueprint
from api.models.products import Products
from api.product_actions import ProductActions
from api.validators import Validators
from flask_jwt_extended import (jwt_required, get_jwt_identity)

product = Blueprint('product', __name__)


@product.route('/')
def home():
    """Home route"""
    return make_response(jsonify({"message": "Welcome to Store Manager"}), 200)


@product.route('/api/v2/products', methods=['POST'])
@jwt_required
def post_products():
    """
    method to post a product
    """
    user_identity = get_jwt_identity()
    if user_identity['role'] == 'admin':
        try:
            form_data = request.get_json(force=True)
            product_name = form_data['product_name']
            category = form_data['category']
            price = form_data['price']
            quantity = form_data['quantity']
            minimum_quantity = form_data['minimum_quantity']

            if product_name == "":
                return jsonify({"error": "Product name missing"}), 400
            if category == "":
                return jsonify({"error": "Category missing"}), 400
            if price == "":
                return jsonify({"error": "price missing"}), 400
            if quantity == "":
                return jsonify({"error": " Quantity missing"}), 400
            if minimum_quantity == "":
                return jsonify({"error": "Minimum Quantity missing"}), 400

            product = Products(product_name, category, price, quantity, minimum_quantity)
            valid_name = Validators.validate_input_string(product_name)
            valid_category = Validators.validate_input_string(category)
            valid_price = Validators.validate_input_number(price)
            valid_quantity = Validators.validate_input_number(quantity)
            valid_minimum = Validators.validate_input_number(minimum_quantity)
            if valid_name:
                return valid_name
            if valid_category:
                return valid_category
            if valid_price:
                return valid_price
            if valid_quantity:
                return valid_quantity
            if valid_minimum:
                return valid_minimum

            product_in_store = ProductActions.check_product_name(product.product_name)
            if product_in_store:
                error = {
                    "error": "Product {} already exists.".format(product_name)
                }
                return jsonify(error), 200
            # save product in database
            save_product = ProductActions.create_product(product_name, category, price, quantity, minimum_quantity)
            if save_product:
                message = {
                    "message": "Product created successfully",
                    "product": {
                        "product_name": product_name,
                        "category": category,
                        "price": price,
                        "quantity": quantity,
                        "minimum_quantity": minimum_quantity,
                    }
                }
                return jsonify(message), 201
        except Exception:
            return jsonify({'message': 'Please input right data format'}), 400
    else:
        return jsonify({"error": "Please sign in as admin"}), 401


@product.route('/api/v2/products')
def get_products():
    """route to return all products"""
    fetch_all = ProductActions()
    get_all_products = fetch_all.get_products()
    if get_all_products:
        message = {
            "message": "All products returned successfully",
            "product_list": get_all_products
        }
        return jsonify(message), 200
    else:
        return jsonify({"message": "No products found" }), 404

@product.route('/api/v2/products/<int:product_id>')
def get_product(product_id):
    """route to get single product"""
    fetch_one_product = ProductActions().get_single_product(product_id)
    if fetch_one_product:
        message = {
            "message": "Product retrieved successfully",
            "product": {
                'product_id': fetch_one_product[0],
                'product_name': fetch_one_product[1],
                'category': fetch_one_product[2],
                'price': fetch_one_product[3],
                'quantity': fetch_one_product[4],
                'minimum_quantity': fetch_one_product[5],
                'date': fetch_one_product[6]
            }
        }
        return jsonify(message), 200
    else:
        return jsonify({"error": "Product not found"}), 404


@product.route('/api/v2/products/')
def get_on_url():
    """route to get on wrong data"""
    return jsonify({"error": "Unallowed route"}), 400


@product.route('/api/v2/products/<int:product_id>', methods=['POST'])
def post_product(product_id):
    """route to post a product to an Id"""
    return jsonify({"error": "Unallowed route"}), 400


@product.route('/api/v2/products/', methods=['POST'])
def post_wrong_url_products():
    """route to handle wrong url on post"""
    return jsonify({"error": "Unallowed route"}), 400


@product.route('/api/v2/products/<int:product_id>', methods=['PUT'])
@jwt_required
def update_product(product_id):
    """route to update a product """
    user_identity = get_jwt_identity()
    if user_identity['role'] == 'admin':
        try:
            form_data = request.get_json(force=True)
            product_name = form_data['product_name']
            category = form_data['category']
            price = form_data['price']
            quantity = form_data['quantity']
            minimum_quantity = form_data['minimum_quantity']

            if product_name == "":
                return jsonify({"error": "Product name missing"}), 400
            if category == "":
                return jsonify({"error": "Category missing"}), 400
            if price == "":
                return jsonify({"error": "price missing"}), 400
            if quantity == "":
                return jsonify({"error": " Quantity missing"}), 400
            if minimum_quantity == "":
                return jsonify({"error": "Minimum Quantity missing"}), 400

            valid_name = Validators.validate_input_string(product_name)
            valid_category = Validators.validate_input_string(category)
            valid_price = Validators.validate_input_number(price)
            valid_quantity = Validators.validate_input_number(quantity)
            valid_minimum = Validators.validate_input_number(minimum_quantity)
            if valid_name:
                return valid_name
            if valid_category:
                return valid_category
            if valid_price:
                return valid_price
            if valid_quantity:
                return valid_quantity
            if valid_minimum:
                return valid_minimum
            get_product = ProductActions.get_single_product(product_id)
            if get_product:
                update = ProductActions.edit_product(product_id, product_name, category, price, quantity, minimum_quantity)
                if update:
                    message = {
                        "message": "product edited",
                        "updated product": {
                            "product_name": product_name,
                            "category": "{}".format(category),
                            "price": "{}".format(price),
                            "quantity": "{}".format(quantity),
                            "minimum_quantity": "{}".format(minimum_quantity),
                        }
                    }
                    return jsonify(message), 201
            else:
                return jsonify({"error": "Product not found"}), 404
        except Exception:
            return jsonify({"error": "Wrong data format"}), 400
    else:
        return jsonify({"error": "Please sign in as admin"}), 401


@product.route('/api/v2/products', methods=['PUT'])
def put_on_wrong_route():
    """route to put on wrong route"""
    return jsonify({"error": "unallowed route"}), 400


@product.route('/api/v2/products/<int:product_id>', methods=['DELETE'])
def delete(product_id):
    """route to delete product"""
    get_product = ProductActions.get_single_product(product_id)
    if get_product:
        deleted_product = ProductActions.delete_product(product_id)
        if deleted_product:
            return jsonify({"message": "product deleted successfully"}), 200
    return jsonify({"error": "product not found"}), 404
