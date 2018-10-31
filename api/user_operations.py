"""file to handle db operations"""
import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from api.models.db import Database

db = Database()
cursor = db.cur
dict_cursor = db.dict_cursor
db.create_user_table()

class UserOperations():
  """
  class to handle user specific operations
  """
  @staticmethod
  def create_user(firstname, lastname, username, password):
    """
    method to register a user
    """
    query = "INSERT INTO users(firstname, lastname, username, password, role) VALUES(\
    '{}', '{}', '{}', '{}', 'attendant')".format(firstname, lastname, username, 
    generate_password_hash(password))
    cursor.execute(query)
    return True

  @staticmethod
  def create_admin( firstname, lastname, username, password):
    """
    method to register an admin
    """
    query = "INSERT INTO users(firstname, lastname, username, password, role) VALUES(\
    '{}', '{}', '{}', '{}', 'admin')".format(firstname, lastname, username, generate_password_hash(password))
    cursor.execute(query)
    return True


  @staticmethod
  def check_username(username):
    """
    method to check if username exists
    """
    query = "SELECT * from users WHERE username='{}'".format(username)
    dict_cursor.execute(query)
    data = dict_cursor.fetchone()
    return data

  @staticmethod
  def check_password(password, username):
    """
    function to check user password
    """ 
    query = "SELECT password from users WHERE username='{}'".format(username)
    cursor.execute(query)
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
    query = "SELECT role from users WHERE username='{}'".format(username)
    cursor.execute(query)
    data = cursor.fetchall()
    for id in data:
      print(id[0])
      return id[0]
