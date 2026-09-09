class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.bottom = 0
        self.top = 1
        self.size = 0  

    def push_down(self, x):
        if self.size < self.capacity:
            self.array[self.bottom] = x
            self.bottom = (self.bottom - 1) % self.capacity
            self.size += 1
        else:
            raise OverflowError("push_down on full deque")

    def push_up(self, x):
        if self.size < self.capacity:
            self.array[self.top] = x
            self.top = (self.top + 1) % self.capacity
            self.size += 1
        else:
            raise OverflowError("push_up on full deque")

    def pop_down(self):
        if self.size == 0:
            raise IndexError("pop_down from empty deque")
        else:
            self.bottom = (self.bottom + 1) % self.capacity
            value = self.array[self.bottom]
            self.array[self.bottom] = None  
            self.size -= 1
            return value

    def pop_up(self):
        if self.size == 0:
            raise IndexError("pop_up from empty deque")
        else:
            self.top = (self.top - 1) % self.capacity
            value = self.array[self.top]
            self.array[self.top] = None  
            self.size -= 1
            return value
