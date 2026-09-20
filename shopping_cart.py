class ShoppingCart():
    def __init__(self):
        """ Initializes shopping cart class with an empty list of products"""
        self.items = []

    def add_product(self, product):
        """ Adds products to shpping cart"""
        self.items.append(product)

    def remove_product(self, product_id: str):
        """ Removes products from shopping cart, 
        returns true if product was removed and false if it isn't in the cart"""
        for product in self.items:
            if product.get_id() == product_id:
                self.items.remove(product)
                return True
        return False

    def get_items(self):
        """ Returns a list of products in the shopping cart"""
        return self.items

    def calculate_total(self):
        """ Returns total price of the products in the cart"""
        total = 0.0
        for product in self.items:
            total += product.get_price()

        return total 

    def is_empty(self):
        """ Returns true when there's no products and false otherwise"""
        return len(self.items) == 0

    