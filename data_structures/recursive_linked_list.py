from linked_list import Linked_list

def iterate_linked_list(node):
    if node == None:
        return 0

    else:
        return 1 + iterate_linked_list(node.next)


def find_element(node, value):
    if node == None:
        return "Not found"

    elif node.value == value:
        return "Found it"

    else:
        return find_element(node.next, value)
