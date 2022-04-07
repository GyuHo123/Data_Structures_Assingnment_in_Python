from abc import ABCMeta, abstractmethod

class MyQueue(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def len(self):
        pass

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def enqueue(self):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def printMyQueue(self):
        pass
