'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True

'''


def solution(m):
    for i in range(len(m) - 1):
        for j in range(len(m[0]) - 1):
            if m[i][j] != m[i + 1][j + 1]:
                return False
    return True

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
print(solution(matrix))