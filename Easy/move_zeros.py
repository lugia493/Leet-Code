'''
Given an array nums, write a function to move all 0's to 
the end of it while maintaining the relative order of the non-zero elements.


Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

'''


def solution(arr):
    lastZeroFound = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[i], arr[lastZeroFound] = arr[lastZeroFound], arr[i]
            lastZeroFound += 1
    return arr

arr = [0,1,0,3,12]
print(solution(arr))