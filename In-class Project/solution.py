import random as r


class Order:
    """_summary_
    """

    def __init__(self, order_id, items, status):
        self.order_id = order_id
        self.items = items
        self.status = status


class OrderFulfillmentSystem:
    def __init__(self) -> None:
        self.orders = []
    def place_order(self, order : Order) -> str:
        self.orders.append(order)
        return order.order_id

    def process_order(self, order_id: Order) -> None:
        for x in self.orders:
            if x.order_id == order_id:
                x.status = 'processing'
                break
            else:
                
    def ship_order(self, order_id: str) -> None:
        

    def deliver_order(self, order_id: str) -> None:
        pass

    def get_order_status(self, order_id: str) -> str:
        pass
