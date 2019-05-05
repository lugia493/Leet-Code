
'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

'''

def solution(str1, str2):
    while str1 != "" and str2 != "":
        # If the strings are of equal length,
        # Then they are the same or not the same. 
        # If they are the same, return one or the
        # other sense it is the biggest, if not, 
        # return nothing because they dont divide
        if len(str1) == len(str2):
            return str1 if str1 == str2 else ""
        # if str1 length is less than str2,
        # switch them
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        # if str2 is in str1, remove str2 from 
        # str1
        if str2 in str1:
            str1 = str1.replace(str2, "")
        # If str2 is not in str1, that means we cant divide it
        # so we return 
        else:
            return ""
    # If str1 or str2 is "", then we found the 
    # non empty str to be the answer
    return str2 if str1 == "" else str1
    
str1 = "ABCABC"
str2 = "ABC"
print(solution(str1, str2))

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
print(solution(str1, str2))