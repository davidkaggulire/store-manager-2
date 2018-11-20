"""Validation class"""

import re
from flask import jsonify

class Validators:
  """class for validation """

  @staticmethod
  def validate_input_string(input_string):
    """
    method to validate input for a string
    """
    if re.search(r'\s', input_string):
        return jsonify({'error': 'input should not have empty spaces'}), 400
    if re.search(r'\d', input_string):
        return jsonify({'error': 'input should not have digits but letters'}), 400
    if re.search(r'\W', input_string):
        return jsonify({'error': 'input should contain alphabet letters only'}), 400
    
  @staticmethod
  def validate_input_number(input_number):
    """validate an input that is a number"""      
    if not isinstance(input_number, int):
        return jsonify({'error': 'input should be a number'}), 400  
  
  @staticmethod
  def validate_password(password): 
    """validate """
    if not len(password) >= 6:
        return jsonify({"error": "password length should be equal or greater than 6"}), 400
    if not re.search(r'\d', password):
        return jsonify({"error": "password should contain a digit"}), 400
    if not re.search(r'\W', password):
        return jsonify({"error": "password should contain alphanumeric characters"}), 400
