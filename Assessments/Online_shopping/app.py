import mysql.connector as sql
from dotenv import load_dotenv
import os


load_dotenv()
user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')


class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity


class Customer:
    def __init__(self, customer_id, name, email, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = address


class Order:
    def __init__(self) -> None:
        pass


class DB:
    def __init__(self):
        self.__db = sql.connect(
            host=host,
            password=password,
            user=user,
            database='supermart'
        )
        self.productT = 'product'
        self.customerT = 'customer'
        self.orderT = 'orders'
        self.orderItem = 'order_item'
        self.__cursor = self.__db.cursor()

    def add_new_product(self, product: Product):
        self.__cursor.execute(
            f'INSERT INTO {self.productT} (name, category,price, stock_quantity) VALUES (%s, %s,%s,%s)', (product.product_id, product.name, product.category, product.stock_quantity))
        self.__db.commit()
