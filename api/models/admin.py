"""
module admin
"""

from api.models.user import User

class Admin(User):
    """
    defining admin class
    """
    def __init__(self, user_id, username, admin_status=True):
        """
        initializing attributes for admin user
        """
        super().__init__(user_id, username)
        self.username = 'admin'
        self.admin_status = True
        
    def __str__(self):
        """return string rep of class"""
        return '{}'.format(self.username)

    @staticmethod
    def add_product(product, product_list):
        """
        method to add products
        """
        response = {
            'product_id': product.product_id,
            'product_name': product.product_name,
            'category': product.category,
            'quantity': product.quantity,
            'minimum_quantity': product.minimum_quantity,
            'price': product.price
        }
        product_list.append(response)
        return "Product added successfully"

    @staticmethod
    def get_all_sales(sales_list):
        """
        method to get all sale orders
        """
        if len(sales_list) == 0:
            message = {
                'message': 'First make a sale'
                }
            return message
        else:
            return sales_list
            