"""__init__.py"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
from api.views import product_views
