import random as r
"""importing random package to use for generating IDs"""
# :return: int


class Order:
    """class order has 2 arguments to take that creates the object
    """

    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.status = 'pending'


class OrderFulfillmentSystem:
    def __init__(self) -> None:
        self.orders = []

    def place_order(self, order: Order) -> str:
        self.orders.append(order)
        return order.order_id

    def process_order(self, order_id: Order) -> None:
        for x in self.orders:
            if x.order_id == order_id:
                x.status = 'processing'
                break
        else:
            print('missing or wrong id')

    def ship_order(self, order_id: str) -> None:
        for x in self.orders:
            if x.order_id == order_id:
                x.status = 'shipped'
                break
        else:
            print('missing or wrong id')

    def deliver_order(self, order_id: str) -> None:
        for x in self.orders:
            if x.order_id == order_id:
                x.status = 'delivered'
                break
        else:
            print('missing or wrong id')

    def get_order_status(self, order_id: str) -> str:
        for x in self.orders:
            if x.order_id == order_id:
                print(x.status)
                break
        else:
            print('missing or wrong id')


order1 = Order(r.randint(100000, 900000), ['egg', 'apple', 'fish'])
order_system = OrderFulfillmentSystem()
order1_id = order_system.place_order(order1)
order_system.process_order(order1_id)
order_system.get_order_status(order1_id)
order_system.ship_order(order1_id)
order_system.get_order_status(order1_id)
