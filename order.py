from product import Product
from customer import Customer

class Order:
    def __init__(self, order_id: str, customer: Customer, items: list[Product] | None = None): 
        self.order_id = order_id
        self.customer = customer
        self.items = items if items is not None else []
        self.status = "PENDING"

    def get_id(self):
         return self.order_id

    def get_customer(self):
        return self.customer

    def get_items(self):
        return self.items
    
    def get_status(self):
        return self.status

    def set_status(self, status: str):
        valid_statuses = {"PENDING", "PROCESSING", "COMPLETED"}
        if status not in valid_statuses:
            raise ValueError(f"Invalid status '{status}'. Must be one of: {valid_statuses}")
        self.status = status

    def calculate_total(self):
        return sum(item.price for item in self.items)
