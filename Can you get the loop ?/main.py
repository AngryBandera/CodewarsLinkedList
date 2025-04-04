def loop_size(node):
    head = node.next
    traversed_nodes = node
    i = 0
    while True:
        if is_in_traversed(traversed_nodes, head, i):
            return i
        traversed_nodes.next = head
        head = head.next
        i += 1
        

def is_in_traversed(traversed, node, i):
    head = traversed
    if node is traversed:
        print(1)
        return True
    i_ = 1
    while head.next is not None and i_ < i:
        i_ += 1
        print(str(i_) + " ##")
        if node == head.next:
            print('ended')
            return True
        head = head.next
    
    return False
