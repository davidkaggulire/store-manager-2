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
    DATABASE_URI = "postgresql://dkaggs:password@localhost/storemanagerapp"
class TestingConfig(Config):
    """
    Testing Config class
    """
    DEBUG = True
    TESTING = True
    DATABASE_URI = "postgresql://dkaggs:password@localhost/test"


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}