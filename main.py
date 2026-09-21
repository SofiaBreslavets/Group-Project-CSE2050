
import unittest

from customer import Customer
from product import Product
from cart import ShoppingCart


class test2_customer(unittest.TestCase):

    def test_customer_creation(self):
        customer = Customer("C101", "Camrin")

        self.assertEqual(customer.customer_id, "C101")
        self.assertEqual(customer.name, "Camrin")

    def test_customer_repr(self):
        customer = Customer("C101", "Camrin")

        self.assertEqual(repr(customer), "Camrin")

import unittest

from shopping_cart import ShoppingCart
from product import Product


class TestShoppingCart(unittest.TestCase):

    # Test that a new cart starts empty
    def test_new_cart_is_empty(self):
        cart = ShoppingCart()

        self.assertTrue(cart.is_empty())
        self.assertEqual(cart.get_items(), [])
        self.assertEqual(cart.calculate_total(), 0.0)

    # Test adding one product
    def test_add_product(self):
        cart = ShoppingCart()
        product = Product("P100", "Mouse", 59.99)

        cart.add_product(product)

        self.assertFalse(cart.is_empty())
        self.assertEqual(len(cart.get_items()), 1)
        self.assertIn(product, cart.get_items())

    # Test adding multiple products
    def test_add_multiple_products(self):
        cart = ShoppingCart()

        product1 = Product("P100", "Mouse", 59.99)
        product2 = Product("P101", "Keyboard", 65.99)

        cart.add_product(product1)
        cart.add_product(product2)

        self.assertEqual(len(cart.get_items()), 2)

    # Test calculating the total
    def test_calculate_total(self):
        cart = ShoppingCart()

        product1 = Product("P100", "Mouse", 59.99)
        product2 = Product("P101", "Keyboard", 65.99)

        cart.add_product(product1)
        cart.add_product(product2)

        self.assertAlmostEqual(cart.calculate_total(), 125.98)

    # Test removing a product that exists
    def test_remove_product(self):
        cart = ShoppingCart()
        product = Product("P100", "Mouse", 59.99)

        cart.add_product(product)

        result = cart.remove_product("P100")

        self.assertTrue(result)
        self.assertTrue(cart.is_empty())

    # Test removing a product that does not exist
    def test_remove_nonexistent_product(self):
        cart = ShoppingCart()
        product = Product("P100", "Mouse", 59.99)

        cart.add_product(product)

        result = cart.remove_product("P999")

        self.assertFalse(result)
        self.assertEqual(len(cart.get_items()), 1)

    # Edge case: remove from an empty cart
    def test_remove_from_empty_cart(self):
        cart = ShoppingCart()

        result = cart.remove_product("P100")

        self.assertFalse(result)
        self.assertTrue(cart.is_empty())

    # Edge case: duplicate product
    def test_duplicate_product(self):
        cart = ShoppingCart()
        product = Product("P100", "Mouse", 59.99)

        cart.add_product(product)
        cart.add_product(product)

        # Your current ShoppingCart allows duplicates
        self.assertEqual(len(cart.get_items()), 2)

    # Test that total updates after removing a product
    def test_total_after_removing_product(self):
        cart = ShoppingCart()

        product1 = Product("P100", "Mouse", 59.99)
        product2 = Product("P101", "Keyboard", 65.99)

        cart.add_product(product1)
        cart.add_product(product2)

        cart.remove_product("P100")

        self.assertAlmostEqual(cart.calculate_total(), 65.99)


class test5_edge_cases(unittest.TestCase):

    def test_empty_cart(self):
        cart = ShoppingCart()

        self.assertTrue(cart.is_empty())
        self.assertEqual(cart.get_items(), [])
        self.assertEqual(cart.calculate_total(), 0.0)

    def test_add_product(self):
        cart = ShoppingCart()
        product = Product("P100", "Mouse", 59.99)

        cart.add_product(product)

        self.assertFalse(cart.is_empty())
        self.assertEqual(len(cart.get_items()), 1)
        self.assertIn(product, cart.get_items())

    def test_add_multiple_products(self):
        cart = ShoppingCart()

        product1 = Product("P100", "Mouse", 59.99)
        product2 = Product("P101", "Keyboard", 65.99)

        cart.add_product(product1)
        cart.add_product(product2)

        self.assertEqual(len(cart.get_items()), 2)

    def test_calculate_total(self):
        cart = ShoppingCart()

        product1 = Product("P100", "Mouse", 59.99)
        product2 = Product("P101", "Keyboard", 65.99)

        cart.add_product(product1)
        cart.add_product(product2)

        self.assertAlmostEqual(cart.calculate_total(), 125.98)

    def test_remove_product(self):
        cart = ShoppingCart()
        product = Product("P100", "Mouse", 59.99)

        cart.add_product(product)

        result = cart.remove_product("P100")

        self.assertTrue(result)
        self.assertTrue(cart.is_empty())

    def test_remove_product_not_found(self):
        cart = ShoppingCart()
        product = Product("P100", "Mouse", 59.99)

        cart.add_product(product)

        result = cart.remove_product("P999")

        self.assertFalse(result)
        self.assertEqual(len(cart.get_items()), 1)

    def test_remove_from_empty_cart(self):
        cart = ShoppingCart()

        result = cart.remove_product("P100")

        self.assertFalse(result)
        self.assertTrue(cart.is_empty())

    def test_duplicate_product(self):
        cart = ShoppingCart()
        product = Product("P100", "Mouse", 59.99)

        cart.add_product(product)
        cart.add_product(product)

        # Tests the current behavior: duplicates are allowed
        self.assertEqual(len(cart.get_items()), 2)


if __name__ == "__main__":
    unittest.main()

