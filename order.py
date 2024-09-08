class Order:
    def __init__(self, customer, coffee, price):
        from customer import Customer  # Import locally
        from coffee import Coffee  # Import locally
        
        if not isinstance(customer, Customer) or not isinstance(coffee, Coffee):
            raise ValueError("Invalid customer or coffee.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price

        coffee._orders.append(self)
       

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
