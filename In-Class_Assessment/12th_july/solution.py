import random as r


class Order:
    """_summary_
    """

    def __init__(self, order_id, items, status):
        self.order_id = order_id
        self.items = items
        self.status = status


class OrderFulfillmentSystem:
    def place_order(self, items: list[str]) -> str:
        return f' {items} and {order_id}'

    def process_order(self, order_id: str) -> None:
        pass

    def ship_order(self, order_id: str) -> None:
        pass

    def deliver_order(self, order_id: str) -> None:
        pass

    def get_order_status(self, order_id: str) -> str:
        pass
