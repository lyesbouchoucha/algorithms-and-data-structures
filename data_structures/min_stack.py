class MinStack:
    """
    Stack implementation that retrieves the minimum element in O(1) time.
    """
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((x, min(x, current_min)))

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()[0]

    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self.stack[-1][0]

    def get_min(self):
        if self.is_empty():
            raise IndexError("get_min from empty stack")
        return self.stack[-1][1]
        
    def is_empty(self):
        return len(self.stack) == 0
