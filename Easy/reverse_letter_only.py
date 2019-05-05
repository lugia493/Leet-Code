'''
Given a string S, return the "reversed" string where 
all characters that are not a letter stay in the same place, 
and all letters reverse their positions.
'''


def solution(s):
    letters = [c for c in s if c.isalpha()]
    ans = []
    for c in s:
        if c.isalpha():
            ans.append(letters.pop())
        else:
            ans.append(c)
    return ''.join(ans)

s = "Test1ng-Leet=code-Q!"
print(solution(s))