'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

'''

def sol(m):

    def adjacent(i,j):
        count = 0
        adj = (i+1,j), (i-1,j), (i,j+1), (i,j-1)
        for x,y in adj:
            if x < 0 or y < 0 or x == len(m) or y == len(m[0]) or m[x][y] == 0:
                count += 1
        return count

    res = 0
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            if m[i][j] == 1:
                res += adjacent(i,j)
    return res

m = [[0,1,0,0], [1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(sol(m))