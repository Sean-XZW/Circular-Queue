class Circularqueue(object):
    def __init__(self, n):
        self.item = [None]*n
        self.headpointer = 0
        self.tailpointer = 0
        self.size = 0

    def is_full(self):
        if self.headpointer == self.tailpointer and self.size != 0:
            return True
        else:
            return False

    def Enqueue(self, a):
        if self.is_full() == False:
            if self.headpointer <= self.tailpointer and self.tailpointer < len(self.item):
                self.item[self.tailpointer] = a
                self.size = self.size+1
                self.tailpointer = self.tailpointer + 1
                if self.tailpointer == len(self.item):
                    self.tailpointer = 0
            else:
                self.item.insert(self.tailpointer, a)
                self.item[self.tailpointer] = a
                self.size = self.size + 1
                self.tailpointer = self.tailpointer + 1

    def Dequeue(self):
        if self.size != 0:
            self.item[self.headpointer] =None
            self.size = self.size - 1
            self.headpointer = self.headpointer + 1
            if self.headpointer == len(self.item):
                self.headpointer = 0

Myqueue = Circularqueue(10)
Myqueue.Enqueue(1)
Myqueue.Enqueue(2)
Myqueue.Enqueue(3)
Myqueue.Enqueue(4)
Myqueue.Enqueue(5)
Myqueue.Enqueue(6)
Myqueue.Enqueue(10)
Myqueue.Dequeue()
Myqueue.Dequeue()
Myqueue.Dequeue()
Myqueue.Enqueue(13)
Myqueue.Enqueue(11)
Myqueue.Enqueue(12)

print(Myqueue.item)