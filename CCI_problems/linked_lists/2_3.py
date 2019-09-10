#Delete middle node into the list

#Time complexity: O(n)

def get_len(node):
    if not node:
        return None

    return 1 + get_len(node.next)


def check_middle(node, target):
    return node.value == target


def delete_middle(node, targe):
    count = get_len(node) / 2
    middle = count

    while count - 1 > 0:
        if middle == 1:
            aux_node = p_node

        p_node = node
        node = node.next
        count -= 1

    if middle % 2 == 1:
        if check_middle(node, target):
            p_node.next = node.next

    else:
        if check_middle(p_node, target):
            aux_node.next = node.next

        elif check_middle(node, target):
            p_node.next = node.next

    return node
