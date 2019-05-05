# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:56:51 2019

@author: Daniel
"""
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
def levelorder(root):
    if not root:
        return
    q = deque()
    q.append(root)
    while q:
        count = len(q)
        while count > 0:
            tNode = q.popleft()
            print(tNode.val)
            if tNode.left:
                q.append(tNode.left)
            if tNode.right:
                q.append(tNode.right)
            count -= 1
        print()
        

'''
1. Need a recursive function that has right and left nodes and check if head is None
2. Consider two cases: 1 where node is leaf and not a leaf
3. If node is a leaf, then we could return True once we get to this point, 
    because we will check for a false condition on the way
4. if node is not a leaf, we must check if left == right and check the children too
    if all of this is true, return true, else return false
'''        
def isSymmetric(head):
    return not head or check(head.left, head.right)

def check(leftNode, rightNode):
    if leftNode is None and rightNode is None:
        return True
    elif leftNode is not None and rightNode is not None:
        if leftNode.val == rightNode.val and check(leftNode.right, rightNode.left) and check(rightNode.right, leftNode.left):
            return True
    return False

head = Node(1)
head.right = Node(2)
head.left = Node(2)
head.right.right = Node(3)
head.right.left = Node(4)
head.left.left = Node(3)
head.left.right = Node(4)
levelorder(head)

print(isSymmetric(head))