from node import Node

class Stack(object):

    def __init__(self):
        self.top = None


    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node


    def pop(self):
        if self.is_empty():
            return "empty stack"

        data = self.top.value
        self.top = self.top.next
        return data


    def is_empty(self):
        return self.top == None


    def peek(self):
        if self.is_empty():
            return "empty stack"

        return self.top.value


    def iterate_stack(self, node):
        if node == None:
            return 0

        else:
            print(node.value)
            self.iterate_stack(node.next)
