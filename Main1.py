from HW1_1 import ArrayBasedList

if __name__ == '__main__':

    korea = ArrayBasedList(10)
    korea.insertItem(4, 0)
    korea.insertItem(3, 0)
    korea.insertItem(1, 0)
    korea.insertItem(2, 1)

    korea.printMyList()

    korea.removeItem(3)
    korea.removeItem(1)
    korea.removeItem(0)

    korea.printMyList()
