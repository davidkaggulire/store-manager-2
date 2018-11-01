# store-manager-2
Store Manager helps store owners manage sales and product inventory records

[![Build Status](https://travis-ci.org/davidkaggulire/store-manager-2.svg?branch=feat-challenge-3)](https://travis-ci.org/davidkaggulire/store-manager-2)
[![Maintainability](https://api.codeclimate.com/v1/badges/50796fb3922e9c5bdab6/maintainability)](https://codeclimate.com/github/davidkaggulire/store-manager-2/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/davidkaggulire/store-manager-2/badge.svg?branch=feature-challenge-2)](https://coveralls.io/github/davidkaggulire/store-manager-2?branch=feature-challenge-2)

# Getting Started
The following information will help you setup and run the application on your local machine.

# Prerequisites
You will need the following

- Internet
- Git
- An IDE such as Visual Studio Code
- Postman

# Project links
**UI link:** - The user interface are hosted on gh-pages on https://davidkaggulire.github.io/store-manager/UI/templates/index.html

**API Endpoints:** The code for api endpoints can be found on https://github.com/davidkaggulire/store-manager-2/tree/feature-challenge-2

# Project Functionality

**User Interface**
- Store attendant can search and add products to buyer's cart.
- Store attendant can see his or her sale records but can't modify them.
- Store owner can see sales and filter attendants.
- Store owner can add modify and delete products.
- The application shows available products, quantity and price.

**API endpoints**
- Create a product
- Get all products
- Fetch a single product record
- Create a sale order
- Fetch all sale records
- Fetch a single sale record

# Installing application on your local machine
In order to install the application, clone the remote repository to your local machine using the following command in the terminal of your IDE.

`git clone https://github.com/davidkaggulire/store-manager-2.git`

`cd` into the project directory.
When inside the application, you can then create a virtual environment by typing 

`python3 -m venv venv`.

You can now activate your virtual environment using 

`source venv/bin/activate`

# Installing dependencies
To install dependencies needed, use the following command

 `pip install -r requirements.txt`

# Running the project
Type `export FLASK_APP=run.py`

To run type `flask run`

Or simply type `python run.py`

# Running Unit Tests
You can run unit tests using this command 


`python -m pytest tests/test_api.py` 
 
 
 To check the **coverage** report using this command.


`python -m pytest tests --cov=api --cov-report term-missing`

# Deployment
The app has been deployed on heroku and can be tested using this link (https://david-store-manager.herokuapp.com/)

# Accessing Endpoints

| Method        | Route           | Function  |
| ------------- |:-------------------:| -----:|
| POST  | api/v1/products   |post products      |
| GET   | api/v1/products    |get products   |
| GET   | api/v1/products/product_id  |   get product by id       |
| POST  | api/v1/sales   |post a sale        |
| GET   | api/v1/sales   |get all sales        |
| GET   | api/v1/sales/sale_id   |get sale by id        |

# Built with:
**User Interface:**
- HTML5
- CSS3

**API endpoints:**
- Python3
- Flask

# Author:
David Kaggulire

