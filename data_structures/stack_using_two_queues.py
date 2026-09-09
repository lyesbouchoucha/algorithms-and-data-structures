class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, x):
        self.items.append(x)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)
        
    def is_empty(self):
        return len(self.items) == 0
        
    def size(self):
        return len(self.items)

class StackUsing2Queues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q1.enqueue(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        while self.q1.size() > 1:
            self.q2.enqueue(self.q1.dequeue())    
        value = self.q1.dequeue()
        self.q1, self.q2 = self.q2, self.q1
        return value

    def is_empty(self):
        return self.q1.is_empty()

    def size(self):
        return self.q1.size()
