"""__init__.py"""

import os
from flask import Flask
from config import app_config
from flask_jwt_extended import JWTManager
from api.views.product_views import product
from api.views.sales_views import sales
from api.views.user_views import userpage


# app = Flask(__name__)
# app.config['JWT_SECRET_KEY'] = 'davidsecret123'
# jwt = JWTManager(app)
# from api.models.db import Database
# db = Database()

# db.create_user_table()
# db.create_products_table()
# db.create_sales_table()


# from api.views import product_views
# from api.views import user_views
# from api.views import sales_views

def create_app(config_name):
    app = Flask(__name__)
    """setting flask app"""
    app.config.from_object(app_config[config_name])
    app.config['JWT_SECRET_KEY'] = 'davidsecret123'
    JWTManager(app)
    from api.models.db import Database
    
    db = Database()
    db.create_user_table()
    db.create_products_table()
    db.create_sales_table()

    app.register_blueprint(product)
    app.register_blueprint(sales)
    app.register_blueprint(userpage)
  
    return app

