'''
Find 3 numbers in arr that add up to 0

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

# 0(N^2)

def solution(arr):
    arr.sort()
    res = []
    for i in range(0, len(arr)-2):
        # The check below makes sure we dont process duplicated elements
        # If we process arr[i] and arr[i+1] == arr[i+1], no need to reprocess
        # the same element
        if i == 0 or i > 0 and arr[i] != arr[i-1]:
            lo, hi, sum = i+1, len(arr) - 1, 0 - arr[i]
            while lo < hi:
                if arr[lo] + arr[hi] == sum:
                    res.append([arr[lo], arr[hi], arr[i]])
                    # If there are duplicate elements in arr, 
                    # then we iterate through those elemenets to
                    # find the unique element. 
                    while lo < hi and arr[lo] == arr[lo+1]:
                        lo += 1
                    while lo < hi and arr[hi] == arr[hi-1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif arr[lo] + arr[hi] < sum:
                    lo += 1
                else:
                    hi -= 1
    return res

arr = [-1, 0, 1, 2, -1, -4]
print(solution(arr))


def helper(arr):
    arr.sort()
    res = []
    for i in range(0, len(arr)-2):
        if i == 0 or i > 0 and arr[i] != arr[i-1]:
            lo, hi, sum = i+1, len(arr) - 1, 0 - arr[i]
            while lo < hi:
                if arr[lo] + arr[hi] == sum:
                    res.append([arr[lo], arr[hi], arr[i]])
                    while arr[lo] == arr[lo+1]:
                        lo += 1
                    while arr[hi] == arr[hi-1]:
                        hi -= 1
                    hi -= 1
                    lo += 1
                elif arr[lo] + arr[hi] < sum:
                    lo += 1
                else:
                    hi -= 1
    return res
arr = [-1, 0, 1, 2, -1, -4]
print(helper(arr))