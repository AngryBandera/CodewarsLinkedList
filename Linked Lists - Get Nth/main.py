    
def get_nth(node, index):
    head = node
    i = 0
    while head.next is not None:
        if i == index:
            print(head.data)
            return head
        i += 1
        head = head.next
    if i == index:
        return head
    raise IndexError
