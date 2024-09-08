import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_creation():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("Ex")

def test_coffee_orders():
    coffee = Coffee("Espresso")
    customer = Customer("Alice")
    order = customer.create_order(coffee, 5.0)
    assert len(coffee.orders()) == 1
    assert coffee.orders()[0] == order

def test_coffee_customers():
    coffee = Coffee("Espresso")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)
    assert len(coffee.customers()) == 2
    assert customer1 in coffee.customers()
    assert customer2 in coffee.customers()

def test_average_price():
    coffee = Coffee("Espresso")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 7.0)
    assert coffee.average_price() == 6.0
