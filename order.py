from product import Product
from customer import Customer

class Order:
    """Initializes an order in the store"""
    def __init__(self, order_id: str, customer: Customer, items: list[Product] | None = None): 
        """ Initializes an order with id, customer, items, and status"""
        self.order_id = order_id
        self.customer = customer
        self.items = items if items is not None else []
        self.status = "PENDING"

    def get_id(self):
         """ Returns the order's id"""
         return self.order_id

    def get_customer(self):
        """ Returns the customer associated with the order"""
        return self.customer

    def get_items(self):
        """ Returns the items in the order"""
        return self.items
    
    def get_status(self):
        """ Returns status of the order"""
        return self.status

    def set_status(self, status: str):
        """ Sets the status of the order, raises order if invalid"""
        valid_statuses = {"PENDING", "PROCESSING", "COMPLETED"}
        if status not in valid_statuses:
            raise ValueError(f"Invalid status '{status}'. Must be one of: {valid_statuses}")
        self.status = status

    def calculate_total(self):
        """ Returns total price of an order"""
        return sum(item.price for item in self.items)
