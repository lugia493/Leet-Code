class Node:
    def __init__ (self,val):
        self.val = val
        self.left = None
        self.right = None

def isUnivalue(root):
    if root is None:
        return True

    if root.right and root.val != root.right.val:
            return False
    
    if root.left and root.val != root.left.val:
            return False

    return isUnivalue(root.left) and isUnivalue(root.right)


root = Node(5) 
root.left = Node(5) 
root.right = Node(5) 
root.left.left = Node(5) 
root.left.right = Node(5) 
root.right.right = Node(5)
print(isUnivalue(root))
