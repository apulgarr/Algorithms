from linked_list import *

#rotation: all nodes less than x come before all nodes greater than or equal to x

#Time complexity: O(n)

def rotation(pivot, node_head):
    aux_node = node_head
    p_node = None
    new_linked_list = None

    while aux_node:
        if aux_node.value < pivot:

            if not new_linked_list:
                r_new_linked = Node(aux_node.value)
                new_linked_list = r_new_linked

            else:
                new_linked_list.next = Node(aux_node.value)
                new_linked_list = new_linked_list.next


            if not p_node:
                node_head = node_head.next

            else:
                p_node.next = aux_node.next

        else:
            p_node = aux_node

        aux_node = aux_noded.next


    if not new_linked_list:
        r_new_linked = node_head

    else:
        new_linked_list.next = node_head

    return r_new_linked
