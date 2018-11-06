"""sales.py"""


class Sales:
    """class to define a sale"""
    def __init__(self, product_id, total):
        """initializing variables"""
        self.product_id = product_id
        self.total = total
