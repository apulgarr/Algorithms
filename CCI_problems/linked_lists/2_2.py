#Return kth to last: Find the Kth element into the list and then return from kth to last

#Time complexity: O(n)

def find_kth_node(node, k):
    if k == 1:
        return node

    while node:
        node = node.next
        k -= 1

    return node


def kth_to_last(node):
    if not node:
        return None

    else:
        print(node.value)
        return kth_to_last(node.next)


def solution(node, k):
    node_kth = find_kth_node(node, k)
    kth_to_last(node_kth)
