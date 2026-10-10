import unittest
from store import Store
from order import Order
from order_queue import order_queue
from customer import Customer
from stack import Stack
from product import Product
from linked_list import linked_list

class TestStoreSystem(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("C99", "Jane Doe")
        self.prod1 = Product("P1", "Laptop", 1200.00)
        self.prod2 = Product("P2", "Mouse", 25.00)
        self.order = Order("ORD-001", self.customer, [self.prod1, self.prod2])

    def test_order_creation_and_status(self):
        self.assertEqual(self.order.get_id(), "ORD-001")
        self.assertEqual(self.order.status, "PENDING")
        
        self.order.set_status("COMPLETED")
        self.assertEqual(self.order.status, "COMPLETED")

        with self.assertRaises(ValueError):
            self.order.set_status("INVALID_STATUS")

    def test_order_total_and_cart_independence(self):
        self.assertEqual(self.order.calculate_total(), 1225.00)
        
        order2 = Order("ORD-002", self.customer, [self.prod2])
        self.assertEqual(order2.calculate_total(), 25.00)
        self.assertEqual(len(self.order.items), 2)

    def test_linked_list_add_first_and_last(self):
        ll = linked_list()
        ll.add_last(10)
        ll.add_last(20)
        ll.add_first(5)
        
        self.assertEqual(ll.get_head(), 5)
        self.assertEqual(ll.size(), 3)

    def test_linked_list_remove_first(self):
        ll = linked_list([10, 20, 30])
        removed = ll.remove_first()
        
        self.assertEqual(removed, 10)
        self.assertEqual(ll.get_head(), 20)
        self.assertEqual(ll.size(), 2)

    def test_linked_list_empty_and_size_behavior(self):
        ll = linked_list()
        self.assertTrue(ll.is_empty())
        self.assertEqual(ll.size(), 0)
        self.assertIsNone(ll.get_head())

        ll.add_last("Item")
        self.assertFalse(ll.is_empty())
        self.assertEqual(ll.size(), 1)

    def test_linked_list_remove_empty_error(self):
        ll = linked_list()
        with self.assertRaises(RuntimeError):
            ll.remove_first()

    def test_stack_lifo_order(self):
        stack = Stack()
        stack.push("First")
        stack.push("Second")
        
        self.assertEqual(stack.pop(), "Second")
        self.assertEqual(stack.pop(), "First")
        self.assertTrue(stack.is_empty())

    def test_stack_peek(self):
        stack = Stack()
        stack.push(100)
        stack.push(200)
        
        self.assertEqual(stack.peek(), 200)
        self.assertEqual(len(stack), 2)

    def test_stack_empty_pop_error(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_order_queue_fifo_order(self):
        queue = order_queue()
        queue.enqueue("Order_A")
        queue.enqueue("Order_B")
        
        self.assertEqual(queue.dequeue(), "Order_A")
        self.assertEqual(queue.dequeue(), "Order_B")
        self.assertTrue(queue.is_empty())

    def test_order_queue_peek(self):
        queue = order_queue()
        queue.enqueue("First_InLine")
        queue.enqueue("Second_InLine")
        
        self.assertEqual(queue.peek(), "First_InLine")
        self.assertEqual(len(queue), 2)

    def test_order_queue_empty_dequeue_error(self):
        queue = order_queue()
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_store_checkout_workflow(self):
        store = Store()
        store.add_customer(self.customer)
        self.customer.cart.add_product(self.prod1)
        
        store.checkout(self.customer.customer_id)
        self.assertFalse(store.checkout_queue.is_empty())
        self.assertEqual(store.checkout_queue.peek().get_id(), "ORD-001")

    def test_store_processing_workflow(self):
        store = Store()
        store.add_customer(self.customer)
        self.customer.cart.add_product(self.prod1)
        store.checkout(self.customer.customer_id)
        
        processed = store.process_next_order()
        self.assertEqual(processed.status, "PROCESSING")
        self.assertTrue(store.checkout_queue.is_empty())
        self.assertFalse(store.processed_stack.is_empty())

    def test_store_history_workflow(self):
        store = Store()
        store.add_customer(self.customer)
        self.customer.cart.add_product(self.prod1)
        store.checkout(self.customer.customer_id)
        store.process_next_order()
        
        history = store.get_order_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].get_id(), "ORD-001")


if __name__ == "__main__":
    unittest.main()
