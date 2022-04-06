from MyList import MyList
class Node(object):
    def __init__(self, data = None, next_node = None, previous_node = None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next
    def get_previous(self):
        return self.previous_node
    def set_previous(self, new_next):
        self.previous_node = new_next

class DoublyLinkedList(MyList):
    def __init__(self, head=None):
        self.head = None
        self.length = 0

    def len(self):
        return self.length

    def getitem(self, j):
        if (self.length > j):
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
            if self.head is None:
                self.head = new_node
                self.length += 1
                return
            else:
                self.head.previous_node = new_node
                new_node.next_node = self.head
                self.head = new_node
                self.length += 1
                return
        elif j < self.length - 1:
            current = self.head
            for i in range(j - 1):
                current = current.next_node
            temp = current.next_node
            current.set_next(new_node)
            new_node.set_previous(current)
            new_node.set_next(temp)
            temp.set_previous(new_node)
            self.length += 1
        elif j == self.length-1:
            current = self.head
            for i in range(j - 1):
                current = current.next_node
            current.next_node = new_node
            new_node.previous_node = current
            self.length += 1

    def removeItem(self, j=0):
        if j == 0:
            if self.length == 1:
                new_node = self.head.previous_node
                new_node = None
                self.head = new_node
                print("No data")
                self.length -= 1
            else:
                self.head = self.head.next_node
                self.head.previous_node = None
                self.length -= 1

        elif j > 0 and j < self.length-1:
            current = self.head
            for i in range(j):
                current = current.next_node
            current.previous_node.set_next(current.next_node)
            current.next_node.set_previous(current.previous_node)
            self.length -= 1

        elif j == self.length-1:
            current = self.head
            for i in range(j):
                current = current.next_node
            current.previous_node.next_node = None
            self.length -= 1

        elif j >= self.length:
            raise ValueError('index out of bound')

    def printMyList(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.next_node
        print(" ")







