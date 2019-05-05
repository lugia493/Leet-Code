'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
'''


'''
Input: "00110011"
Output: 6

Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
'''

# 0(N) - 0(N)
def solution1(s):
    group = [1]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            group.append(1)
        else:
            group[-1] += 1
    res = 0
    for i in range(1, len(group)):
        res += min(group[i-1], group[i])
    return res

s = "001100110"
print(solution1(s))

# 0(N) - 0(1)
def solution2(s):
    curr = 1
    prev = 0
    res = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr += 1
        else:
            res += min(prev, curr)
            prev = curr
            curr = 1
    res += min(prev, curr)
    return res

print(solution2(s))
