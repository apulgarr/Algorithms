class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum = 0
        l_aux = None
        
        while l1 or l2 or sum:
            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next 
                
            if l_aux:
                l_aux.next = Node(sum%10)
                l_aux = l_aux.next
            else:
                l3 = Node(sum%10)
                l_aux = l3
                
            sum = sum / 10
        
        return l3
