from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    return Node(data, head)
  
def build_one_two_three():
    return Node(1, Node(2, Node(3)))
        
