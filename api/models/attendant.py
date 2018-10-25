"""
module attendant
"""

from api.models.user import User

class Attendant(User):
    """
    defining attendant class
    """
    def __init__(self, user_id, username='attendant', admin_status=False):
        """
        defining class attributes for attendant
        initializing attributes of user_class
        """
        super().__init__(user_id, username)

    @staticmethod
    def add_sale(sale_id, quantity, price, product_list, sales_list, attendant_id, product_name):
        """
        method to add a sale order
        """
        # parsing in an attendant from whom Id is gotten
        for product in product_list:
            if product['product_name'] == product_name:
                response = {
                    'sale_id': sale_id,
                    'product_name': product['product_name'],
                    'price': price,
                    'quantity': quantity,
                    'category': product['category'],
                    'attendant_id': attendant_id
                }
                sales_list.append(response)
                return 'Sale made successfully'
