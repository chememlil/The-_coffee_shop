class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def create_order(self, coffee, price):
        from order import Order  # Import locally to avoid circular import
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))
