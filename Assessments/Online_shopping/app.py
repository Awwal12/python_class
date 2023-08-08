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

    def remove_product(self, id):
        self.__cursor.execute(
            f'DELETE FROM {self.productT} WHERE product_id = {id}')
        self.__db.commit()

    def update_product(self, product: Product):
        self.__cursor.execute(
            f'UPDATE {self.productT} SET name = {product.name}, category = {product.category}, price = {product.price}, stock_quantity = {product.stock_quantity} WHERE product_id = {product.product_id}')
        self.__db.commit()

    def get_all_data(self, tableName):
        self.__cursor.execute(f'SELECT * FROM {tableName}')
        return self.__cursor.fetchall()

    def new_customer(self, customer: Customer):
        self.__cursor.execute(f'INSERT INTO {self.customerT} (name,email,address) VALUES (%s,%s,%s)', (
            customer.name, customer.email, customer.address))
        self.__db.commit()

    def update_customer(self, customer: Customer):
        self.__cursor.execute(
            f'UPDATE {self.customerT} SET name = {customer.name}, email = {customer.email}, address = {customer.address} WHERE cust_id = {customer.customer_id}')
        self.__db.commit()
