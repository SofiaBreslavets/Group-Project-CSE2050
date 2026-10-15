from linked_list import LinkedList

class Stack:
    def __init__(self):
        """ Initializes a stack using a linked list"""
        self.LinkedList = LinkedList()

    def push(self, item):
        """ Adds an item to the top of the stack"""
        self.LinkedList.add_first(item)
   
    def pop(self):
        """ Removes and returns the item at the top of the stack"""
        if self.is_empty():
            return None
        return self.LinkedList.remove_first()

    def peek(self):
        """ Returns the item at the top of the stack"""
        if self.is_empty():
            return None
        return self.LinkedList.get_first()

    def is_empty(self):
        """ Returns true if stack is empty and false otherwise"""
        return len(self.LinkedList) == 0

    def size(self):
        """ Returns the size of the stack"""
        return len(self.LinkedList)

    def __len__(self):
        """ Returns the length of the stack"""
        return self.LinkedList.size() 
