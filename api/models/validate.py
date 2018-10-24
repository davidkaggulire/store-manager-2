""" validate.py """

from flask import jsonify, make_response

class Validate():
    """
    class to validate inputs
    """

    @staticmethod
    def validate_string(input):
        """
        function to validate 
        """
        if input.strip() == '':
            return jsonify({'error': input + "cannot be an empty string"})
        if isinstance(input, str):
            return True
        if not input.isalpha():
            return jsonify({'error': input+" should contain only alphabet letters"})
        if  input.isalnum() is True:
            return jsonify({'error': input+" should contain only alphabet letters"})
        if input.isspace() is True:
            return jsonify({'error': input+" should not be an empty string"})
        return True