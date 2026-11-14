import unittest

import algorithms
from hash_mapping import hash_mapping
from product import Product
from store import Store


def make_products(product_ids):
	return [Product(product_id, product_id, float(index))
			for index, product_id in enumerate(product_ids)]


def product_ids(products):
	return [product.product_id for product in products]


class TestMergeSort(unittest.TestCase):
	def test_empty_and_one_item(self):
		self.assertEqual(algorithms.merge_sort(None, []), [])

		product = Product("P001", "P001", 1.0)
		self.assertEqual(algorithms.merge_sort(None, [product]), [product])

	def test_reverse_order(self):
		products = make_products(["P003", "P002", "P001"])

		result = algorithms.merge_sort(None, products)

		self.assertEqual(product_ids(result), ["P001", "P002", "P003"])

	def test_duplicates(self):
		products = make_products(["P002", "P001", "P002", "P001"])

		result = algorithms.merge_sort(None, products)

		self.assertEqual(product_ids(result), ["P001", "P001", "P002", "P002"])


class TestQuickSort(unittest.TestCase):
	def test_empty_and_one_item(self):
		self.assertEqual(algorithms.quick_sort(None, []), [])

		product = Product("P001", "P001", 1.0)
		self.assertEqual(algorithms.quick_sort(None, [product]), [product])

	def test_reverse_order(self):
		products = make_products(["P003", "P002", "P001"])

		result = algorithms.quick_sort(None, products)

		self.assertEqual(product_ids(result), ["P001", "P002", "P003"])

	def test_duplicates(self):
		products = make_products(["P002", "P001", "P002", "P001"])

		result = algorithms.quick_sort(None, products)

		self.assertEqual(product_ids(result), ["P001", "P001", "P002", "P002"])


class TestQuickSelect(unittest.TestCase):
	def setUp(self):
		self.products = make_products(["P003", "P001", "P002"])

	def test_first_rank(self):
		selected = algorithms.quick_select(None, self.products.copy(), 1)

		self.assertEqual(selected.product_id, "P001")

	def test_middle_rank(self):
		selected = algorithms.quick_select(None, self.products.copy(), 2)

		self.assertEqual(selected.product_id, "P002")

	def test_invalid_rank(self):
		with self.assertRaises(ValueError):
			algorithms.quick_select(None, self.products.copy(), 0)
		with self.assertRaises(ValueError):
			algorithms.quick_select(None, self.products.copy(), len(self.products) + 1)


class CollisionKey:
	def __init__(self, value):
		self.value = value

	def __hash__(self):
		return 1

	def __eq__(self, other):
		return isinstance(other, CollisionKey) and self.value == other.value


class TestHashMapping(unittest.TestCase):
	def test_put_and_get(self):
		mapping = hash_mapping()

		mapping.put("P001", "Widget")

		self.assertEqual(mapping.get("P001"), "Widget")
		self.assertIsNone(mapping.get("missing"))

	def test_update_existing_key(self):
		mapping = hash_mapping()
		mapping.put("P001", "Old name")

		mapping.put("P001", "New name")

		self.assertEqual(mapping.get("P001"), "New name")
		self.assertEqual(len(mapping), 1)

	def test_colliding_keys_remain_retrievable(self):
		mapping = hash_mapping(size=2)
		first_key = CollisionKey("first")
		second_key = CollisionKey("second")
		mapping.put(first_key, "first value")
		mapping.put(second_key, "second value")

		self.assertEqual(mapping.get(first_key), "first value")
		self.assertEqual(mapping.get(second_key), "second value")
		self.assertEqual(len(mapping), 2)


class TestStoreIntegration(unittest.TestCase):
	def test_sorting_products(self):
		merge_store = Store()
		quick_store = Store()
		for product in make_products(["P003", "P002", "P001"]):
			merge_store.add_product(product)
		for product in make_products(["P003", "P002", "P001"]):
			quick_store.add_product(product)

		merge_store.merge_sort_products()
		quick_store.quick_sort_products()

		self.assertEqual(product_ids(merge_store.products), ["P001", "P002", "P003"])
		self.assertEqual(product_ids(quick_store.products), ["P001", "P002", "P003"])

	def test_quick_select_product(self):
		store = Store()
		for product in make_products(["P003", "P001", "P002"]):
			store.add_product(product)

		selected = store.quick_select_products(2)

		self.assertEqual(selected.product_id, "P002")

	def test_find_product_uses_hash_mapping(self):
		store = Store()
		product = Product("P001", "Widget", 4.5)
		store.add_product(product)

		self.assertIs(store.find_product("P001"), product)
		self.assertIsNone(store.find_product("missing"))


if __name__ == "__main__":
	unittest.main()
