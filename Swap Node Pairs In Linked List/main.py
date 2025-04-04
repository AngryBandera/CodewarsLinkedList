from preloaded import Node

def swap_pairs(head):
    if head == None or head.next == None:
        return head
    head_ = head.next
    while head.next is not None:
        next = head.next.next
        head.next.next = head
        head.next = next
        if next is not None and next.next is not None:
            head.next = next.next
        else:
            head.next = next
        head = next
        if head is None or head.next is None:
            break
    return head_
