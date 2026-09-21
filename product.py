class Product():
    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_id(self):
            """ Returns product's id"""
            return self.product_id
    
    def get_name(self):
            """ Returns the product's name"""
            return self.name

    def get_price(self):
          """returnss the product's price"""
          return self.price

    def __repr__(self):
            return self.name
    