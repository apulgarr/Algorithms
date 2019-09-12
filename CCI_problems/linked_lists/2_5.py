from linked_list import *

#Given two linked lists, sum their values and return the result node

#Time complexity: O(max(m,n))

def add_two_numbers(l1, l2):
    sum = 0
    l_aux = None

    while l1 or l2 or sum:
        if l1:
            sum += l1.value
            l1 = l1.next

        if l2:
            sum += l2.value
            l2 = l2.next

        if l_aux:
            l_aux.next = Node(sum%10)
            l_aux = l_aux.next
        else:
            l3 = Node(sum%10)
            l_aux = l3

        sum = sum / 10

    return l3
