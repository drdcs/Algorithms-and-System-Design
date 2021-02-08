"""
Given a 2D binary matrix filled with 0’s and 1’s, 
find the largest square containing only 1’s and return its area.

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

0 1 1 1
0 0 1 1

Output: 4

"""
def findLargestGrid(A):
    col = len(A[0])
    row = len(A)
    path = [[0 for _ in range(col+1)] for j in range(row+1)]
    largest = 0
    for i in range(1,row+1):
        for j in range(1, col+1):
            if A[i-1][j-1] == 1:
                path[i][j] = 1 + min(path[i-1][j], path[i][j-1], path[i-1][j-1])
                if largest < path[i][j]:
                    largest = path[i][j]
    return largest

if __name__ == '__main__':
    A = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
    print(findLargestGrid(A))
    mat = [
        [0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1]
    ]
    print(findLargestGrid(mat))
    mat = [
        [0, 0, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 0]
    ]
    print(findLargestGrid(mat))
