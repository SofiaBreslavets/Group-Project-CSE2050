from linked_list import linked_list

class Stack:
    def __init__(self):
        """ Initializes a stack using a linked list"""
        self.linked_list = linked_list()

    def push(self, item):
        """ Adds an item to the top of the stack"""
        self.linked_list.add_first(item)
   
    def pop(self):
        """ Removes and returns the item at the top of the stack"""
        if self.is_empty():
            return None
        return self.linked_list.remove_first()

    def peek(self):
        """ Returns the item at the top of the stack"""
        if self.is_empty():
            return None
        return self.linked_list.get_head()

    def is_empty(self):
        """ Returns true if stack is empty and false otherwise"""
        return len(self.linked_list) == 0

    def size(self):
        """ Returns the size of the stack"""
        return len(self.linked_list)

    def __len__(self):
        """ Returns the length of the stack"""
        return self.linked_list.size() 
