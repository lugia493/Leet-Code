'''
Given a BST, sum all of the node values as long as
the node values are greater than or equal L and 
less than or equal to R given.
'''

'''
ex. 
         10 
       /    \
      5     15
     / \    / \
    3   7 null 18

    L = 7, R = 15

ans. 32

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def rangeSum1(root,L,R):
    '''
    We need to access each node and figure out if the 
    node.val lays inbetween L and R, inclusive. 
    We could simply use inorder traversal and compare
    the node.val we get, and add it to our global variable
    '''
    if root:
        rangeSum1(root.left,L,R)
        if root.val <= R and root.val >= L:
            rangeSum1.ans += root.val
        rangeSum1(root.right,L,R)

# without a global variable, you can do this
def rangeSum2(root,ans,L,R):
    if root:
        ans = rangeSum2(root.left,ans,L,R)
        if root.val <= R and root.val >= L:
            ans += root.val
        ans = rangeSum2(root.right,ans,L,R)
    return ans

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(18)

L, R = 7, 15

rangeSum1.ans = 0
rangeSum1(root,L,R)
print(rangeSum1.ans)

print(rangeSum2(root,0,L,R))

print(ord('a') - 97)
print(ord('z') - 97)

