from stack import Stack

class StackNew(object):

    def __init__(self, stack):
        self.stack = stack
        self.min_element = None


    def set_min(self, element):
        if self.stack.is_empty():
            self.min_element = element

        else:
            if element < self.min_element:
                min_element = element

        self.stack.push(element)


    def get_min(self):
        return self.min_element
