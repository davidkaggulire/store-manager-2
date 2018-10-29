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
        return jsonify({'error': input_string+' should not have empty spaces'}), 400
    if re.search(r'\d', input_string):
        return jsonify({'error': input_string+' should not have digits but letters'}), 400
    if re.search(r'\W', input_string):
        return jsonify({'error': input_string+' should not contain alphabet letters only'}), 400
    return True
    
  @staticmethod
  def validate_input_number(input_number):
    """validate an input that is a number"""      
    if not isinstance(input_number, int):
        return jsonify({'error': input_number+' should be a number'}), 400  
    return True

  