"""db.py"""

import os
import psycopg2
from psycopg2.extras import RealDictCursor
from config import TestingConfig, DevelopmentConfig

# app.config.from_object(TestingConfig)
class Database:
  """class to define databases for storemanager"""
  def __init__(self):
    """connect to the database"""
    try:
        if os.getenv('APP_SETTING') == 'Testing':
            db_name = "test"
        else:
            db_name = "storemanagerapp"
        self.conn = psycopg2.connect(dbname=db_name, user="postgres", password="password",\
        host="localhost", port="5432")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        print("Connected to {}".format(db_name))

    except Exception:
        print("Database connection failed")
    
  def create_user_table(self):
    """method to create user table"""
    user_table =("CREATE TABLE IF NOT EXISTS users"
                "("
                  "user_id serial PRIMARY KEY,"
                  "firstname VARCHAR (50) NOT NULL,"
                  "lastname VARCHAR (50) NOT NULL,"
                  "username VARCHAR (50) NOT NULL,"
                  "password VARCHAR (100) NOT NULL,"
                  "role VARCHAR (50) NOT NULL"
                ")")
    self.cur.execute(user_table)
    return True

  def create_products_table(self):
    """method to create products table"""
    products_table = ("CREATE TABLE IF NOT EXISTS products"
                    "("
                      "product_id serial PRIMARY KEY,"
                      "product_name VARCHAR (50) NOT NULL,"
                      "category VARCHAR (50) NOT NULL,"
                      "price INTEGER NOT NULL,"
                      "quantity INTEGER NOT NULL,"
                      "minimum_quantity INTEGER NOT NULL,"
                      "time TIMESTAMP DEFAULT NOW()"
                    ")")

    self.cur.execute(products_table)
    return True

  def create_sales_table(self):
    """method to create sales table"""
    sales_table = ("CREATE TABLE IF NOT EXISTS sales"
                    "("
                      "sale_id serial PRIMARY KEY,"
                      "product_name VARCHAR (50) NOT NULL,"
                      "quantity INTEGER NOT NULL,"
                      "total INTEGER NOT NULL, "
                      "user_id INTEGER,"
                      "product_id INTEGER,"
                      "date TIMESTAMP DEFAULT NOW()"
                    ")")
    self.cur.execute(sales_table)
    return True

  def drop_table_user(self):
    """method to drop tables"""
    drop_user = "DROP TABLE IF EXISTS users CASCADE"
    self.cur.execute(drop_user)

  def drop_table_products(self):
    """method to drop table sales"""
    drop_user = "DROP TABLE IF EXISTS products CASCADE"
    self.cur.execute(drop_user)

  def drop_table_sales(self):
    """method to drop table sales"""
    drop_user = "DROP TABLE IF EXISTS sales CASCADE"
    self.cur.execute(drop_user)
