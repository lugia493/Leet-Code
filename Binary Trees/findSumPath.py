# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 21:36:14 2019

@author: Daniel
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
'''
1. Do we find a path or not? Boolean function returns
2. Edge case, if node is null. If we get to this point
   we probably dont have a path based on our algorithm
3. Need to check if last node value is equal to final sum if node is 
   leaf
4. final sum needs the be recalulated with each call
5. Return true if a path is found

'''
def findSumPath(root, s):
    if root is None:
        return False
    
    if root.left is None and root.right is None:
        if root.val == s:
            findSumPath.list.append(root.val)
            return True
        else:
            return False
    
    if findSumPath(root.left, s - root.val) or findSumPath(root.right, s - root.val):
        findSumPath.list.append(root.val)
        return True
    return False
    

root = Node(7)
root.right = Node(2)
root.left = Node(6)
root.right.right = Node(3)
root.right.left = Node(4)
root.left.left = Node(-2)
root.left.right = Node(10)

findSumPath.list = []
print(findSumPath(root, 12))
print(findSumPath.list)