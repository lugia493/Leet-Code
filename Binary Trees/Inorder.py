# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:03:49 2019

@author: Daniel
"""

# When deleting nodes in a tree, we use a post-order process to do so
class Node: 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None

def iterativeInorder(root):
    stack = []
    curr = root
    while len(stack) > 0 or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right
        
def recursiveInorder(root):
    if root:
        recursiveInorder(root.left)
        print(root.val)
        recursiveInorder(root.right)
    

def main():
    root = Node(10) 
    root.left = Node(8) 
    root.right = Node(2) 
    root.left.left = Node(3) 
    root.left.right = Node(5) 
    root.right.left = Node(2) 
    iterativeInorder(root) 
    print()
    recursiveInorder(root)
main()