"""
module products
"""

import re
import datetime
from flask import jsonify

class Products():
    """
    Class defining Products 
    """
    def __init__(self, product_id, product_name, category, price, quantity, minimum_quantity):
        """
        initializing attributes for class
        """
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.minimum_quantity = minimum_quantity
        self.date_added = datetime.datetime.now()

    def __str__(self):
        """
        print string rep of class attributes
        """
        return '{}'.format(self.product_name)
        
    def validate_product(self):
        """
        method to validate product input
        """
        if re.search(r'\s', self.product_name):
            return jsonify({'error': 'product name should not have empty spaces'}), 400
        if re.search(r'\d', self.product_name):
            return jsonify({'error': 'product name should not have digits but letters'}), 400
        if re.search(r'\W', self.product_name):
            return jsonify({'error': 'product name should not contain alphabet letters only'}), 400
        if not isinstance(self.price, int):
            return jsonify({'error': 'price should be a number'}), 400
        if not isinstance(self.quantity, int):
            return jsonify({'error': 'quantity should be a number'}), 400
        if not isinstance(self.minimum_quantity, int):
            return jsonify({'error': 'minimum quantity should be a number'}), 400
        if re.search(r'\s', self.category):
            return jsonify({'error': 'category name should not have empty spaces'}), 400
        if re.search(r'\d', self.category):
            return jsonify({'error': 'category name should not have digits but letters'}), 400
        if re.search(r'\W', self.category):
            return jsonify({'error': 'product name should not contain alphabet letters only'}), 400
        return True
