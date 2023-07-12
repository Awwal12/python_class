# Problem: Order Fulfillment System

# You are tasked with implementing an order fulfillment system for an e-commerce company. The system should allow users to place orders, process them, and track their status.
# Requirements:

# Implement a class called "Order" with the following attributes:

# order_id (string): unique identifier for each order
# items (list): a list of items included in the order
# status (string): current status of the order (e.g., "pending", "processing", "shipped", "delivered")

# Implement a class called "OrderFulfillmentSystem" with the following methods:

# place_order(items: List[str]) -> str: Creates a new order with the provided items and returns the order ID.
# process_order(order_id: str) -> None: Updates the status of the order with the given order ID to "processing".
# ship_order(order_id: str) -> None: Updates the status of the order with the given order ID to "shipped".
# deliver_order(order_id: str) -> None: Updates the status of the order with the given order ID to "delivered".
# get_order_status(order_id: str) -> str: Returns the current status of the order with the given order ID.

# Note:
# Each order should have a unique order ID, which can be generated using any method you prefer.
# The "items" attribute of an order can contain multiple items, represented as strings.
# The order status can be one of the following: "pending", "processing", "shipped", or "delivered".
# Instructions:
# Implement the classes "Order" and "OrderFulfillmentSystem" according to the given requirements.
# Test your implementation by creating orders, processing them, and checking their status.

# EXAMPLE USAGE:
# order_system = OrderFulfillmentSystem()
# order_id = order_system.place_order(["item1", "item2", "item3"])
# print(order_system.get_order_status(order_id))  # Output: "pending"

# order_system.process_order(order_id)
# print(order_system.get_order_status(order_id))  # Output: "processing"

# order_system.ship_order(order_id)
# print(order_system.get_order_status(order_id))  # Output: "shipped"

# order_system.deliver_order(order_id)
# print(order_system.get_order_status(order_id))  # Output: "delivered"
