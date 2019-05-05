'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''

'''
My 0(n) 0(n) solution
'''

def sol1(nums):
    d = {}
    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1
    for k,v in d.items():
        if v == 1:
            return k
    return None


'''
0(N) time 0(1) solution

basically we can XOR all of the numbers together to find the single number
Note: 
a ^ 0 = a
a ^ a = 0
a ^ b ^ a = (a ^ a) ^ b = b

'''

def solution(arr):
    a = 0
    for num in arr:
        a ^= num
    return a


arr = [1,2,1,2,3,4,5,4,5]
print(solution(arr))


