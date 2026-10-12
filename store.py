from stack import stack
from order_queue import order_queue
from customer import Customer
from product import Product
from order import Order

class Store:
    """ Initializes a store class with customer, products, orders, and checkout queue """
    def __init__(self):
        self.customers: list[Customer] = []
        self.customer_ids: list[str] = []
        self.products: list[Product] = []
        self.product_ids: list[str] = []
        self.price: list[float] = []
        self.orders: list[Order] = []
        self.checkout_queue = order_queue()
        self.processed_stack = stack()
        self.order_counter: int = 0

    def add_customer(self, customer: Customer):
        """ Adds a customer to the store or returns false if already exists"""
        if customer.customer_id in self.customer_ids: return False
        self.customers.append(customer)
        self.customer_ids.append(customer.customer_id)
        return True

    def add_product(self, product: Product):
        """ Adds a product to the store or returns false if already exists"""
        if product.product_id in self.product_ids: return False
        self.products.append(product)
        self.product_ids.append(product.product_id)
        self.price.append(product.price)
        return True 

    def find_customer(self, customer_id: str):
        """ Returns customer object if found, otherwise returns None"""
        return next((c for c in self.customers if c.customer_id == customer_id), None)
    
    def find_product(self, product_id: str):
        """ Returns product object if found, otherwise returns None"""
        return next((p for p in self.products if p.product_id == product_id), None)

    def find_order(self, order_id: str):
        """ Returns order object if found, otherwise returns None"""
        return next((o for o in self.orders if o.get_id() == order_id), None)

    def get_orders(self):
        """ Returns a list of all orders"""
        return self.orders

    def checkout(self, customer_id: str):
        """ Adds customer's cart to checkout queue, returns the order object if successful """
        customer = self.find_customer(customer_id)
        if (not customer or not hasattr(customer, 'cart') or customer.cart.is_empty()):
            return None
        
        self.order_counter += 1
        order = Order(f"ORD-{self.order_counter:03d}", customer, list(customer.cart.get_items()))
        self.orders.append(order)
        self.checkout_queue.enqueue(order)
        customer.cart.clear()
        return order

    def process_next_order(self):
        """ Processestthe next order in the checkout queue, returns the order"""
        if self.checkout_queue.is_empty(): 
            return None 
        order = self.checkout_queue.dequeue()
        order.set_status("PROCESSING")
        self.processed_stack.push(order)
        return order
    def get_order_history(self):
        """Returns a list of processed orders in order (most recent first)"""
        history = []
        curr = self.processed_stack.linked_list._head
        while curr:
            history.append(curr.item)
            curr = curr.link
            return history
