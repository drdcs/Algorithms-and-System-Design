"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Exampple: 1

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


"""


def numberOfPaths(m,n):
    # function to return count of possible path
    # to reach cell at row number m and column n
    
    # BASE CASE:

    # if either given row number is first
    # or ccolumn number is first
    if (m==1 or n==1):
        return 1
    
    return numberOfPaths(m-1, n) + numberOfPaths(m, n-1)


# Returns count of possible paths to reach cell  
# at row number m and column number n from the  
# topmost leftmost cell (cell at 1, 1) 

def numberOfPathsGrid(m,n):
    grid = [[0 for _ in range(m)] for _ in range(n)]

    # count paths to reach any
    # cell in first column
    for i in range(m):
        grid[0][i] = 1

    # count path to reach any
    # cell in first row

    for i in range(n):
        grid[i][0] = 1

    # calculate count paths for other
    # cells in bottom up
    
    for i in range(1, n):
        for j in range(1, m):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[-1][-1]


if __name__ == '__main__':
    m = n = 3
    print(numberOfPaths(m,n))
    print(numberOfPathsGrid(m,n))

    m = 4 
    n = 3
    print(numberOfPaths(m,n))
    print(numberOfPathsGrid(m,n))


