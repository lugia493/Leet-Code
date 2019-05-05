'''
We are givin array A that needs to be sorted
We are givin arry B which contains the correct
indices for array A. Sort array A in 0(n)
'''

def sort(A,B):
    i = 0 
    # Iterate through array B
    while i < len(B):
        # get the value at B[i]
        pos = B[i] - 1

        # If B is not at the correct index
        # we swap B[pos] with B[i] and
        # the same goes for A[pos] and A[i]
        if pos != i:
            B[i], B[pos] = B[pos], B[i]
            A[i], A[pos] = A[pos], A[i]
        # If the element is in the right
        # position, then we can move on
        else:
            i +=1
        # If we dont enter the else
        # condition, that means that 
        # whatever was placed at B[i] 
        # now needs to be checked if it
        # is in the right position
    
    # Return the answer after one pass
    return A, B

A = [24,56,74,-23,87,91]
B = [2,3,4,1,5,6]

print(sort(A,B))