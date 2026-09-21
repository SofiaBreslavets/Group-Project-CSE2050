import cart
class Customer():
    def __init__(self, customer_id: str, name: str):
        """ Initializes customer class with an id, name, and a shopping cart"""
        self.customer_id = customer_id
        self.name = name
        self.cart = cart.ShoppingCart()
        return

    def get_id(self):
        """ Returns customer's id"""
        return self.customer_id

    def get_name(self):
        """ Returns customer's name"""
        return self.name

    def get_cart(self):
        """ Returns customer's shopping cart"""
        return self.cart

    def __repr__(self):
        return self.name
