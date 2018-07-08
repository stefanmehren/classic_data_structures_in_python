#linked list
class Node(object):


    def __ini__(self,data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self,n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_next(self,data):
        self.data = data

class LinkedList(object):

     def __init__(self, root = None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.get_siz

    def add(self, data)
        new_node = Nod
