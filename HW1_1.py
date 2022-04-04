from MyList import MyList


class ArrayBasedList(MyList):

    length = 0

    def __init__(self, size):
        self.item = size*[None]
        self.length = 0

    def len(self):
        return self.length

    def getitem(self, j):
        if (self.length > j):
            return self.item[j]
        raise ValueError('value not in list')

    def setitem(self, val, j):
        if (self.length > j):
            self.item[j] = val
            return
        raise ValueError('index is out of bound')

    def insertItem(self, item, j=0):
        try:
            for i in range(self.length, j, -1):
                self.item[i] = self.item[i-1]
            self.item[j] = item
            self.length += 1
        except IndexError:
            self.item = self.item + [None] * self.length

    def removeItem(self, j=0):
        for i in range(self.length, j, -1):
            self.item[i] = self.item[i+1]
        self.length -= 1
        return

    def printMyList(self):
            print(self.item)
            print(" ")





