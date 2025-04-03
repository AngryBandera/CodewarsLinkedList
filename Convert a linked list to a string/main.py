def stringify(node):
    head = node
    nodes = str(head.data)
    while head.next is not None:
        head = head.next
        nodes += " -> "+ str(head.data)
    return nodes + " -> None"
