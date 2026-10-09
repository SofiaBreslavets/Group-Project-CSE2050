from linked_list import linked_list

class order_queue:                          #FIFO
    def __init__(self):
        self.linked_list = linked_list()

    def enqueue(self, item):
        self.linked_list.add_last(item)

    def dequeue(self):
        self.linked_list.remove_first()

    def peek(self):
        self.linked_list.get_head()

    def is_empty(self):
        if len(self.linked_list) == 0:
            return True
        else: False

    def size(self):
        return len(self.linked_list)
