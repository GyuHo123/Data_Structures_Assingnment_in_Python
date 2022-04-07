from MyQueue import MyQueue

class Node(object):

    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedListBasedQueue(MyQueue):

    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None
        self.length = 0

    def len(self):
        return self.length

    def first(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.head.data

    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.length += 1

    def dequeue(self, j=0):
        if self.is_empty():
            print("This is Empty, So can't dequeue")
        else:
            self.head = self.head.next_node
            self.length -= 1

    def printMyQueue(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.next_node
        print(" ")


