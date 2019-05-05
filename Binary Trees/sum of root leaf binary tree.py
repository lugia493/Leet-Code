'''
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def helper(root, val):
    if root is None:
        return 0
    val = 2*val + root.val
    if root.left == root.right:
        return val
    return helper(root.left, val) + helper(root.right,val)

root = Node(1)
root.left = Node(0)
root.right = Node(1)
root.left.left = Node(0)
root.left.right = Node(1)
root.right.right = Node(1)
root.right.left = Node(0)

print(helper(root,0))