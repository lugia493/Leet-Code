'''
Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L). 
You might need to change the root of the tree, so the result should
return the new root of the trimmed binary search tree.

Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
'''


class Node:
    def __init__ (self, val):
        self.val = val
        self.right = None
        self.left = None

root = Node(3)
root.left = Node(0)
root.right = Node(4)
root.left.right = Node(2)
root.left.right.left = Node(1)

L = 1
R = 3

def trim(root, L, R):
    if root is None:
        return None
    # if the node value is less than L, then we only worry about the right subtree
    # to be trimed so return it
    elif root.val < L:
        return trim(root.right)
    # if the node value is greater than R, then we only worry about the left subtree
    # to be trimed, so return it 
    elif root.val > R:
        return trim(root.left)
    # if the node falls inbetween the two limits, we can assign its left and right
    # counterparts and trim both side
    else:
        root.left = trim(root.left)
        root.right = trim(root.right)
        return root







