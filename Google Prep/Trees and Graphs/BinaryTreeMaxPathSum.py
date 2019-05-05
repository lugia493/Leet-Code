'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of 
nodes from some starting node to any node in the tree along 
the parent-child connections. The path must contain at least
one node and does not need to go through the root.

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


root = Node(-10)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

'''
We need to find the maximum path from left children
and maximum path from right children and add those paths 
to the root. We do this recursively


'''
def solution(root):
    helper.ans = -float('Inf')
    helper(root)
    return helper.ans

def helper(root):
    # If we reach None, return 0
    if root is None:
        return 0
    # When calculating the max root path, we dont care about the negative
    # values. We filter out the negative node values using the code below
    # Think of it like, if all node on the left is -, then none of those
    # nodes will be apart of the answer, so we set the left to 0
    l = max(0, helper(root.left))
    r = max(0, helper(root.right))

    # Now ans will be the max between the old ans, and 
    # l + r + node.val
    helper.ans = max(helper.ans, l+r+root.val)
    
    # After that, we need to return the max of the left or right 
    # which is then added to the root.val. This returns the max 
    # value to l or r which is in the call stack
    return max(l,r) + root.val

print(solution(root))