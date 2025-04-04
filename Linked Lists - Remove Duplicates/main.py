class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    elif head.next is None:
        return head
    head_ = head
    while head_.next is not None:
        if head_.next.data == head_.data:
            head_.next = head_.next.next
        else:
            head_ = head_.next
    return head
