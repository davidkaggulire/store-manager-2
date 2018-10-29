"""user.py"""

class User:
  """class for user"""
  def __init__(self, user_id, firstname, lastname, username, password, role):
    self.user_id = user_id
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password
    self.role = role