'''
Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings within the list (including duplicates). 
For example, if a character occurs 3 times in all strings but not 4 times, 
you need to include that character three times in the final answer.

You may return the answer in any order.

Input: ["bella","label","roller"]
Output: ["e","l","l"]

'''


def most_common(A):
    # Result array
    result = []

    # iterator for the first word
    i = 0

    # Not sure how many times we will loop, so use a while. We only need to loop over the 
    # first word, looping over all words are unnecessary
    
    while i < len(A[0]):

        # Returns true if [True, True, ... , True], basically if the char A[0][i] exists 
        # in all of the words. all is a built in python function. Creates a 0(N) Space bool
        # array in worst case and runtime would be 0(N * num of chars)
        if all(A[0][i] in word for word in A):
            # Append to the result arr
            result.append(A[0][i])
            # Now we must delete this char from all words in A or else
            # we may get incorrect answers (i.e. the case when first char
            # has 2 'i's and all other words have 1 'i')
            # replace create a new string copy when called
            A = [word.replace(A[0][i], "", 1) for word in A]

            # A is now one char less (i.e. "string" -> "sring")
            # basically, if we dont adjust pointer i, after removing 't', we could 
            # iterate at 'i' and skip 'r'. Therefore we need to push i back by 1
            i -= 1
        i += 1
    return result

A = ["bella","label","roller"]
ans = most_common(A)
print(ans)