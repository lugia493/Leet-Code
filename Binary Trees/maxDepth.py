# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:10:52 2019

@author: Daniel
"""

# Bottom-Up approach

class Node: 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None

def maxDepth(root):
    if not root:
        return 0
    lDepth = maxDepth(root.left)
    rDepth = maxDepth(root.right)
    return max(lDepth, rDepth) + 1
    
def main():
    root = Node(10) 
    root.left = Node(8) 
    root.right = Node(2) 
    root.left.left = Node(3) 
    root.left.right = Node(5) 
    root.right.left = Node(2) 
    print(maxDepth(root))
main()