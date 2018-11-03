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

LOGIN_USER = {
   "username":"dkaggs",
	"password": "dkaggs123!"
}

LOGIN_ADMIN = {
    "username":"dkaggs",
	"password": "dkaggs123!"
}


PRODUCT = {
	"product_name": "book",
	"category": "scholastic",
	"price": 5000,
	"quantity": 10,
	"minimum_quantity": 2
}

PRODUCT_LIST=[
    {
        "product_name": "book",
        "category": "scholastic",
        "price": 5000,
        "quantity": 10,
        "minimum_quantity": 2
    },
    {
        "product_name": "pen",
        "category": "scholastic",
        "price": 500,
        "quantity": 10,
        "minimum_quantity": 2
    }
]

EMPTY_PRODUCT = {
    "product_name": "",
	"category": "",
	"price": "",
	"quantity": "",
	"minimum_quantity": ""
}

SALE = {
    'product_id': 1,
    'quantity': 2
}