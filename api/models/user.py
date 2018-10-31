"""
user.py
"""

from api.models.db import Database

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
