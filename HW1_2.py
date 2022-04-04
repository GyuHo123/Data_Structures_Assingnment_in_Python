from MyList import MyList

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(MyList):

    def __init__(self, head=None):
        self.head = None
        self.length = 0

    def len(self):
        return self.length

    def getitem(self, j):
        current = self.head
        for index in range(j+1):
            current = current.next
        return current

    def setitem(self, val, j):
        molayo = 1

    def insertItem(self, item, j=0):
        new_node = Node(item)
        if j == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        elif j != 0 or j != self.length:
            new_node.next = self.
            self. = new_node
            self.length += 1
        else:
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def removeItem(self, j=0):
        if j == 0:
            self.head = self.head.next
            return
        data = self.getitem(j-1)
        data.next_node = data.next_node.next_node

    def printMyList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next



