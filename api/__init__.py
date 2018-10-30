"""__init__.py"""

import os
from flask import Flask

app = Flask(__name__)
from api.views import product_views
from api.views import user_views

def create_app(app):
  """setting flask app"""
  config_name = os.getenv('FLASK_CONFIGURATION', 'default')
  app.config.from_object('config.DevelopmentConfig')
  