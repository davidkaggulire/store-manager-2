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
        cursor.execute("INSERT INTO products(product_name, category, price, quantity, minimum_quantity) VALUES(\
        %s, %s, %s, %s, %s)", (product_name, category, price, quantity, minimum_quantity,))
        return True

    @staticmethod
    def get_products():
        """
        method that returns all products 
        """
        dict_cursor.execute("SELECT * FROM products")
        return dict_cursor.fetchall()

    @staticmethod
    def get_single_product(product_id):
        """
        method to return a single product
        """
        cursor.execute("SELECT * FROM products WHERE product_id=%s",(product_id,))
        return cursor.fetchone()
        
    @staticmethod
    def edit_product(product_id, product_name, category, price, quantity, minimum_quantity):
        """
        method to update a single product
        """
        dict_cursor.execute("UPDATE products SET product_name=%s, category=%s, price=%s, quantity=%s,\
        minimum_quantity=%s WHERE product_id=%s", (product_name, category, price, quantity, minimum_quantity, product_id,))
        return True

    @staticmethod
    def update_on_sale(product_id, quantity):
        """
        method to update on sale (it takes on quantity only)
        """
        dict_cursor.execute("UPDATE products SET quantity=%s WHERE product_id=%s", (quantity, product_id,))
        return True

    @staticmethod
    def check_product_name(product_name):
        """
        method to check if product_name exists
        """
        dict_cursor.execute("SELECT * from products WHERE product_name=%s",(product_name,))
        return dict_cursor.fetchone()

    @staticmethod
    def delete_product(product_id):
        """
        method to delete a product
        """
        cursor.execute("DELETE from products WHERE product_id=%s", (product_id,))
        return True
    