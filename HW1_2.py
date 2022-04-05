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
        if(self.length > j):
            current = self.head
            for i in range(j):
                current = current.next_node
            return current.data
        raise ValueError('value not in list')

    def setitem(self, val, j):
        if (self.length > j):
            current = self.head
            for i in range(j):
                current = current.next_node
            current.data = val
            return
        raise ValueError('index is out of bound')

    def insertItem(self, item, j=0):
        new_node = Node(item)
        if j == 0:
            new_node.set_next(self.head)
            self.head = new_node
            self.length += 1
            return

        elif j > 0 and j < self.length:
            current = self.head
            for i in range(j-1):
                current = current.next_node
            temp = current.next_node
            current.set_next(new_node)
            new_node.set_next(temp)
            self.length += 1


    def removeItem(self, j=0):
        if j == 0:
            self.head = self.head.next_node

        elif j <= self.length:
            current = self.head
            for i in range(j-1):
                current = current.next_node
            current.next_node = current.next_node.next_node

        elif j > self.length:
            raise ValueError('index out of bound')

        self.length -= 1



    def printMyList(self):
        curr = self.head
        while curr != None:
            print(curr.data, end = ' ')
            curr = curr.next_node
        print()

