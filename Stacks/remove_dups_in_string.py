'''
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and 
equal letters, and removing them.We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Input: "abbaca"
Output: "ca"

'''

def solution(S):
    res = []
    for char in S:
        if res and res[-1] == char:
            res.pop()
        else:
            res.append(char)
    return ''.join(res)

print(solution("abbaca"))