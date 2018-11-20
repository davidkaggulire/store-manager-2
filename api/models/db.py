"""db.py"""

import os
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from psycopg2.extras import RealDictCursor


class Database:
    """class to define databases for storemanager"""
    def __init__(self):
        """connect to the database"""
        try:
            if os.getenv('APP_SETTING') == 'testing':
                db_name = "testdb"
                user = "postgres"
                pwd = "password"
                host = "localhost"
                port = "5432"
            elif os.getenv('heroku'):
                db_name = "dd38125et4t431"
                user = "tpzzndqodqzjda"
                pwd = "0f0ff18502d303dc31bc3316b54eb5afd6fb44828d274238f7846708e9ee4c75"
                host = "ec2-54-235-156-60.compute-1.amazonaws.com"
                port = "5432"
            else:
                db_name = "storemanagerapp"
                user = "postgres"
                pwd = "password"
                host = "localhost"
                port = "5432"
            self.conn = psycopg2.connect(dbname=db_name, user=user, password=pwd, host=host, port=port)
            self.conn.autocommit = True
            self.cur = self.conn.cursor()
            self.dict_cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            print("Connected to {}".format(db_name))

        except Exception as e:
            print(e)
            print("Database connection failed")

    def create_user_table(self):
        """method to create user table"""
        user_table = ("CREATE TABLE IF NOT EXISTS users"
                        "("
                        "user_id serial PRIMARY KEY,"
                        "firstname VARCHAR (50) NOT NULL,"
                        "lastname VARCHAR (50) NOT NULL,"
                        "username VARCHAR (50) NOT NULL,"
                        "password VARCHAR (100) NOT NULL,"
                        "role VARCHAR (50) NOT NULL"
                        ")")
        self.cur.execute(user_table)

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
                        "date_created TIMESTAMP DEFAULT NOW()"
                    ")")

        self.cur.execute(products_table)

    def create_sales_table(self):
        """method to create sales table"""
        sales_table = ("CREATE TABLE IF NOT EXISTS sales"
                        "("
                        "sale_id serial PRIMARY KEY,"
                        "product_name VARCHAR (50) NOT NULL,"
                        "quantity INTEGER NOT NULL,"
                        "total INTEGER NOT NULL, "
                        "attendant_id INTEGER NOT NULL,"
                        "product_id INTEGER NOT NULL,"
                        "date TIMESTAMP DEFAULT NOW()"
                        ")")
        self.cur.execute(sales_table)

    def create_admin(self, firstname, lastname, username, password):
        """
        method to register a user
        """
        self.cur.execute("INSERT INTO users(firstname, lastname, username, password, role) VALUES(\
        %s, %s, %s, %s, 'admin')", (firstname, lastname, username, generate_password_hash(password),))

    def create_user(self, firstname, lastname, username, password):
        """
        method to register a user
        """
        self.cur.execute("INSERT INTO users(firstname, lastname, username, password, role) VALUES(\
        %s, %s, %s, %s, 'attendant')", (firstname, lastname, username, generate_password_hash(password),))

    def check_username(self, username):
        """
        method to check if username exists
        """
        self.dict_cursor.execute("SELECT * from users WHERE username=%s", (username,))
        return self.dict_cursor.fetchone()

    def check_password(self, password, username):
        """
        function to check user password
        """
        self.cur.execute("SELECT password from users WHERE username=%s", (username,))
        data = self.cur.fetchall()
        for d in data:
            check = check_password_hash(d[0], password)
            return check

    def create_product(self, product_name, category, price, quantity):
        """
        method to create products
        """
        self.cur.execute("INSERT INTO products(product_name, category, price, quantity, minimum_quantity) VALUES(\
        %s, %s, %s, %s, %s)", (product_name, category, price, quantity, 5, ))

    def get_products(self):
        """
        method that returns all products
        """
        self.dict_cursor.execute("SELECT * FROM products")
        return self.dict_cursor.fetchall()

    def get_single_product(self, product_id):
        """
        method to return a single product
        """
        self.cur.execute("SELECT * FROM products WHERE product_id=%s", (product_id,))
        return self.cur.fetchone()

    def update_product(self, product_id, product_name, category, price, quantity):
        """
        method to update a single product
        """
        self.dict_cursor.execute("UPDATE products SET product_name=%s, category=%s, price=%s, quantity=%s WHERE product_id=%s", (product_name, category, price, quantity, product_id,))

    def update_on_sale(self, product_id, quantity):
        """
        method to update on sale (it takes on quantity only)
        """
        self.dict_cursor.execute("UPDATE products SET quantity=%s WHERE product_id=%s", (quantity, product_id,))

    def check_product_name(self, product_name):
        """
        method to check if product_name exists
        """
        self.dict_cursor.execute("SELECT * from products WHERE product_name=%s", (product_name,))
        return self.dict_cursor.fetchone()

    def delete_product(self, product_id):
        """
        method to delete a product
        """
        self.cur.execute("DELETE from products WHERE product_id=%s", (product_id,))

    def create_sale(self, product_name, quantity, total, attendant_id, product_id):
        """
        method to register a user
        """
        self.cur.execute("INSERT INTO sales(product_name, quantity, total, attendant_id, product_id) VALUES(\
        %s, %s, %s, %s, %s)", (product_name, quantity, total, attendant_id, product_id))

    def get_sales(self):
        """"
        method to return all sales made
        """
        self.dict_cursor.execute("SELECT * FROM sales")
        return self.dict_cursor.fetchall()

    def get_single_sale(self, sale_id):
        """
        method to return single sale
        """
        self.cur.execute("SELECT * FROM sales WHERE sale_id=%s", (sale_id,))
        return self.cur.fetchone()

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
