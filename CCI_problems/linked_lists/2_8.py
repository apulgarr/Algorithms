from linked_list import Linked_list

#Find the node where the LL gets into a loop

#Time complexity: O(n)

def get_loop(node):
    elements = {}

    while node:
        if node.value not in elements:
            elements[node.value] = True

        else:
            return node.value

        node = node.next

    return "The LL is not circular"
