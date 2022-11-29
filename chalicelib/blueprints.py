import json

from chalice import Blueprint

extra_routes = Blueprint(__name__)


class Product:

    def __init__(self, product_id, first_name, last_name, email_id):
        self.product_id = product_id
        self.first_name = first_name
        self.last_name = last_name
        self.email_id = email_id

    def display_customer(self):
        print("Product ID:", self.product_id, "First Name:", self.first_name, "Last name", self.last_name, "Email ID",
              self.email_id)


products = [Product("mobile", "test1", "test2", "test@test.com")]


@extra_routes.route('/products')
def products():
    return {'products': {
        'count': 4
    }}
