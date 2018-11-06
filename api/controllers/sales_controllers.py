"""sales_actions.py"""

from api.models.db import Database
from api.models.sales import Sales


class SalesController:
    """
    handles actions to be implemented from models to views
    """

    def __init__(self):
        """create initial db connection"""
        self.db_con = Database()


    def create_sale(self, product_name, quantity, total, attendant_id, product_id):
        """
        method to register a user
        """
        new_sale = Sales(product_id = product_id, total = total)

        return self.db_con.create_sale(product_name, quantity, new_sale.total, attendant_id, new_sale.product_id)

    def get_sales(self):
        """"
        method to return all sales made
        """
        return self.db_con.get_sales()

    def get_single_sale(self, sale_id):
        """
        method to return single sale
        """
        return self.db_con.get_single_sale(sale_id)

    def update_on_sale(self, product_id, quantity):
        """
        method to update on sale (it takes on quantity only)
        """
        return self.db_con.update_on_sale(product_id, quantity)