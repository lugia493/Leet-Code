# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:57:52 2019

@author: Daniel
"""
class Node: 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None

def iterativePreorder(root):
    
    if not root:
        return
    
    l, stack = [],[]
    stack.append(root)
    
    while len(stack) > 0:
        node = stack.pop()
        l.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    print(l)
    
def recursivePreordereHelper(root, res):
    if root:
        res.append(root.val)
        recursivePreordereHelper(root.left, res)
        recursivePreordereHelper(root.right, res)
    return res

def recursivePreorder(root):
    res = []
    res = recursivePreordereHelper(root, res)
    print(res)
    
def main():
    root = Node(10) 
    root.left = Node(8) 
    root.right = Node(2) 
    root.left.left = Node(3) 
    root.left.right = Node(5) 
    root.right.left = Node(2) 
    iterativePreorder(root) 
    recursivePreorder(root)
main()