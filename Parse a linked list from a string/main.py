def linked_list_from_string(s):
    last_node = None
    first_node = None
    for node in s.split(" -> "):
        if node == "None":
            break
        new_node = Node(int(node))
        if last_node is not None:
            last_node.next = new_node
        else:
            first_node = new_node
        last_node = new_node
    
    return first_node
