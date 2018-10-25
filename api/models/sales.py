"""
module sales
"""

import re
from flask import jsonify

class Sales():
    """
    class for creating a saleorder
    """
    def __init__(self, sale_id, product_name, quantity, price):
        """
        initializing class attributes
        """
        self.sale_id = sale_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        """
        returns string representation of attributes
        """
        return '{}'.format(self.sale_id)

    def validate_sale(self):
        """function to validate sale inputs"""
        if re.search(r'\s', self.product_name):
            return jsonify({'error': 'product name should not have empty spaces'}), 400
        if re.search(r'\d', self.product_name):
            return jsonify({'error': 'product name should not have digits'}), 400
        if re.search(r'\W', self.product_name):
            return jsonify({'error': 'product name should contain alphabet letters only'}), 400
        if not isinstance(self.price, int):
            return jsonify({'error': 'price should be a number'}), 400
        if not isinstance(self.quantity, int):
            return jsonify({'error': 'quantity should be a number'}), 400
        return True
        