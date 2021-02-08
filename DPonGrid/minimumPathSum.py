"""
Minimum Path Sum
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes 
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


"""

def findMinimumSum(A):
    row = len(A)
    col = len(A[0])
    # build a path .. 
    path = [[0 for _ in range(col)] for j in range(row)]
    # intialize the path
    path[0][0] = A[0][0]
    # update the path for row and column
    for i in range(1,row):
        path[i][0] = path[i-1][0] + A[i][0]
    # update the path for the column
    for j in range(1, col):
        path[0][j] = path[0][j-1] + A[0][j]
    # traver the array and return the path..
    for i in range(1,row):
        for j in range(1,col):
            path[i][j] = min(path[i-1][j],path[i][j-1]) + A[i][j]
    return path[-1][-1]

if __name__ == '__main__':
    A = [[1,3,1],[1,5,1],[4,2,1]]
    print(findMinimumSum(A))
    A = [[1,3,1,5],[1,5,1,1],[4,2,1,4]]
    print(findMinimumSum(A))