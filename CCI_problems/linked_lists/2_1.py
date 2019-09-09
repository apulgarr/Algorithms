#Delete duplicates: Remove duplicates from an unsorted linked list

#Time complexity: O(n^2)
#Brute force solution with pointers

def delete_duplicates(node):
    if not node:
        return 0

    while node:
        visitor_p = node
        visitor = node.next

        while visitor:
            if node.value == visitor.value:
                    visitor_p.next = visitor.next
                    visitor = visitor_p.next

            else:
                visitor_p = visitor
                visitor = visitor.next

    return node


#Time complexity: O(n)
#Optimized

def delete_duplicates_optimized(node):
    no_duplicates = {}
    curr_node = node
    p_node = None

    while curr_node:
        if curr_node.value not in no_duplicates.keys():
            no_duplicates[curr_node.value] = True
            p_node = curr_node
            curr_node = curr_node.next

        else:
            p_node.next = curr_node.next
            curr_node = p_node.next

    return node
