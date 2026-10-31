import unittest
from store import Store
import algorithms
from product import Product

class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()

    def add_products(self):
        products = [
            Product("P002", "Product 2", 10.0),
            Product("P001", "Product 1", 20.0),
            Product("P003", "Product 3", 5.0),
        ]
        for product in products:
            self.store.add_product(product)

    def test_bubble_sort_products(self):
        self.add_products()

        self.store.bubble_sort_products()

        self.assertEqual([product.product_id for product in self.store.products], ["P001", "P002", "P003"])

    def test_selection_sort_products(self):
        self.add_products()

        self.store.selection_sort_products()

        self.assertEqual([product.product_id for product in self.store.products], ["P001", "P002", "P003"])

    def test_insertion_sort_products(self):
        self.add_products()

        self.store.insertion_sort_products()

        self.assertEqual([product.product_id for product in self.store.products], ["P001", "P002", "P003"])

    def test_binary_search_product(self):
        self.add_products()
        self.store.insertion_sort_products()

        self.assertIs(self.store.binary_search_product("P002"), self.store.products[1])
        self.assertIsNone(self.store.binary_search_product("P004"))

    def test_recursive_catalog_total(self):
        self.add_products()

        self.assertEqual(self.store.recursive_catalog_total(), 35.0)

    def test_calculate_change(self):
        self.assertEqual(self.store.calculate_change([1, 5, 10, 25], 63), [25, 25, 10, 1, 1, 1])

    def test_sort_products_with_empty_catalog(self):
        self.store.bubble_sort_products()
        self.store.selection_sort_products()
        self.store.insertion_sort_products()

        self.assertEqual(self.store.products, [])

    def test_binary_search_product_with_empty_catalog(self):
        self.assertIsNone(self.store.binary_search_product("P001"))

    def test_calculate_change_edge_cases(self):
        self.assertEqual(self.store.calculate_change([1, 5, 10], 0), [])
        self.assertEqual(self.store.calculate_change([2, 4], 3), [])

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


