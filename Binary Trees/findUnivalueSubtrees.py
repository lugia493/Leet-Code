# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:18:31 2019

@author: Daniel
"""
class Node: 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        
def countUnivalueSubtrees(root):    
    if root is None:
        return True
    r = countUnivalueSubtrees(root.right)
    l = countUnivalueSubtrees(root.left)
    if l and r:
        if (root.left is not None and root.left.val != root.val) or (root.right is not None and root.right.val != root.val):
            return False
        else:
            countUnivalueSubtrees.count += 1
            return True
    return False

def main():
    root = Node(5) 
    root.left = Node(1) 
    root.right = Node(5) 
    root.left.left = Node(5) 
    root.left.right = Node(5) 
    root.right.right = Node(5)
    
    countUnivalueSubtrees.count = 0
    countUnivalueSubtrees(root)
    print(countUnivalueSubtrees.count)
main()