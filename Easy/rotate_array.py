'''
Given and array and k, find the rotation
ex. input = 1,2,3,4,5,6,7], k = 3
ans. [5,6,7,1,2,3,4]
'''
def brute_force(arr,k):
    '''
    Time 0(N * K) - exceeds runtime for very large input
    Space 0(N)
    '''
    k %= len(arr)
    # This process is 0(K) time
    for i in range(0,k):
        # I think this process is 0(N) time
        tailVal = arr.pop(len(arr) - 1)
        # new allocation of arr is 0(N) space
        arr[:] = [tailVal] + arr[:len(arr)]
    print(arr)

def solution(arr,k):
    '''
    Optimal Solution
    Time 0(N)
    Space 0(1)

    Step 1: Reverse arr
    Step 2: Reverse the first k elements
    Step 3: Reverse the last elements, starting at k - 1

    Ex. [1,2,3,4,5,6,7]

    Step 1: [7,6,5,4,3,2,1]
    Step 2: [5,6,7,4,3,2,1]
    Step 3: [5,6,7,1,2,3,4]
    '''
    def reverse(arr,start,end):
        '''
        0(N) time
        0(1) space
        '''
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1

    # 0(N) time
    reverse(arr,0,len(arr)-1)
    # 0(k)
    reverse(arr,0,k-1)
    # 0(N-k)
    reverse(arr,k,len(arr)-1)
    # 0(N) + 0(k) + 0(N-k) = 0(2N) = 0(N)
    print(arr)

arr = [1,2,3,4,5,6,7]
k = 3
brute_force(arr, k)

arr = [1,2,3,4,5,6,7]
solution(arr,k)   