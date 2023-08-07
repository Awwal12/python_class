Title: Online Shopping System

Objective:
Create a Python program that simulates an Online Shopping System using Object-Oriented Programming (OOP) and SQL. The program should allow users to interact with the system by performing various tasks related to managing products, customers, and orders in an online shopping platform.

Scenario:
You are tasked with developing an Online Shopping System for a fictional e-commerce website called "SuperMart." SuperMart sells various products like electronics, clothing, books, and more. The system should allow customers to browse products, add items to their shopping cart, place orders, and view their order history.

Requirements:

1. Implement the following classes:

   - Product: Represents a product with attributes like product ID, name, category, price, and stock quantity.
   - Customer: Represents a customer with attributes like customer ID, name, email, and shipping address.
   - Order: Represents an order with attributes like order ID, order date, customer ID, and total amount.
   - OrderItem: Represents an individual item in an order with attributes like product ID, quantity, and sub-total.
   - ShoppingSystem: Represents the online shopping system and manages products, customers, and orders.

2. Use SQLite or any other SQL database for storing product, customer, order, and order item data.

   - The database should have tables for storing product, customer, order, and order item information.

3. The Product class should have the following functionalities:

   - Add a new product to the system.
   - Remove an existing product from the system.
   - Update product information (e.g., price or stock quantity).
   - Display the list of all available products.

4. The Customer class should have the following functionalities:

   - Register a new customer to the system.
   - Update customer information (e.g., email or shipping address).
   - Display the list of all registered customers.

5. The Order class should have the following functionalities:

   - Place a new order for a customer.
   - Display the order history of a specific customer.

6. Implement a user interface to interact with the Online Shopping System.

   - The user should be able to use command-line inputs to perform various tasks.

7. The program should handle possible errors gracefully and provide informative error messages.

Example Usage:

```
Welcome to SuperMart - Your Online Shopping Destination!

1. Browse products
2. Add a product to cart
3. View cart
4. Place an order
5. View order history
6. Register as a new customer
7. Update customer information
8. Exit

Please enter your choice: 1

--- Available Products ---
Product ID: 1 | Name: Laptop | Category: Electronics | Price: $800.00 | Stock Quantity: 10
Product ID: 2 | Name: T-shirt | Category: Clothing | Price: $20.00 | Stock Quantity: 50
Product ID: 3 | Name: Book | Category: Books | Price: $15.00 | Stock Quantity: 100

Please enter your choice: 2

Enter product ID to add to cart: 1
Enter quantity: 2

Product added to cart successfully!

Please enter your choice: 3

--- Shopping Cart ---
1. Product ID: 1 | Name: Laptop | Quantity: 2 | Subtotal: $1600.00

Please enter your choice: 4

Enter your customer ID: 1

Order placed successfully! Your order ID is 1001.

Please enter your choice: 5

--- Order History ---
Order ID: 1001 | Order Date: 2023-08-07 | Total Amount: $1600.00

Please enter your choice: 6

Enter your name: John Doe
Enter your email: john@example.com
Enter your shipping address: 123 Main St, City

Registration successful! Your customer ID is 1.

Please enter your choice: 8

Thank you for shopping at SuperMart! Goodbye!
```

Note:

- You can use the `sqlite3` library in Python to interact with the SQL database.
- Make sure to validate user inputs and handle exceptions appropriately.
- You can use the `argparse` library to handle command-line inputs for the user interface.
