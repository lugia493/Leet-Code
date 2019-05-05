from collections import deque 

# TreeNode is a class definition for a node in a tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def longestUnivalePath(root):

    # If the root node is None, we can simply return 
    if root is None: 
        return 0

    # Define global variable to keep track of the maximum length
    longestUnivalePath.maxLength = 0

    # In order to find the maxiumum path, we need to compare the current node val and
    # the previous node value. Thus, we need a helper function.
    def helper(node, nodePrevVal):

        # If we get to a leaf node, return 0. 
        if node is None:
            return 0
        
        # When a problem asks for finding the any sort of path, we use a depth
        # first search approach. Thus, we recurse down the left and right
        # branches of the tree immediatly after checking if node is None.
        left = helper(node.left, node.val)
        right = helper(node.right, node.val)

        # Next, we need to calculate the maxLength. So the reason why we finding
        # max between maxLength and left + right is because left and right can make up
        # the longest path. For instance, left could be 1 and right could be 2. This looks like
        #     1
        #    /
        #   5
        #  / \
        # 5   5
        #    /
        #   5
        # Left or right could also be zero, which simply means that the somewhere in our recusion,
        # node.val != nodePrevVal, which is what we need to figure out next ...
        longestUnivalePath.maxLength = max(longestUnivalePath.maxLength, left + right)

        # We have found a path according to problem where node.val == nodePrevVal. 
        # So consider the example
        #     1
        #    /
        #   5
        #  / \
        # 5   5
        #    /
        #   5
        # if node.val = 5 and nodePrevVal is 5 we notice that left is 1 and right is 2. Well sense we are trying to find
        # the longest path, obviously we chose right. Therefore we chose right, add 1, and return the value
        if node.val == nodePrevVal:
            return max(left, right) + 1
        
        # Otherwise, if node.val != nodePrevVal, then the path is set to 0
        return 0

    # Call the helper function
    helper(root, root.val)

    # Return the maxLength global variable
    return longestUnivalePath.maxLength

def main():
    # Create the tree
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(5)

    # Print the answer
    print(longestUnivalePath(root))
main()