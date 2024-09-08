# The-_coffee_shop
The Coffee Shop - Domain Modeling
This project implements a domain model for a coffee shop using Python's object-oriented programming principles. The application allows for creating customers, coffees, and orders while maintaining relationships between these entities. The primary goal is to showcase how entities interact with each other through a well-structured class design.

Table of Contents
Project Structure
Installation
Usage
Class Descriptions
Customer
Coffee
Order
Testing
Contributing
License
Project Structure
The project structure is as follows:

css
Copy code
The-_coffee_shop/
├── src/
│   ├── coffee.py
│   ├── customer.py
│   ├── order.py
│   └── __init__.py
└── tests/
    ├── test_coffee.py
    ├── test_customer.py
    ├── test_order.py
    └── __init__.py
src/: Contains the core classes for the project (Customer, Coffee, Order).
tests/: Contains the unit tests for each class.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/The-_coffee_shop.git
cd The-_coffee_shop
Create a virtual environment and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
After setting up the environment, you can explore the different classes and their relationships.

Example
python
Copy code
from src.customer import Customer
from src.coffee import Coffee
from src.order import Order

# Create a customer and a coffee
customer = Customer("Alice")
coffee = Coffee("Espresso")

# Customer places an order
order = customer.create_order(coffee, 5.0)

# Access customer's orders
print(customer.orders())  # [<Order object>]

# Access the coffee types a customer has ordered
print(customer.coffees())  # [<Coffee object>]
Class Descriptions
Customer
The Customer class represents a customer in the coffee shop. It has the following attributes and methods:

Attributes:

_name: A string representing the customer's name (1-15 characters).
_orders: A list of orders associated with the customer.
Methods:

__init__(name): Initializes a new customer.
name: Property to get the customer's name.
create_order(coffee, price): Creates an order for a specific coffee and price, and adds it to the customer's list of orders.
orders(): Returns the list of orders associated with the customer.
coffees(): Returns a list of unique coffees the customer has ordered.
Coffee
The Coffee class represents a type of coffee in the coffee shop. It has the following attributes and methods:

Attributes:

_name: A string representing the coffee's name.
_orders: A list of orders associated with this type of coffee.
Methods:

__init__(name): Initializes a new coffee type.
name: Property to get the coffee's name.
orders(): Returns the list of orders associated with this coffee.
Order
The Order class represents an order in the coffee shop. It has the following attributes and methods:

Attributes:

_customer: A Customer object representing the customer who placed the order.
_coffee: A Coffee object representing the coffee that was ordered.
_price: A float representing the price of the order.
Methods:

__init__(customer, coffee, price): Initializes a new order. Validates that the customer is an instance of Customer, the coffee is an instance of Coffee, and the price is between 1.0 and 10.0.
customer: Property to get the customer who placed the order.
coffee: Property to get the coffee associated with the order.
price: Property to get the price of the order.
Testing
Unit tests are provided to ensure the functionality of each class. The tests are located in the tests/ directory.

To run the tests, simply execute:

bash
Copy code
pytest
This will run all tests and provide a summary of any failures or errors.

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

