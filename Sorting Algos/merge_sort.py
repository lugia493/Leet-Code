# Comparison-based sorting algo
# Divide and Conquer
# 0(nlogn) time
# 0(n) space
# best when data is huge and stored in external storage
# Allocating and de-allocating the extra space used for merge sort increases the running time of the algorithm
def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    p = arr[0]
    left = []
    right = []
    for val in arr:
        if val < p:
            left.append(val)
        elif val > p:
            right.append(val)
    return merge_sort(left) + [p] + merge_sort(right)
def main():
    arr = [5,1,7,3,6,34,8]
    print(merge_sort(arr))
main()