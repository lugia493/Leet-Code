'''
Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
'''

def solution(words):

    '''
    Optimization would be making this array into a map
    '''
    map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    # For getting rid of duplicates
    s = set()
    for word in words:
        # creates a new string temp and temp equals the morse code
        # representation of the word
        temp = "".join([map[ord(char)-97] for char in word])
        # add the temp string to set
        s.add(temp)
    # return the number of unique morse code strings
    return len(s)