'''
There are 2N people a company is planning to interview. 

The cost of flying the i-th person to city A is costs[i][0], 
and the cost of flying the i-th person to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
'''

'''
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110

Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
'''

# 0(n2) sorting solution
def solution1(arr):

    for i in range(0, len(arr)):
        j = i + 1
        while j < len(arr):
            diff1 = arr[i][0] - arr[i][1]
            diff2 = arr[j][0] - arr[j][1]
            if diff1 > diff2:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1

    print(arr)
    
    res = 0
    for i in range(0, len(arr)):
        if i < len(arr) / 2:
            res += arr[i][0]
        else:
            res += arr[i][1]
    return res

arr = [[10,20],[30,200],[400,50],[30,20]]
print(solution1(arr))


# Faster, 0(nlogn)
def solution2(arr):

    def function(arr):
        return arr[0] - arr[1]

    # Either or works
    #arr = sorted(arr, key=function)
    arr.sort(key = function)
    
    res = 0
    for i in range(0, len(arr)):
        if i < len(arr) / 2:
            res += arr[i][0]
        else:
            res += arr[i][1]
    return res
            
print(solution2(arr))


def solution3(arr):
    arr.sort(key = lambda x : x[0] - x[1])
    res = 0
    for i in range(0, len(arr)):
        if i < len(arr) / 2:
            res += arr[i][0]
        else:
            res += arr[i][1]
    return res

print(solution3(arr))