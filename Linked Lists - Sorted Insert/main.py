def sorted_insert(head_, data):
    if head_ == None:
        return Node(data)
    head = head_
    if head.data > data:
            node = Node(data)
            node.next = head
            return node
    while head.next is not None:
        if head.next.data > data:
            node = Node(data)
            node.next = head.next
            head.next = node
            return head_
        else:
            head = head.next
    head.next = Node(data)
    return head_
