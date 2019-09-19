from stack import Stack

class StackNew(object):

    def __init__(self, stack):
        self.stack = stack
        self.min_element = None
        self.min_element_old = None


    def set_min_push(self, element):
        if self.stack.is_empty():
            self.min_element_old = self.min_element
            self.min_element = element

        else:
            if element < self.min_element:
                self.min_element_old = self.min_element
                self.min_element = element

        self.stack.push(element)



    def set_min_pop(self):
        value = self.stack.pop()

        if value == self.min_element:
            self.min_element = self.min_element_old


    def get_min(self):
        return self.min_element
