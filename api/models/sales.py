"""
module sales
"""

class Sales():
    """
    class for creating a saleorder
    """
    def __init__(self, sale_id, product_id, username):
        """
        initializing class attributes
        """
        self.sale_id = sale_id
        self.product_id = product_id
        self.username = username

    def __str__(self):
        """
        returns string representation of attributes
        """
        return '{}'.format(self.sale_id)
