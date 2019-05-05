'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
'''

# My solution
def isMonotonic(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    if len(A) <= 2:
        return True
    elif A[0] < A[len(A)-1]:
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                return False
    else:
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                return False
            
    return True

# 2 more solutions
def isMonotonic2(A):
    return all(A[i] <= A[i+1] for i in range(len(A)-1)) or all(A[i] >= A[i+1] for i in range(len(A)-1))

def isMonotonic3(A):
    increasing = decreasing = True
    for i in range(len(A) - 1):
        if A[i] < A[i+1]:
            decreasing = False
        if A[i] > A[i+1]:
            increasing = False
    return increasing or decreasing

print(isMonotonic([1,2,2,3]))
print(isMonotonic2([6,5,4,4]))
print(isMonotonic3([1,3,2]))

A = [10,9,8,7,6]
print(A[2:4])