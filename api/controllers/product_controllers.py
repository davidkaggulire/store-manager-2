"""product_actions.py"""

from api.models.db import Database
from api.models.products import Products


class ProductController:
    """class to implement product actions"""
    def __init__(self):
        """initialize connection to db"""
        self.db_con = Database()

    def register_product(self, product_name, category, price, quantity, minimum_quantity):
        """
        method to register products
        """
        new_product = Products(product_name, category, price, quantity, minimum_quantity)
        self.db_con.create_product(product_name=new_product.product_name, category=new_product.category, price=new_product.price, quantity=new_product.quantity, minimum_quantity=new_product.minimum_quantity)

    def get_products(self):
        """
        method that returns all products
        """
        return self.db_con.get_products()

    def get_single_product(self, product_id):
        """
        method to return a single product
        """
        return self.db_con.get_single_product(product_id)

    def edit_product(self, product_id, product_name, category, price, quantity, minimum_quantity):
        """
        method to update a single product
        """
        self.db_con.update_product(product_id, product_name, category, price, quantity, minimum_quantity)

    def check_product_name(self, product_name):
        """
        method to check if product_name exists
        """
        return self.db_con.check_product_name(product_name)

    def delete_product(self, product_id):
        """
        method to delete a product
        """
        return self.db_con.delete_product(product_id)
