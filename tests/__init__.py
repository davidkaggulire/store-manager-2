"""module init tests"""

ADMIN_USER = {
	"firstname": "don",
	"lastname": "kaggulire",
	"username":"don",
	"password": "don1234!"
}

USER = {
	"firstname": "david",
	"lastname": "kaggulire",
	"username":"dkaggs",
	"password": "dkaggs123!"
}

INVALID_USER = {
	"lastname": "kaggulire",
	"username":"dkaggs",
	"password": "dkaggs123!"
}

USERS = [{
        "firstname": "",
        "lastname": "kaggulire",
        "username":"dkaggs",
        "password": "dkaggs123!"
    },
    {
        "firstname": "david",
        "lastname": "",
        "username":"dkaggs",
        "password": "dkaggs123!"
    },
    {
        "firstname": "david",
        "lastname": "kaggulire",
        "username":"",
        "password": "dkaggs123!"
    },
    {
        "firstname": "david",
        "lastname": "kaggulire",
        "username":"dkaggs",
        "password": ""
    }
]

LOGIN_USER = {
   "username":"dkaggs",
	"password": "dkaggs123!"
}

LOGIN_ADMIN = {
    "username":"don",
	"password": "don1234!"
}


PRODUCT = {
	"product_name": "book",
	"category": "scholastic",
	"price": 5000,
	"quantity": 10
}

PRODUCT_LIST=[
    {
        "product_name": "book",
        "category": "scholastic",
        "price": 5000,
        "quantity": 10
    },
    {
        "product_name": "pen",
        "category": "scholastic",
        "price": 500,
        "quantity": 10
    },
    {
      "product_name": "pencil",
        "category": "scholastic",
        "price": 200,
        "quantity": 0  
    }
]

EMPTY_PRODUCT = {
    "product_name": "",
	"category": "",
	"price": "",
	"quantity": ""
}

SALE = {
    'product_id': 1,
    'quantity': 2
}