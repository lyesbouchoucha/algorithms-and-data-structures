class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class LinkedListSet:
   
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

def union_sets(s1, s2):
    """
    Unions of two LinkedListSets by appending s2 at the end of s1. 
    Time Complexity: O(1)
    """
    if s1.head is None:
        s1.head = s2.head
        s1.tail = s2.tail
        return s1
        
    if s2.head is None:
        return s1
        
    s1.tail.next = s2.head
    
    s1.tail = s2.tail 
    
    s2.head = None
    s2.tail = None
    
    return s1

    print("None")
