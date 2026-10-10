from linked_list import linked_list

class order_queue:
    def __init__(self):
        self.linked_list = linked_list()

    def enqueue(self, item):
        self.linked_list.add_last(item)

    def dequeue(self):
        if self.is_empty() or self.linked_list._head is None:
            raise IndexError("Queue is empty")
        return self.linked_list.remove_first()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.linked_list.get_head()

    def is_empty(self):
        return len(self.linked_list) == 0

    def size(self):
        return len(self.linked_list)

    def top(self):
        return getattr(self.linked_list, '_head', None)

    def __len__(self):
        return self.linked_list.size()
