'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Example:
Input: [4,2,5,7]
Output: [4,5,2,7]
'''


def sort(A):
    '''
    Define the even and off pointers. These pointers will find where there are
    elements in the wrong place. For each pair, we swap the elements.
    '''
    i = 0
    j = 1

    while i < len(A) and j < len(A):
        '''
        Iterate the i pointer if element is in the right place and 
        Iterate the j pointer if element is in the right place.

        If we get to the else condition, then we found a pair of elements 
        that need to be switched. 
        '''
        if A[i] % 2 == 0:
            i += 2
        
        elif A[j] % 2 == 1:
            j += 2
        else:
            A[i], A[j] = A[j], A[i]
    return A

A = [4,2,5,7]
sort(A)
print(A)