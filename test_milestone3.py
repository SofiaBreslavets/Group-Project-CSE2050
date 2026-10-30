import unittest
from store import Store
from algorithms import algorithms
from product import Product

class TestStore(unittest.TestCase):
    pass

class TestAlgorithms(unittest.TestCase):
    def test_recursive_total_price(self):
        products = [Product("P001", "Product 1", 10.0), Product("P002", "Product 2", 20.0)]
        self.assertEqual(algorithms.recursive_total_price(products), 30.0)

    def test_fewest_coins(self):
        coins = [1, 5, 10, 25]
        amount = 63
        self.assertEqual(algorithms.fewest_coins(coins, amount), [25, 25, 10, 1, 1, 1])

    def test_bubble_sort(self):
        products = [Product("P002", "Product 2", 20.0), Product("P001", "Product 1", 10.0)]
        sorted_products = algorithms.bubble_sort(products)
        self.assertEqual([p.product_id for p in sorted_products], ["P001", "P002"])

    def test_insertion_sort(self):
        products = [Product("P002", "Product 2", 20.0), Product("P001", "Product 1", 10.0)]
        sorted_products = algorithms.insertion_sort(products)
        self.assertEqual([p.product_id for p in sorted_products], ["P001", "P002"])

    def test_selection_sort(self):
        products = [Product("P002", "Product 2", 20.0), Product("P001", "Product 1", 10.0)]
        sorted_products = algorithms.selection_sort(products)
        self.assertEqual([p.product_id for p in sorted_products], ["P001", "P002"])

    def test_binary_search(self):
        products = [Product("P001", "Product 1", 10.0), Product("P002", "Product 2", 20.0)]
        self.assertEqual(algorithms.binary_search(products, "P001"), products[0])
        self.assertIsNone(algorithms.binary_search(products, "P003"))

