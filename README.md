# store-manager-2
Store Manager helps store owners manage sales and product inventory records

[![Build Status](https://travis-ci.org/davidkaggulire/store-manager-2.svg?branch=feature-challenge-2)](https://travis-ci.org/davidkaggulire/store-manager-2)
[![Maintainability](https://api.codeclimate.com/v1/badges/50796fb3922e9c5bdab6/maintainability)](https://codeclimate.com/github/davidkaggulire/store-manager-2/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/davidkaggulire/store-manager-2/badge.svg?branch=feature-challenge-2)](https://coveralls.io/github/davidkaggulire/store-manager-2?branch=feature-challenge-2)

# Getting Started
Follow the instructions to help you get started.

# Requirements for project
 `Flask server side framework
   -- pip install flask
 `

`Python version -- python 3.5.2`

` Postman to test API endpoints`

`Pytest -- pip install -U pytest`

`Pylint -- pip install pylint`

To install dependencies run the command

`pip install -r requirements.txt`

# Installing virtual machine
To install the virtual machine run this 
command

`pip install virtualenv`


To create a virtual environment run this command

`python3 -m venv venv`

# Accessing project
https://github.com/davidkaggulire/store-manager-2/tree/feature-challenge-2

__Installing__

Please clone or download the repo at:

`https://github.com/davidkaggulire/store-manager-2.git`

# Project Functionality
- Store attendant can search and add products to buyer's cart.
- Store attendant can see his or her sale records but can't modify them.
- Store owner can see sales and filter attendants.
- Store owner can add modify and delete products.
- The application shows available products, quantity and price.

# UI link
- ` https://davidkaggulire.github.io/store-manager/UI/templates/index.html`

# Running Unit Tests
`python -m pytest tests/test_api.py`

__With Coverage__

`python -m pytest tests --cov=api `

# Endpoints

| Method        | Route           | Function  |
| ------------- |:-------------------:| -----:|
| POST  | api/v1/products   |post products      |
| GET   | api/v1/products    |get products   |
| GET   | api/v1/products/product_id  |   get product by id       |
| POST  | api/v1/sales   |post a sale        |
| GET   | api/v1/sales   |get all sales        |
| GET   | api/v1/sales/sale_id   |get sale by id        |
