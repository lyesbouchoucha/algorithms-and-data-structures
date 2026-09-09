## Problem Statement
The dynamic-set operation `UNION` takes two disjoint sets $S_1$ and $S_2$ as input, and it returns a set $S = S_1 \cup S_2$ consisting of all the elements of $S_1$ and $S_2$. The sets $S_1$ and $S_2$ are usually destroyed by the operation. 

Show how to support `UNION` in $O(1)$ time using a suitable list data structure.

## Implementation details
By using a linked list where each set maintains a pointer to both its `head` and its `tail`, the `UNION` operation can simply point the `tail` of $S_1$ to the `head` of $S_2$. This achieves the required $O(1)$ time complexity without traversing the sets.
