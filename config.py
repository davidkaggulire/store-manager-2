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
    DATABASE_URI = "postgres://dkaggs:password@localhost/storemanagerapp"


class TestingConfig(Config):
    """
    Testing Config class
    """
    DEBUG = True
    TESTING = True
    DATABASE_URI = "postgresql://dkaggs:password@localhost/testdb"


class ProductionConfig(Config):
    """
    Production config class
    """
    DEBUG = True
    DATABASE_URI = "postgres://tpzzndqodqzjda:0f0ff18502d303dc31bc3316b54eb5afd6fb44828d274238f7846708e9ee4c75@ec2-54-235-156-60.compute-1.amazonaws.com:5432/dd38125et4t431"


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
