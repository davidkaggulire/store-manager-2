"""
user.py
"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from api.models.db import Database

db = Database()
dict_cursor = db.dict_cursor

class User:
  """class for user"""
  def __init__(self, firstname, lastname, username, password):
    """
    initialize class attributes
    """
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password
