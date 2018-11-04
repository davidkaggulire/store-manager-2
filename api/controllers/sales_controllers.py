"""sales_actions.py"""

from api.models.db import Database

db = Database()
cursor = db.cur
dict_cursor = db.dict_cursor
db.create_sales_table()

class SalesController:
    """
    handles actions to be implemented from models to views
    """
    @staticmethod
    def create_sale(product_name, quantity, total, attendant_id, product_id):
        """
        method to register a user
        """
        cursor.execute("INSERT INTO sales(product_name, quantity, total, attendant_id, product_id) VALUES(\
        %s, %s, %s, %s, %s)",(product_name, quantity, total, attendant_id, product_id))
        return True

    @staticmethod
    def get_sales():
        """"
        method to return all sales made
        """
        dict_cursor.execute("SELECT * FROM sales")
        return dict_cursor.fetchall()


    @staticmethod
    def get_single_sale(sale_id):
        """
        method to return single sale
        """
        cursor.execute("SELECT * FROM sales WHERE sale_id=%s",(sale_id,))
        return cursor.fetchone()