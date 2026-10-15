from linked_list import linked_list

class Order_queue:
    def __init__(self):
        """ Initializes an order queue using a linked list"""
        self.linked_list = linked_list()

    def enqueue(self, item):
        """ Adds an item to the end of the queue"""
        self.linked_list.add_last(item)

    def dequeue(self):
        """ Removes and returns the item at the front of the queue"""
        if self.is_empty():
            return None
        return self.linked_list.remove_first()

    def peek(self):
        """ Returns the item at the front of the queue"""
        if self.is_empty():
            return None
        return self.linked_list.get_head()

    def is_empty(self):
        """ Returns true if queue is empty, false otherwise"""
        return len(self.linked_list) == 0

    def size(self):
        """ Returns the size of the queue"""
        return len(self.linked_list)

    def __len__(self):
        """ Returns the length of the queue"""
        return self.linked_list.size()
