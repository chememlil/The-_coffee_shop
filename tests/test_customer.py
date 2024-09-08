import pytest
from customer import Customer
from coffee import Coffee

def test_customer_creation():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_customer_orders():
    from order import Order  # Import locally to avoid circular import issues
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    assert len(customer.orders()) == 1
    assert customer.orders()[0] == order

def test_customer_coffees():
    from order import Order  # Import locally
    customer = Customer("Alice")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 6.0)
    assert len(customer.coffees()) == 2
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()
