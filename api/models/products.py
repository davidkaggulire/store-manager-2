"""products.py"""

import datetime


class Products:
    """creates a product"""
    def __init__(self, product_name, category, price, quantity, minimum_quantity):
        """
        initializing attributes for class
        """
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.minimum_quantity = minimum_quantity
        self.date_added = datetime.datetime.now()
