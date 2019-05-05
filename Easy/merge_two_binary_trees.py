
from collections import deque
import numpy as np
# Make a new tree out of two trees with the node being the
# addition of the two nodes from the two trees.

class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def levelorder(root):
    if not root:
        return 
    q = deque()
    q.append(root)
    final = []
    while q:
        count = len(q)
        temp_l = []
        while count > 0:
            temp = q.popleft()
            temp_l.append(temp.val)
            if temp.right:
                q.append(temp.right)
            if temp.left:
                q.append(temp.left)
            count -= 1
        final.append(temp_l)
    
    print(np.matrix(final))

def mergeTrees(t1,t2):
    '''
    So we will be traversing each node in each of trees. 
    We can do a prelevel traversal for this

    Rather than make a new tree, we could just modify one of the trees, 
    adding the other tree nodes values to it.

    Base Case:
    If a node on one tree is None, we could return the other tree's node

    Recursive:
    Pre level traversal, adding nodes values
    '''
    if t1 is None:
        return t2
    if t2 is None:
        return t1

    t1.val += t2.val
    t1.left = mergeTrees(t1.left,t2.left)
    t1.right = mergeTrees(t1.right,t2.right)

    return t1

t1 = Node(1)
t1.left = Node(2)
t1.right = Node(3)
t1.left.left = Node(4)
t1.left.right = Node(5)

t2 = Node(5)
t2.left = Node(3)
t2.left.left = Node(2)
t2.right = Node(6)
t2.right.right = Node(4)
t2.right.left = Node(1)

t3 = mergeTrees(t1,t2)
levelorder(t3)

