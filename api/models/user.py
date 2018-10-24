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
            return {'message': 'Please add products to store'}
        else:
            return product_list

    @staticmethod
    def get_specific_product(product_id, product_list):
        """
        method returns specific product
        """
        if len(product_list) == 0:
            return {'message': 'Please add products to store'}
        else:
            for product in product_list:
                if product['product_id'] == product_id:
                    return product
    
    @staticmethod
    def get_single_sale(sale_id, admin_status, user_id, sales_list):
        """
        method to get a specific sale
        """
        if len(sales_list) == 0:
            return {'message': "No sale has been made"}
        else:
            if admin_status is True or user_id == 'user_id':
                for sale in sales_list:
                    if sale['sale_id'] == sale_id:
                        return sale
                else: 
                   return {'message': 'Sale not found'}
            else:
                return {'message': 'You are not authorized'}