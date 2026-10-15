from linked_list import linked_list

class OrderQueue:
    def __init__(self):
        """ Initializes an order queue using a linked list"""
        self.LinkedList = LinkedList()

    def enqueue(self, item):
        """ Adds an item to the end of the queue"""
        self.LinkedList.add_last(item)

    def dequeue(self):
        """ Removes and returns the item at the front of the queue"""
        if self.is_empty():
            return None
        return self.LinkedList.remove_first()

    def peek(self):
        """ Returns the item at the front of the queue"""
        if self.is_empty():
            return None
        return self.LinkedList.get_head()

    def is_empty(self):
        """ Returns true if queue is empty, false otherwise"""
        return len(self.LinkedList) == 0

    def size(self):
        """ Returns the size of the queue"""
        return len(self.LinkedList)

    def __len__(self):
        """ Returns the length of the queue"""
        return self.LinkedList.size()
