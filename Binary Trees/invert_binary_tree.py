'''
Invert a binary tree
'''


# BFS solution

def invertTree(root):
        
        if root is None:
            return None
                
        q = collections.deque()
        q.append(root)
        while q:
            count = len(q)
            while count > 0:
                node = q.popleft()
                if node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
                    node.left, node.right = node.right, node.left
                elif node.right and node.left is None:
                    q.append(node.right)
                    node.left = node.right
                    node.right = None
                elif node.left and node.right is None:
                    q.append(node.left)
                    node.right = node.left
                    node.left = None
                count -= 1
        return root

# Recursive Solutions

def solution(root):
    if root is None:
        return None
    right = solution(root.left)
    left = solution(root.right)
    root.left = right
    root.right = left
    return root
