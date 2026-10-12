from linked_list import linked_list

class order_queue:
    def __init__(self):
        """ Initializes an order queue using a linked list"""
        self.linked_list = linked_list()

    def enqueue(self, item):
        """ Adds an item to the end of the queue"""
        self.linked_list.add_last(item)

    def dequeue(self):
        """ Removes and returns the item at the front of the queue"""
        if self.is_empty() or self.linked_list._head is None:
            raise IndexError("Queue is empty")
        return self.linked_list.remove_first()

    def peek(self):
        """ Returns the item at the front of the queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.linked_list.get_head()

    def is_empty(self):
        """ Returns true if queue is empty, false otherwise"""
        return len(self.linked_list) == 0

    def size(self):
        """ Returns the size of the queue"""
        return len(self.linked_list)

    def top(self):
        """ Returns the head of the queue"""
        return getattr(self.linked_list, '_head', None)

    def __len__(self):
        """ Returns the length of the queue"""
        return self.linked_list.size()
