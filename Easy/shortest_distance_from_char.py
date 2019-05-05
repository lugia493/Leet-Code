def solution(S,char):

    '''
    First, we pass through the array. we are populating the elements to the left 
    of the desired char. We will use the indices to calculate the distance from 
    the char, and from the left char that is in interest.

    So we need to keep track of the last index where we see an e.
    '''

    # this parameter is necessary because if we dont see our char yet, 
    # we populate the array with a inf number.
    # This value must be negative, because (prev - i) will populate the
    # box with a possible Inf number. We are fining the minimum distance from 
    # char, so when we do the pass from the right and compare, the element 
    # we get from that pass will always be less than inf, so we use that number
    prev = float('-inf')

    res = []

    for i in range(0,len(S)):
        if S[i] == char:
            prev = i
        # i - prev will give us the distance. 
        # ex. if e == 5 and t == 6, then t will be labeled as 1
        res.append(i - prev)
    
    print "Left pass:", res
    '''
    Now we take a pass from the right, and comparing the
    number we get to the number in our result array. We 
    populate the res array with the lesser number.

    We keep track of a prev just as before
    '''

    # So we will be doing prev - i this time bcs we are coming
    # from the right. prev will be Inf for reasons already discussed
    prev = float("inf")
    for i in range(len(S) - 1, -1, -1):
        if S[i] == char:
            prev = i
        res[i] = min(res[i], prev - i)

    return res

S = "lovetoleetcode"
char = "e"
print(solution(S,char))