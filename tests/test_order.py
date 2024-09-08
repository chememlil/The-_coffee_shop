import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_creation():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_price_validation():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)

def test_order_customer_validation():
    coffee = Coffee("Espresso")
    with pytest.raises(ValueError):
        Order("Not a Customer", coffee, 5.0)

def test_order_coffee_validation():
    customer = Customer("Alice")
    with pytest.raises(ValueError):
        Order(customer, "Not a Coffee", 5.0)
