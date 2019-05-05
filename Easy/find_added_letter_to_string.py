'''
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''

def sol1(t,s):

    letter_added = 0
    for char in s:
        letter_added ^= ord(char)
    for char in t:
        letter_added ^= ord(char)
    return chr(letter_added)

def sol2(t,s):

    for char in t:
        s = s.replace(char, "", 1)
    return s

def sol3(t, s):
    diff1 = diff2 = 0
    for char in t:
        diff1 += ord(char)
    for char in s:
        diff2 += ord(char)
    return chr(diff2 - diff1)

t = 'abcd'
s = 'abcde'
print(sol1(t,s))
print(sol2(t,s))
print(sol3(t,s))