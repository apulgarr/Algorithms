from node import Node

class Queue(object):

    def __init__(self):
        self.first = None
        self.last = None


    def add(self, value):
        if self.first == None:
            self.first = Node(value)
            self.last = self.first

        else:
            self.last.next = Node(value)
            self.last = self.last.next


    def remove(self):
        if self.is_empty():
            return "empty queue"

        if self.first == self.last:
            data = self.first.value
            self.first = None
            self.last = None
            return data

        else:
            data = self.first.value
            self.first = self.first.next
            return data


    def is_empty(self):
        return self.first == None


    def peek(self):
        if self.is_empty():
            return "empty queue"

        return self.last.value


    def iterate_queue(self, node):
        if node == None:
            return 0

        else:
            print(node.value)
            return self.iterate_queue(node.next)
