from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    if head is None:
        return Node(data)
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    head = Node(3)
    for i in range(2, 0, -1):
        node = Node(i)
        node.next = head
        head = node
        
    return head
        
