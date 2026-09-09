class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class MergeableHeap:
    def __init__(self):
        self.head = None 
        self.tail = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head = new_node 

    def minimum(self):
        if self.head is None:
            return None
            
        current = self.head
        min_node = current
        
        while current.next is not None:
            if current.next.value < min_node.value:
                min_node = current.next 
            current = current.next 
            
        return min_node

    def extract_min(self):
        min_node = self.minimum()
        if min_node is None:
            raise ValueError("extract_min from empty heap") 
            
        # Si le minimum est la tête
        if min_node == self.head:
            self.head = min_node.next 
            if self.head is None:  
                self.tail = None
        else:
            current = self.head
            while current.next != min_node:
                current = current.next 
            current.next = min_node.next
            if min_node == self.tail:
                self.tail = current
                
        return min_node.value

    def union(self, other_heap):
        if other_heap.head is None:
            return
            
        if self.head is None:
            self.head = other_heap.head
            self.tail = other_heap.tail
        else:
            self.tail.next = other_heap.head
            self.tail = other_heap.tail
            
        other_heap.head = None
        other_heap.tail = None
