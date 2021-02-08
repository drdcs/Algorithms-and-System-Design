"""
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



"""

def uniquePathsWithObstacles(A):
    # start if the 
    paths = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    
    # Initialize the left corner if no obstacle
    if A[0][0] == 0:
        paths[0][0] = 1
    
    # initializing the first column
    for i in range(1,len(A)):
        if A[i][0] == 0:
            paths[i][0] = paths[i-1][0]

    # initializing the first row
    for i in range(1, len(A[0])):
        if A[0][i] == 0:
            paths[0][i] = paths[0][i-1]

    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[i][j] == 0:
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
    return paths[-1][-1]
     
    
if __name__ == '__main__':
    A = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # 2 ways
    print(uniquePathsWithObstacles(A))
    A = [[0, 0, 0], [1, 1, 0], [0, 0, 0]] 
    print(uniquePathsWithObstacles(A))
    A = [[0, 0, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0]] 
    print(uniquePathsWithObstacles(A))