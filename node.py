class Node:
    def __init__(self, item, link = None):
        """ Initializes a node with an item and a link to the next node"""
        self.item = item
        self.link = link

    def __repr__(self):
        """ Returns string representation of node"""
        return f"Node({self.item})"
