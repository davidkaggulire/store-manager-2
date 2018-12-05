"""sales_views.py"""

import datetime
from flask import jsonify, request, Blueprint
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from flasgger import swag_from
from api.controllers.product_controllers import ProductController
from api.controllers.sales_controllers import SalesController
from api.validators import Validators

sales = Blueprint('sales', __name__)


@sales.route('/api/v2/sales', methods=['POST'])
@jwt_required
@swag_from('../swagger/sales/create_sale.yml')
def post_sale():
    """method to post a sale"""

    user_identity = get_jwt_identity()
    if user_identity['role'] == 'attendant':
        try:
            form_data = request.get_json(force=True)
            product_id = form_data['product_id']
            quantity = form_data['quantity']

            if product_id == "" or quantity == "":
                return jsonify({"error": "product id or quantity missing"}), 400

            valid_product_id = Validators.validate_input_number(product_id)
            if valid_product_id:
                return valid_product_id
            valid_quantity = Validators.validate_input_number(quantity)
            if valid_quantity:
                return valid_quantity

            product = ProductController()
            sale = SalesController()
            check_product = product.get_single_product(product_id)

            if check_product:
                db_quantity = int(check_product[4])
                if db_quantity == 0:
                    return jsonify({"message": "Product out of stock"}), 400
                if quantity > db_quantity:
                    return jsonify({"message": "Quantity greater than store quantity"}), 400
                
                balance_quantity = db_quantity - quantity
                total = check_product[3] * quantity
                product_name = check_product[1]
                sale.create_sale(product_name, quantity, total, user_identity['id'], product_id)
                sale.update_on_sale(product_id, balance_quantity)
                message = {
                    "message": "Sale made successfully",
                    "sale_receipt": {
                        "product_id": "{}".format(product_id),
                        "product_name": product_name,
                        "quantity": quantity,
                        "total": total,
                        "attendant_id": user_identity['id'],
                        "datetime": str(datetime.datetime.now())
                    }
                }
                return jsonify(message), 201
            return jsonify({"message": "Product not found"}), 404
        except KeyError:
            return jsonify({"error": "Wrong input data"}), 400
    else:
        return jsonify({"message": "Please sign in as attendant"}), 401


@sales.route('/api/v2/sales')
@jwt_required
@swag_from('../swagger/sales/get_sales.yml')
def get_all_sales():
    """route to return all sales"""
    sale = SalesController()
    user_identity = get_jwt_identity()
    if user_identity['role'] == 'admin':
        all_sales = sale.get_sales()
        if len(all_sales) == 0:
            return jsonify({"message": "no sales have been made yet"}), 200
        if all_sales:
            message = {
                "message": "All sales retrieved",
                "sales": all_sales
            }
            return jsonify(message), 200
    else:
        return jsonify({"message": "Please sign in as admin"}), 401


@sales.route('/api/v2/sales/<int:sale_id>')
@swag_from('../swagger/sales/get_sale.yml')
def get_sale(sale_id):
    """route to return a single sale"""
    sale = SalesController()
    single_sale = sale.get_single_sale(sale_id)
    if single_sale:
        message = {
            "message": "Sale retrieved",
            "sale": {
                "sale_id": single_sale[0],
                "product_name": single_sale[1],
                "quantity": single_sale[2],
                "total": single_sale[3],
                "attendant_id": single_sale[4],
                "product_id": single_sale[5],
                "date": single_sale[6]
            }
        }
        return jsonify(message), 200
    else:
        return jsonify({"message": "Sale not found"}), 404


@sales.route('/api/v2/sales/')
def get_wrong_sale():
    """route to wrong sale"""
    return jsonify({"error": "Unallowed route"}), 400


@sales.route('/api/v2/sales/<int:sale_id>', methods=['POST'])
def post_sale_with_id(sale_id):
    """route to post a sale to an Id"""
    return jsonify({"error": "Unallowed route"}), 400


@sales.route('/api/v2/sales/', methods=['POST'])
def post_wrong_url_sale():
    """route to handle wrong url on post"""
    return jsonify({"error": "Unallowed route"}), 400
