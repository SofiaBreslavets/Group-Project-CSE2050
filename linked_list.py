from node import Node

class linked_list:
    def __init__(self, items=None):
        """Initializes a linked list"""
        self._head = None
        self._tail = None
        self._len = 0

        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        """Returns the length of the list"""
        return self._len

    def get_first(self):
        """Returns the item at the head of the list"""
        return self._head.item if self._head else None

    def add_last(self, item):
        """Adds an item to the end of the list"""
        node = Node(item)

        if self._len == 0:
            self._head = node
        else:
            self._tail.link = node

        self._tail = node
        self._len += 1

    def add_first(self, item):
        """Adds an item to the front of the list"""
        node = Node(item, link=self._head)
        self._head = node

        if self._len == 0:
            self._tail = node

        self._len += 1

    def remove_first(self):
        """Removes the first item from the list and returns it"""
        if self._len == 0:
            raise RuntimeError("Cant remove from empty list")

        node = self._head
        self._head = node.link
        self._len -= 1

        if self._len == 0:
            self._tail = None

        return node.item

    def is_empty(self):
        """Returns true if the list is empty"""
        return self._len == 0

    def size(self):
        """Returns the size of the list"""
        return self._len
