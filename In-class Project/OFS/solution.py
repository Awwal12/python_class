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
    """Class where the logic happens has no arguments to be passed in however it has 5 methods 
    """

    def __init__(self) -> None:
        self.orders = []

    def place_order(self, order: Order) -> str:
        """method for placing order 

        :param order: of Class Order it gets the order object created 
        :return: it returns an int 
        """
        self.orders.append(order)
        return order.order_id

    def process_order(self, order_id: Order) -> None:
        """it prints 'processing' if condition is successful else prints something else
        """
        for i in self.orders:
            if i.order_id == order_id:
                i.status = 'processing'
                break
        else:
            print('missing or wrong id')

    def ship_order(self, order_id: str) -> None:
        """it prints 'shipped' if condition is successful else prints something else
        """
        for i in self.orders:
            if i.order_id == order_id:
                i.status = 'shipped'
                break
        else:
            print('missing or wrong id')

    def deliver_order(self, order_id: str) -> None:
        """it prints 'delivered' if condition is successful else prints something else
        """
        for i in self.orders:
            if i.order_id == order_id:
                i.status = 'delivered'
                break
        else:
            print('missing or wrong id')

    def get_order_status(self, order_id: str) -> str:
        """it prints the current status of the order object.
        """
        for i in self.orders:
            if i.order_id == order_id:
                print(i.status)
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
