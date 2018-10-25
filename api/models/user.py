"""
module user
class with general user functions
"""

from flask import jsonify, make_response

class User():
    """
    defining class User
    """
    def __init__(self, user_id, username, admin_status=False):
        """
        initializing attributes for class user
        """
        self.user_id = user_id
        self.username = username
        self.admin_status = bool(admin_status)

    def __str__(self):
        """return string rep of class"""
        return '{}'.format(self.username)

    @staticmethod
    def get_products(product_list):
        """
        returns all products in product_list
        """
        if len(product_list) == 0:
            return jsonify({'message': 'Please add products to store'}), 200
        return jsonify(product_list), 200

    @staticmethod
    def get_specific_product(product_id, product_list):
        """
        method returns specific product
        """
        if len(product_list) == 0:
            return jsonify({'message': 'Please add products to store'}), 200
        for product in product_list:
            if product['product_id'] == product_id:
                return make_response(jsonify(product), 200)
        return make_response(jsonify({'message': 'Product not found'}), 404)
            
    @staticmethod
    def get_single_sale(sale_id, admin_status, user_id, sales_list):
        """
        method to get a specific sale
        """
        if len(sales_list) == 0:
            return make_response(jsonify({'message': "No sale has been made"}), 200)
        if admin_status is True or user_id == 'user_id':
            for sale in sales_list:
                if sale['sale_id'] == sale_id:
                    return make_response(jsonify(sale), 200)
            return make_response(jsonify({'message': 'Sale not found'}), 404)
