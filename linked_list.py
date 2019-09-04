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
