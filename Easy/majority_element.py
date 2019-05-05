'''
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

# 0 (nlogn) 0(1)
def sol1(arr):
    arr.sort()
    return arr[len(arr)/2]

# 0(n) 0(1)
def sol2(arr):
    count = 0
    for val in arr:
        if count == 0:
            candidate = val
        count += (1 if val == candidate else -1)
    return candidate

arr = [2,2,1,1,1,2,2]
print(sol1(arr))
print(sol2(arr))