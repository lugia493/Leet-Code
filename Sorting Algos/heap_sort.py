# Runtime: 0(nlogn)
# Space: 0(1) in-place

# Two main parts: building a max-heap and then sorting it
# remove root from max-heap, insert elem into arr and
# then heapify the max-heap

# Applications: Sorting a nearly sorted array

import heapq

def sort(arr):
    return heapq.nsmallest(len(arr), arr)

def main():
    arr = [243,5,527,72,3,4,632,1]
    print(sort(arr))
main()
