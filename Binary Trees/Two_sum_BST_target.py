'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def dfs(root, target):
    s = set()
    return helper(root, target, s)

def helper(root, target, s):
    if root is None:
        return False
    if target - root.val in s:
        return True
    s.add(root.val)
    return helper(root.left, target, s) or helper(root.right, target, s)

def bfs(root, target):
    q = []
    s = set()
    q.append(root)           
    while q:
        count = len(q)
        while count > 0:
            node = q.pop(0)
            if target - node.val in s:
                return True
            s.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            count -= 1
    return False

def sol3(root, target):
    vals = []
    def dfs(root, vals):
        if root:
            dfs(root.left, vals)
            vals.append(root.val)
            dfs(root.right, vals)
    dfs(root, vals)
    
    l, r = 0, len(vals) - 1
    while l < r:
        if vals[l] + vals[r] == target:
            return True
        elif vals[l] + vals[r] < target:
            l += 1
        else:
            r -= 1
    return False

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.right.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
target = 9

print(dfs(root, target))
print(bfs(root, target))
print(sol3(root, target))