from customer import Customer
from product import Product
class Store():
    def __init__(self):
        """initializes the store"""
        self.customers = []
        self.customer_ids = []
        self.products = []
        self.product_ids = []
        self.price = []

    def add_customer(self, customer: Customer):
        """Adds customer to database"""
        if customer.customer_id in self.customer_ids:
                            return False
        self.customers.append(customer)
        self.customer_ids.append(customer.customer_id)
        return True

    def add_product(self, product: Product):
        """Adds product to database"""
        if product.product_id in self.product_ids:
                    return False

        self.products.append(product)
        self.product_ids.append(product.product_id)
        self.price.append(product.price)
        return True 
    def find_customer(self, customer_id: str):
        """finds customer by id"""
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None
    
    def find_product(self, product_id: str):
        """Finds product by id"""
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
