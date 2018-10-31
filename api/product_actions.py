"""product_actions.py"""

from api.models.db import Database

db = Database()
cursor = db.cur
dict_cursor = db.dict_cursor
db.create_products_table()

class ProductActions:
    """class to implement product actions"""

    @staticmethod
    def create_product(product_name, category, price, quantity, minimum_quantity):
        """
        method to create products
        """
        query = "INSERT INTO products(product_name, category, price, quantity, minimum_quantity) VALUES(\
        '{}', '{}', '{}', '{}', '{}')".format(product_name, category, price, quantity, 
        minimum_quantity)
        cursor.execute(query)
        return True

    @staticmethod
    def get_products():
        """
        method that returns all products 
        """
        query = "SELECT * FROM products"
        dict_cursor.execute(query)
        products = dict_cursor.fetchall()
        return products

    @staticmethod
    def get_single_product(product_id):
        """
        method to return a single product
        """
        query = "SELECT * FROM products WHERE product_id='{}'".format(product_id)
        cursor.execute(query)
        data = cursor.fetchone()
        return data
        
    @staticmethod
    def edit_product(product_id, product_name, category, price, quantity, minimum_quantity):
        """
        method to update a single product
        """
        query = "UPDATE products SET product_name='{}', category='{}', price='{}', \
        quantity='{}', minimum_quantity='{}' WHERE product_id='{}'".format(product_name, category, price, quantity, minimum_quantity, product_id)
        dict_cursor.execute(query)
        return dict_cursor

    @staticmethod
    def check_product_name(product_name):
        """
        method to check if product_name exists
        """
        query = "SELECT * from products WHERE product_name='{}'\
        ".format(product_name)
        dict_cursor.execute(query)
        data = dict_cursor.fetchone()
        return data

    @staticmethod
    def delete_product(product_id):
        """
        method to delete a product
        """
        query = "DELETE from products WHERE product_id='{}'".format(product_id)
        cursor.execute(query)
        return cursor
    