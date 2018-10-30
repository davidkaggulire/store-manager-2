"""file to handle db operations"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from api.models.db import Database

db = Database()
print(db)
cursor = db.cur
dict_cursor = db.dict_cursor
db.create_user_table()

class UserOperations():
  @staticmethod
  def check_username(username):
    """
    method to check if username exists
    """
    query = "SELECT * from users WHERE username='{}'\
    ".format(username)
    dict_cursor.execute(query)
    data = dict_cursor.fetchone()
    return data

  @staticmethod
  def check_password(password, username):
    """
    function to check user password
    """
  
    query = "SELECT password from users WHERE username='{}'\
    ".format(username)
    cursor.execute(query)
    data = cursor.fetchall()
    for d in data:
      print(d[0])
      check = check_password_hash(d[0], password)
      if check:
        return True
      else:
        return False

  
    # print(data)
    # check = check_password_hash(data['password'], password)
    # if check:
    #   return data['password']
    # else:
    #   return {"error": "Message failed"}, 401
