"""
module config
"""

class Config:
    """
    parent config class
    """

    DEBUG = False

class DevelopmentConfig(Config):
    """
    development config class
    """
    DEBUG = True

class TestingConfig(Config):
    """
    Testing Config class
    """
    DEBUG = True
    TESTING = True
