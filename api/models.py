"""db_models.py"""

import psycopg2
from psycopg2.extras import RealDictCursor
from api import app
from config import DevelopmentConfig

app.config.from_object(DevelopmentConfig)

class Database:
  """class to define databases for storemanager"""
  def __init__(self):
    """connect to the database"""
    try:
        self.conn = psycopg2.connect(dbname="store", user="postgres", password="password",\
        host="localhost", port="5432")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        print("Connected to database")

    except Exception:
      print("Database connection failed")
    
  def create_user_table(self):
    """creating user table"""
    user_table =("CREATE TABLE IF NOT EXISTS users"
                "("
                  "user_id serial PRIMARY KEY,"
                  "username VARCHAR (50) NOT NULL,"
                  "password VARCHAR (25) NOT NULL,"
                  "user_role VARCHAR (50) NOT NULL"
                ")")
    self.cur.execute(user_table)
    return True

  def create_products_table(self):
    """creating products table"""
    products_table = ("CREATE TABLE IF NOT EXISTS products"
                    "("
                      "product_id serial PRIMARY KEY,"
                      "product_name VARCHAR (50) NOT NULL,"
                      "category VARCHAR (50) NOT NULL,"
                      "price INTEGER NOT NULL,"
                      "quantity INTEGER NOT NULL,"
                      "minimum_quantity INTEGER NOT NULL,"
                      "time TIMESTAMP NOT NULL,"
                      "user_id INTEGER, FOREIGN KEY (user_id) REFERENCES users(user_id)"
                    ")")

    self.cur.execute(products_table)
    return True

  def create_sales_table(self):
    """creating sales table"""
    sales_table = ("CREATE TABLE IF NOT EXISTS sales"
                  "("
                    "sale_id serial PRIMARY KEY,"
                    "price INTEGER NOT NULL,"
                    "quantity INTEGER NOT NULL,"
                    "time TIMESTAMP NOT NULL,"
                    "user_id INTEGER, FOREIGN KEY (user_id) REFERENCES users(user_id),"
                    "product_id INTEGER, FOREIGN KEY (product_id) REFERENCES products(product_id)"
                  ")")
    self.cur.execute(sales_table)
    return True
