from stack import Stack
from order_queue import order_queue
from customer import Customer
from product import Product
from order import Order
from customer import Customer
from order_queue import order_queue
from stack import Stack

class Store:
    def __init__(self):
        self.customers: list[Customer] = []
        self.customer_ids: list[str] = []
        self.products: list[Product] = []
        self.product_ids: list[str] = []
        self.price: list[float] = []
        self.orders: list[Order] = []
        self.checkout_queue = order_queue()
        self.processed_stack = Stack()
        self.order_counter: int = 0

    def add_customer(self, customer: Customer):
        if customer.customer_id in self.customer_ids: return False
        self.customers.append(customer)
        self.customer_ids.append(customer.customer_id)
        return True

    def add_product(self, product: Product):
        if product.product_id in self.product_ids: return False
        self.products.append(product)
        self.product_ids.append(product.product_id)
        self.price.append(product.price)
        return True 

    def find_customer(self, customer_id: str):
        return next((c for c in self.customers if c.customer_id == customer_id), None)
    
    def find_product(self, product_id: str):
        return next((p for p in self.products if p.product_id == product_id), None)

    def find_order(self, order_id: str):
        return next((o for o in self.orders if o.get_id() == order_id), None)

    def get_orders(self):
        return self.orders

    def checkout(self, customer_id: str):
        customer = self.find_customer(customer_id)
        if not customer or not getattr(customer, 'cart', None):
            return None
        
        self.order_counter += 1
        order = Order(f"ORD-{self.order_counter:03d}", customer, list(customer.cart.get_items()))
        self.orders.append(order)
        self.checkout_queue.enqueue(order)
        customer.cart.clear()
        return order

    def process_next_order(self):
        if self.checkout_queue.is_empty(): 
            return None 
        order = self.checkout_queue.dequeue()
        order.set_status("PROCESSING")
        self.processed_stack.push(order)
        return order

    def get_order_history(self):
        history = []
        curr = getattr(self.processed_stack, 'top', None)
        if curr is None and hasattr(self.processed_stack, 'linked_list'):
            curr = getattr(self.processed_stack.linked_list, '_head', None)
            
        while curr:
            history.append(curr.item)
            curr = curr.link
        return history
                return product
        return None
