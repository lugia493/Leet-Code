
def binarySearch(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low - int((high-low)/2)
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def nextClosest(input):

    # Split hour and minute. Note that hour and minute are strings
    hour, minute = input.split(":")

    # Get the numbers. set(minute+hour) gets rid of duplicates
    # and sorted creates the array of nums
    nums = sorted(set(minute + hour))

    # Get all two digit values (at most 16 values). Note that they are sorted.
    twoDigitValues = [a+b for a in nums for b in nums]

    # Get the index at the given minute, and check if next minute in twoDigitValues is within an hour (i.e. not over 59)
    # we also must check if i + 1 is within range, as always we should.
    # If we find a twoDigitValues that satisfies the above conditions, we can return 
    i = twoDigitValues.index(minute)
    '''
    Optimize the above code using binary search. However, we only have at most 16 elements, so
    using binary search wont drastically help. Still good to know both methods though.
    i = binarySearch(twoDigitValues, minute)
    '''

    if i + 1 < len(twoDigitValues) and twoDigitValues[i+1] < "60":
        return hour + ":" + twoDigitValues[i + 1]

    # So if we couldnt find a minute that satisfies either of the conditions then we check if 
    # we can find the closest hour within a day
    # If we satisfy the above conditions, return the hour found and the smallest minute in the
    # twoDigitsValue array, which happens to be the first element
    i = twoDigitValues.index(hour)
    '''
    Optimize the above code using binary search. However, we only have at most 16 elements, so
    using binary search wont drastically help. Still good to know both methods though.
    i = binarySearch(twoDigitValues, hour)
    '''
    
    if i + 1 < len(twoDigitValues) and twoDigitValues[i+1] < "25":
        return twoDigitValues[i+ 1] + ":" + twoDigitValues[0]

    # If the above 2 conditions are not met, that means we roll over to another day
    # in this case, we can just return the earliest day and minutes of that day
    return twoDigitValues[0] + ":" + twoDigitValues[0]

def main():
    input = "23:59"
    print(nextClosest(input))
main()
