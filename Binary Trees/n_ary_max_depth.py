
def max_depth(root):

    # If we have a None root, return 0
    if not root:
        return 0
    # if the children of a root is None, return 1 for that rot
    if not root.childen:
        return 1

    # We need the two condtions if we run into a tree that has some 
    # valid nodes and some None nodes.
    # i.e.  5 (3 children) -> 1,2,None
    return max(max_depth(child) for child in root.children) + 1


# Iterative solution 
def dfs(self, d, node):
    if len(node.children) == 0:
        if d > maxDepth.mDepth:
            maxDepth.mDepth = d
        return
    
    for child in node.children:
        self.dfs(d+1, child)

def maxDepth(self, root):
    if root == None:
        return 0
    dfs(1, root)
    return maxDepth.mDepth

maxDepth.mDepth = 0
