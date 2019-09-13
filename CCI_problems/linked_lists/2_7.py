#Return the node intersection beetwen two linked lists

#Time complexity: O(n + m)


def get_intersection(node_1, node_2):
    if not node_1 or not node_2:
        return 0

    elements = {}

    while node_1:
        elements[node_1] = True


    while node_2:
        if node_2 in elements:
            return node_2


    return "No intersection"
