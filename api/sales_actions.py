"""sales_actions.py"""

from api.models.db import Database

db = Database()
cursor = db.cur
dict_cursor = db.dict_cursor
db.create_sales_table()

class Sales_Controller:
    """
    handles actions to be implemented from models to views
    """
    @staticmethod
    def create_sale(product_name, price, quantity):
        """
        method to register a user
        """
        query = "INSERT INTO sales(product_name, price, quantity) VALUES(\
        '{}', '{}', '{}', '1', '1')".format(product_name, price, quantity)
        cursor.execute(query)
        return True