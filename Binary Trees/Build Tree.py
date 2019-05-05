# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:00:14 2019

@author: Daniel
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(arr, start, end, val):
    for i in range(start, end + 1):
        if arr[i] == val:
            return i
        
def buildTree(inorder, preorder, start, end):
    if start > end:
        return None
    
    tNode = Node(preorder[buildTree.preIndex])
    buildTree.preIndex += 1
    
    if start == end:
        return tNode
    
    inorderIdx = search(inorder, start, end, tNode.val)
    
    tNode.left = buildTree(inorder, preorder, start, inorderIdx - 1)
    tNode.right = buildTree(inorder, preorder, inorderIdx + 1, end)
    
    return tNode

def makeTree(inOrder, postOrder, inStart, inEnd):
    if inStart > inEnd:
        return None
    
    tNode = Node(postOrder[makeTree.postIdx])
    makeTree.postIdx -= 1
    
    if inStart == inEnd:
        return tNode
    
    inIdx = search(inOrder, inStart, inEnd, tNode.val)

    tNode.right = makeTree(inOrder, postOrder, inIdx + 1, inEnd)
    tNode.left = makeTree(inOrder, postOrder, inStart, inIdx - 1)
    
    return tNode
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        inorder(root.left)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

'''
# Driver program to test above function 
inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preOrder = ['A', 'B', 'D', 'E', 'C', 'F'] 
# Static variable preIndex 
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1) 
  
inorder(root)
print()
preorder(root)
'''
inOrder = [9,3,15,20,7]
postOrder = [9,15,7,20,3]
makeTree.postIdx = len(postOrder) - 1
root2 = makeTree(inOrder, postOrder, 0, len(inOrder) - 1)

inorder(root2)
print()
postorder(root2)
  