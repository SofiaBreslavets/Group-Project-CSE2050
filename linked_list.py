from node import Node

class linked_list:
    def __init__(self, items=None):
        """Initializes a linked list"""
        self._head = self._tail = None
        self._len = 0
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        """ Returns the length of the list"""
        return self._len

    def get_head(self):
        """ Returns the head of the list"""
        if self._head is not None:
            return self._head.item
        return None

    def add_last(self, item):
        """ Adds an item to the end of the list"""
        node = Node(item)
        if len(self) == 0:
            self._head = node
        else:
            self._tail.link = node
        self._tail = node
        self._len += 1

    def add_first(self, item):
        """ Adds an item to the front of the list"""
        if len(self) == 0:
            self.add_last(item)
        else:
            node = Node(item, link=self._head)
            self._head = node
            self._len += 1

    def remove_first(self):
        """ Removes the first item from the list and returns it"""
        if self._head is None or self.is_empty():
            raise RuntimeError("Cant remove from empty list")
        
        head_node = self._head
        ret = head_node.item if hasattr(head_node, 'item') else head_node
        
        self._head = self._head.link
        self._len -= 1
        
        if self._head is None:
            self._tail = None
            
        return ret
    
    def is_empty(self):
        """ returns true of the ist is empty and false otherwise"""
        return self._len == 0

    def size(self):
        """ Returns the size of the list"""
        return self._len
