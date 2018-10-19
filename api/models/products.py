"""
module products
"""

import datetime
from flask import jsonify, make_response

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
