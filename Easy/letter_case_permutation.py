'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string. 
Return a list of all possible strings we could create.
'''

def solution(S):
    res = [S]
    for i, c in enumerate(S):
        if c.isalpha():
            res.extend([s[:i] + s[i].swapcase() + s[i+1:] for s in res])
    return res

S = "a1b2"
print(solution(S))