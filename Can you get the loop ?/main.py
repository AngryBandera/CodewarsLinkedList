def loop_size(node):
        slow = node
        fast = node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return 0

        count = 1
        current = slow.next
        while current != slow:
            count += 1
            current = current.next

        return count
