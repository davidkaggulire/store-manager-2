"""file to handle db operations"""
import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from api.models.user import User
from api.models.db import Database

db = Database()
cursor = db.cur
dict_cursor = db.dict_cursor
db.create_user_table()

class UserController(User):
    """
    class to handle user specific operations
    """



    @staticmethod
    def create_user(firstname, lastname, username, password):
        """
        method to register a user
        """
        cursor.execute("INSERT INTO users(firstname, lastname, username, password, role) VALUES(\
        %s, %s, %s, %s, 'attendant')", (firstname, lastname, username, 
        generate_password_hash(password),))
        return True

    @staticmethod
    def create_admin( firstname, lastname, username, password):
        """
        method to register an admin
        """
        cursor.execute("INSERT INTO users(firstname, lastname, username, password, role) VALUES(\
        %s, %s, %s, %s, 'admin')", (firstname, lastname, username, generate_password_hash(password),))
        return True

    @staticmethod
    def check_username(username):
        """
        method to check if username exists
        """
        dict_cursor.execute("SELECT * from users WHERE username=%s", (username,))
        return dict_cursor.fetchone()

    @staticmethod
    def check_password(password, username):
        """
        function to check user password
        """ 
        cursor.execute("SELECT password from users WHERE username=%s", (username,))
        data = cursor.fetchall()
        for d in data:
            check = check_password_hash(d[0], password)
            if check:
                return True
            else:
                return False

    @staticmethod
    def get_user_by_role(username):
        """
        get user by id
        """
        cursor.execute("SELECT role from users WHERE username=%s", (username,))
        data = cursor.fetchall()
        for id in data:
            return id[0]
