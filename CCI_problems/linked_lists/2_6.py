from linked_list import *

#Check if a linked list is palindrome

#Time complexity: O(n + n)

def palindrome(node):
    if not node:
        return None

    head_new_node = None
    aux_node = node

    while aux_node:
        new_node = Node(aux_node.value)
        new_node.next = head_new_node
        head_new_node = new_node

        aux_node = aux_node.next


    while node:
        if node.value.lower() != head_new_node.value.lower():
            return False

        node = node.next
        head_new_node = head_new_node.next

    return True
