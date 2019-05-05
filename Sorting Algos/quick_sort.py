
# divide and conquer, like merge sort, Counting sort
# in-place algo, we have to store recursive calls but not for manipulating input 

# 0(nlogn) time but 0(n2) if the pivot doesnt chop the array efficiently
# 0(1) storage 
# Prefered over merge sort bcs of storage needed in arrays
def sort(arr):
    quick_sort(arr,0,len(arr)- 1)

def quick_sort(arr, l, r):
    if l < r:
        # Returns the index of the element that is sandwiched
        # between the elements less and greater than that element
        p = partition(arr,l,r)
        # sort the left side
        quick_sort(arr,l, p - 1)
        # sort the right side
        quick_sort(arr, p+1, r)

def partition(arr,l,r):
    # i tracks the tail end of elements less than that of pivot
    # At the end of partition, pivot will swap with the element
    # at (i+1), setting the pivot in the proper place in arr
    # i must begin at l - 1 because if all elements are greater than
    # pivot, place pivot at the first elem.
    i = l - 1

    # p can be set to any value. Right now, it is set to the last 
    # element in arr
    p = arr[r]

    # j will be looking through the whole arr except for the last
    # element, where we have chosen our pivot
    for j in range(l, r):
        # We check if the elem at index j is less than p
        # if that is the case, increment i, than we swap the elements at
        # indices i and j
        if arr[j] <= p:
            # We than increment i 
            i += 1
            # Than we swap
            arr[i], arr[j] = arr[j], arr[i]
    # At the end of the for loop, i will be set in a manner where
    # i is the tail of a subarray where all elements in that subarr are
    # less than our chosen pivot. We therfore found the correct location for 
    # p and we swap the elements at i + 1 with the pivot
    arr[i+1], arr[r] = arr[r], arr[i+1]

    # return the location of the pivot, or middle elem of less and greater subarr within arr
    return i + 1

def main():
    arr = [5,2,64,32,45,1,23,5,65,3,1,23,56,6,5]
    sort(arr)
    print(arr)
main()