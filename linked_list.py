from node import Node

class linked_list:
    def __init__(self, items=None):
        self._head = self._tail = None
        self._len = 0
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        return self._len

    def get_head(self):
        if self.head is not None:
            return self.head.item
        return None
    
    def add_last(self, item):
        node = Node(item)
        if len(self) == 0:
            self._head = node
        else:
            self._tail.link = node
        self._tail = node
        self._len += 1

    def add_first(self, item):
        if len(self) == 0: 
            self.add_last(item)
        else:
            node = Node(item, link = self._head)
            self._head = node
            self._len += 1

    def remove_first(self):
        if len(self) == 0:
            raise NotImplementedError("Cant remove from empty list")
        ret = self.get_head()
        if len(self) == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.link
        self._len -= 1
        return ret
    
    def is_empty(self):
        if self.len == 0:
            return True
        else:
            False

    def size(self):
        return self._len
