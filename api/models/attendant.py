"""
module attendant
"""

from flask import jsonify, make_response
from api.models.user import User
from api.models.products import Products

class Attendant(User):
    """
    defining attendant class
    """
    def __init__(self, user_id, username = 'attendant', admin_status=False):
        """
        defining class attributes for attendant
        initializing attributes of user_class
        """
        super().__init__(user_id, username)

    def __str__(self):
        """
        returning str repr for class
        """
        return '{}'.format(self.username)
