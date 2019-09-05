class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list(object):

    def __init__(self):
        self.head = None
        self.tail = None


    def add_node(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next


    def iterate_linked_list(self):
        current_node = self.head

        while current_node:
            print (current_node.value)
            current_node = current_node.next


    def delete_node(self, value):
        if self.head.value == value:
            aux = self.head.next
            self.head.next = None
            self.head = aux

        prev_node = self.head
        curr_node = self.head.next

        while curr_node:
            if curr_node.value == value:
                if not curr_node.next:
                    self.tail = prev_node
                    self.tail.next = None
    
                else:
                    prev_node.next = curr_node.next
                    curr_node.next = None

                break

            else:
                prev_node = curr_node
                curr_node = curr_node.next


    def delete_duplicates(self):
        curr_node = self.head

        while curr_node:
            visitor = curr_node.next
            visitor_prev = curr_node

            while visitor:

                if visitor.value == curr_node.value:
                    visitor_prev.next = visitor.next
                    visitor.next = None
                    visitor = visitor_prev.next

                else:
                    visitor_prev = visitor
                    visitor = visitor.next

            curr_node = curr_node.next


        self.iterate_linked_list()


l = Linked_list()
l.add_node(2)
l.add_node(3)
l.add_node(4)
l.add_node(8)
l.add_node(4)
l.add_node(10)
l.delete_node(8)
#l.delete_duplicates()
l.iterate_linked_list()
