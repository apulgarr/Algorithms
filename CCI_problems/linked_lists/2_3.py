from linked_list import Linked_list

#Delete middle node into the list

#Time complexity: O(n)

def get_len(node):
    if not node:
        return 0

    return 1 + get_len(node.next)


def check_middle(node, target):
    return node.value == target


def delete_middle(node, target):
    head_node = node
    middle = get_len(node)
    count = middle/2
    p_node = None

    while count > 0:
        if count == 1:
            aux_node = p_node

        p_node = node
        node = node.next
        count -= 1

    if middle % 2 == 1:
        if check_middle(node, target):
            if middle == 1:
                head_node = None

            else:
                p_node.next = node.next

    else:
        if check_middle(p_node, target):
            if middle == 2:
                head_node = head_node.next

            else:
                aux_node.next = p_node.next

        elif check_middle(node, target):
            p_node.next = node.next

    return head_node
