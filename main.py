import unittest

from customer import Customer
from product import Product
from cart import ShoppingCart


class testCustomer(unittest.TestCase):

    def test_customer_creation(self):
        """ Tests the creation of a customer and its attributes"""
        customer = Customer("C101", "Camrin")

        self.assertEqual(customer.customer_id, "C101")
        self.assertEqual(customer.name, "Camrin")

    def test_customer_repr(self):
        """ Tests the string representation of a customer"""
        customer = Customer("C101", "Camrin")

        self.assertEqual(repr(customer), "Camrin")


class testShoppingCart(unittest.TestCase):

    def test_empty_cart(self):
        """ Tests the creation of an empty shopping cart"""
        cart = ShoppingCart()

        self.assertTrue(cart.is_empty())
        self.assertEqual(cart.get_items(), [])
        self.assertEqual(cart.calculate_total(), 0.0)

    def test_add_product(self):
        """ Tests adding a product to the shopping cart"""
        cart = ShoppingCart()
        product = Product("P100", "Mouse", 59.99)

        cart.add_product(product)

        self.assertFalse(cart.is_empty())
        self.assertEqual(len(cart.get_items()), 1)

    def test_calculate_total(self):
        """ Tests the total price calculation of the shopping cart"""
        cart = ShoppingCart()

        product1 = Product("P100", "Mouse", 59.99)
        product2 = Product("P101", "Keyboard", 65.99)

        cart.add_product(product1)
        cart.add_product(product2)

        self.assertAlmostEqual(cart.calculate_total(), 125.98)

    def test_remove_product(self):
        """ Tests removing a product from the shopping cart"""
        cart = ShoppingCart()
        product = Product("P100", "Mouse", 59.99)

        cart.add_product(product)

        result = cart.remove_product("P100")

        self.assertTrue(result)
        self.assertTrue(cart.is_empty())

    def test_remove_nonexistent_product(self):
        """ Tests removing a product that doesn't exist in the shopping cart"""
        cart = ShoppingCart()

        result = cart.remove_product("P999")

        self.assertFalse(result)

    def test_remove_from_empty_cart(self):
        """ Tests removing a product from an empty shopping cart"""
        cart = ShoppingCart()

        result = cart.remove_product("P100")

        self.assertFalse(result)
        self.assertTrue(cart.is_empty())


if __name__ == "__main__":
    unittest.main()
