"""file to handle db operations"""

from api.models.user import User
from api.models.db import Database


class UserController:
    """
    class to handle user specific operations
    """
    def __init__(self):
        """
        initialize variables
        """
        self.db_con = Database()

    def register_user(self, firstname, lastname, username, password):
        """
        method to register a user
        """
        new_user = User(firstname, lastname, username, password)
        return self.db_con.create_user(firstname=new_user.firstname, lastname=new_user.lastname, username=new_user.username, password=new_user.password)

    def register_admin(self, firstname, lastname, username, password):
        """
        method to register an admin
        """
        new_admin = User(firstname, lastname, username, password)
        return self.db_con.create_admin(firstname=new_admin.firstname, lastname=new_admin.lastname, username=new_admin.username, password=new_admin.password)

    def correct_username(self, username):
        """
        method to check if username exists
        """
        return self.db_con.check_username(username)

    def correct_password(self, password, username):
        """
        function to check user password
        """
        return self.db_con.check_password(password, username)
