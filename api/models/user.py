"""
module user
class with general user functions
"""

class User():
    """
    defining class User
    """
    def __init__(self, user_id, username, admin_status=False):
        """
        initializing attributes for class user
        """
        self.user_id = user_id
        self.username = username
        self.admin_status = bool(admin_status)

    def __str__(self):
        """return string rep of class"""
        return '{}'.format(self.username)
