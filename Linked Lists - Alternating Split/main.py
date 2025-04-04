def alternating_split(head):
    if head is None:
        raise ValueError
    elif head.next is None:
        raise ValueError

    first = Node(head.data)
    second = Node(head.next.data)
    first_ = first
    second_ = second
    head = head.next
    is_first = True
    while head.next is not None:
        if is_first:
            first.next = Node(head.next.data)
            first = first.next
        else:
            second.next = Node(head.next.data)
            second = second.next
        is_first = not is_first
        head = head.next

    return Context(first_, second_)

    
