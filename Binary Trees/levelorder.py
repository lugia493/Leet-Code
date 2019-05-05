# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:58:48 2019

@author: Daniel
"""
from collections import deque
import numpy as np

class Node: 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        
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
    
def main():
    root = Node(10) 
    root.left = Node(8) 
    root.right = Node(2) 
    root.left.left = Node(3) 
    root.left.right = Node(5) 
    root.right.left = Node(2) 
    levelorder(root)
main()