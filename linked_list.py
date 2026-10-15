from node import Node

class LinkedList:
    def __init__(self, items=None):
        """Initializes the linked list, optionally with an iterable of items."""
        self._head = None
        self._tail = None
        self._len = 0
        
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        """Returns the length of the list."""
        return self._len

    def get_head(self):
        """Returns the head item of the list."""
        if self._head is not None:
            return self._head.item
        return None

    def add_last(self, item):
        """Adds an item to the end of the list."""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            self._tail.link = node
        self._tail = node
        self._len += 1

    def add_first(self, item):
        """Adds an item to the front of the list."""
        node = Node(item, link=self._head)
        self._head = node

        if self.is_empty():
            self._tail = node
              
        self._len += 1

    def remove_first(self):
        """Removes the first item from the list and returns it."""
        if self.is_empty():
            return None
        
        head_node = self._head
        self._head = head_node.link
        ret = head_node.item if hasattr(head_node, 'item') else head_node
        
        self._len -= 1
        
        if self._head is None:
            self._tail = None
              
        return ret

    def is_empty(self):
        """Returns true if the list is empty and false otherwise."""
        return self._len == 0

    def size(self):
        """Returns the size of the list."""
        return self._len
