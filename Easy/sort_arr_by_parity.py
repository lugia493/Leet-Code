
def brute_force(arr):
    '''
    0(N) time
    0(N) space
    '''
    if len(arr) == 0 or len(arr) == 1:
        return arr
    
    ans = []
    for val in arr:
        if val % 2 == 0:
            ans = [val] + ans
        else:
            ans += [val]
    print(ans)

# Modifies the array in-place but still 0(N)
# sorting is 0(NlogN)

def solution(arr):
    '''
    This is modified quick sort that passes through
    the array only once.
    0(N) time
    0(1) space
    '''
    i = -1 # i tracks the tail of the left subarr 
    for j in range(0, len(arr)):
        if arr[j] % 2 == 0: # if we found an even number, put that number in the left array
            i += 1;    
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    print(arr)

arr = [1,3,5,0,1]
brute_force(arr)
solution(arr)

