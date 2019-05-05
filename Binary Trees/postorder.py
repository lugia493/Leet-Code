# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:48:02 2019

@author: Daniel
"""

#Good for finding tree depth

class Node: 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        
def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

def iterativePostorder(root):
    
    if not root:
        return 
    
    stack = []
    while True:
        while root:
            if root.right:
                    stack.append(root.right)
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.right and root.right == peek(stack):
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            print(root.val)
            root = None
        if len(stack) <= 0:
            break
        
def recursivePostorder(root):
    if root:
        recursivePostorder(root.left)
        recursivePostorder(root.right)
        print(root.val)


def main():
    root = Node(10) 
    root.left = Node(8) 
    root.right = Node(2) 
    root.left.left = Node(3) 
    root.left.right = Node(5) 
    root.right.left = Node(2) 
    iterativePostorder(root) 
    print()
    recursivePostorder(root)
main()