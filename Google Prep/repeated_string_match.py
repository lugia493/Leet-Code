def rss(A, B):
    # Problem 686

    # Important note, '//' operator rounds down to negative infinity
    # We want lower bound here. len(B) // len(A) will give us the floor of the division. Ex. 5//3 == 1 (1.6667 -> 1)
    # Now we want the ceiling actually, so if we do -len(B) // len(A) we get lower bound. Ex. -5//3 == -2 (-1.66 -> -2)
    # Well if we negate -2, we actually get the lower bound we want, which for example lower bound of 5//3 is 2
    times = -(-len(B) // len(A))

    # We only need to search 2 values to see if B is in A
    # We know the lower bound, and if we add one more value to this lower bound, than A >= B
    # If B is not in A in this instance, than is sure enough wont be in A if we keep adding A to A
    # therefore, we only need to check if B is in A when we multiple A by times (lower bound) and by 
    # adding A one more time. 
    for i in range(2):
        if B in (A * (times + i)):
            return times * i
    return -1
    

def main():
    A = "abc"
    B = "cabcabca"

    print(rss(A,B))
main()