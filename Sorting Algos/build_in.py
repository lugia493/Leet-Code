
def main():

    # 0(nlogn)
    arr = [4,2,54,243,1,4,6]

    # Sorted() creates a new list
    # Sorted(arr, reverse=True) puts elements in descending order
    # able to manipulate strings too
    b = sorted(arr)
    print(b)
    
    arr = [4,2,54,243,1,4,6]
    # list.sort() sorts the array in-place. Returns None 
    # list.sort(reverse=True)
    arr.sort()
    print(arr)
main()