'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# Iterative solution (BFS)

def Iterative(root):
    q = collections.deque()
    q.append(root)
    res = []
    while q:
        count = len(q)
        div = float(count)
        avg = 0
        while count > 0:
            node = q.popleft()
            avg += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            count -= 1
        res.append(avg/div)
    return res

# Recursive solution(DFS)

def recursive(root):

    def helper(root,level):
        if root is None:
            return 
        d[level] += [root.val]
        helper(root.left, level+1)
        helper(root.right, level+1)

    if root is None:
        return None
    # key is the level and value is an array of node values for that level
    d = {}
    result = []
    helper(root, 1)
    for k,v in d.items():
        result.append(float(sum(value))/len(value))
    return result
