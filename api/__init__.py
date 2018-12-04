"""__init__.py"""

from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import app_config
from api.views.product_views import product
from api.views.sales_views import sales
from api.views.user_views import userpage
from api.models.db import Database


def create_app(config_name):
    app = Flask(__name__)
    """setting flask app"""
    app.config.from_object(app_config[config_name])
    app.config['JWT_SECRET_KEY'] = 'davidsecret123'
    CORS(app)
    JWTManager(app)
    Swagger(app)    
    db = Database()
    db.create_user_table()
    db.create_products_table()
    db.create_sales_table()
    app.register_blueprint(product)
    app.register_blueprint(sales)
    app.register_blueprint(userpage)
    return app
