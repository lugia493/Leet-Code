'''

Find the maximum contiguous subarray of a given array

'''

arr = [-2,1,-3,4,-1,2,1,-5,4]

def solution(arr):

    # max_so_far is the result of the solution
    max_so_far = arr[0]

    # max_sub_array is the value of the subarray
    # that we have chosen to be max. This is modified
    # throughout the dynamic program
    max_sub_array = arr[0]

    for i in range(1, len(arr)):
        # Decide two things: Continue the subarray or start
        # new subarray. We start a new max_sub_array at 
        # the current value in array if current value 
        # is bigger than current value + max_sub_array
        max_sub_array = max(arr[i], max_sub_array + arr[i])
        max_so_far = max(max_so_far, max_sub_array)
    return max_so_far
    

print(solution(arr))

def solution2(arr):
    max_sub_array = max_so_far = 0
    best_start = this_start = end = 0

    for i, x in enumerate(arr):
        # max_sub_array calculates the added values 
        # of any particular subarray in the array
        max_sub_array += x
        # max_so_far tracks when the we find the maximum
        # valued subarray
        max_so_far = max(max_so_far, max_sub_array)

        if max_sub_array <= 0:
            # If max_sub_array is negative, that means that
            # the subarray that we are essentially analysing 
            # is obviously not max. We wont to throw away this subarray
            # We do this by setting the max_sub_array = 0 and also 
            # setting this_start = i + 1, which is the beginning index
            # of the next subarray
            this_start = i + 1
            max_sub_array = 0
        elif max_sub_array == max_so_far:
            # If max_sub_array == max_so_far, then max_sub_array
            # is better/larger than max_so_far. This means that 
            # we can extend the this_start of max_so_far is best_start
            # and the end will be after the current value at index i
            best_start = this_start
            end = i + 1
    return max_so_far, best_start, end

print(solution2(arr))

def maxSubArray(nums):
    for i in range(1, len(nums)):
        # If the previous value, end of subarray is positive, 
        # then add current value to that
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
        # If the previous node is negative, then dont do anything
        # because adding current value to previous value will 
        # be less than that of current values only. Therefore leave
        # it alone
    return max(nums)

print(maxSubArray(arr))
