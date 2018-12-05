"""products.py"""


class Products:
    """
    creates a product
    """
    def __init__(self, product_name, category, price, quantity):
        """
        initializing attributes for class
        """
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity = quantity
