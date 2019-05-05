'''
Given a complete binary tree, count the number of nodes.

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# 0(n) solution
def sol1(root):
    if root:
        sol1.count += 1
        sol1(root.left)
        sol1(root.right)
sol1.count = 0
sol1(root)
print(sol1.count)

# 0(log 2 n) Divide and conquer technique

import math 

def sol2(root):
    if not root:
        return 0
    
    leftDepth = getDepth(root.left)
    rightDepth = getDepth(root.right)

    if leftDepth == rightDepth:
        # left tree is a perfect binart tree. Add up all nodes including root
        # right tree is a complete binary tree. Traverse the tree and count its nodes
        return math.pow(2,leftDepth) + sol2(root.right)
    # This case only occurs when leftDepth > rightDepth (due to complete binary tree properties)
    # left binary tree is a complete binary tree. Tranverse the tree and count its nodes
    # right binary tree is perfect binary tree. Add up all nodes including root
    return math.pow(2, rightDepth) + sol2(root.left)

def getDepth(subRoot):
    if not subRoot:
        return 0
    # Only traverse the left side of the subRoot. We only 
    # care about this because this helps us figure out
    # if a tree is complete or perfect based on comparing the
    # right subtree and left subtree
    return 1 + getDepth(subRoot.left)

print(sol2(root))

