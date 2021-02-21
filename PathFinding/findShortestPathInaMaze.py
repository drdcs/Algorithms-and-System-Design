"""
Input:
mat[ROW][COL]  = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
                  [1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
                  [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
                  [1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
                  [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
                  [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
                  [1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]
Source = [0, 0];
Destination = [3, 4];

Output:
Shortest Path is 11 

"""

# possible solution is by backtracking or bfs. keeping time complexity of back tracking is high we need to 
# think through a bfs solution.

"""
Part 1 thinking process:

1. There are 4 possible movements either up ,down or left right
2. the other possible movement is by the matrix value 1.
3. so, we need to validate the position by isValid function.

Part 2 thinking process:

4. as we have discussed the bfs way( as bfs gurentee a shortest path ), 
   the best possible data structure to implement a bfs is queue.

5. in the queue we need to define the co-ordinates along with the distance.(i, j, distance)
   if destination found hten return the distance.

Algorithm Design:

1. create an empty queue and enqueue the source having the distance 0 and mak aux matrix visited.
2. Loop till queue is empty:
    - deque the front node.
    - if poped node is the destination , then return
    - otherwise for each of the four adjacent cell, enqueue each valid cell with +1 distance.
3. if all the nodes are visited and destination not found then return the o/p as False.

"""

# all 4 movements in a cell.
import sys
from collections import deque

row = [-1, 0, 0 , 1]
col = [ 0, -1, 1, 0]

# as discussed above, the below function checks if its possible go all above positions for non-visisted nodes..

def isValid(mat, visited, row, col):
    return (row >=0) and (row < M) and (col >= 0) and (col < N) and mat[row][col] == 1 and not visited[row][col]

## implement the bfs
# i, j is the source and x, y destination..
def bfs(mat, i, j, x, y):

    # aux matrix to define the visisted nodes..
    visited = [[False for _ in range(N)] for _ in range(M)]

    # create a queue.
    q = deque()
    # mark the current element as true
    visited[i][j] = True

    q.append((i, j, 0))

    # store the max size from src to dest and updates accordingly.

    min_dist = sys.maxsize

    while q:
        (i, j, dist) = q.popleft()
        print("(i, j, dist)", (i, j, dist))

        # check if we reached the destination

        if i == x and j == y:
            min_dist = dist
            break

        # check for all possible direction from curent coordinates.

        for k in range(4):
            if isValid(mat, visited, i + row[k], j + col[k]):
                visited[i+row[k]][j + col[k]] = True
                q.append((i + row[k], j+ col[k], dist+ 1))

    if min_dist != sys.maxsize:
        print("shortest distance is: ", min_dist)
    else:
        print("destination can not be found..")


if __name__ == '__main__':

    mat = [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]
    
    M, N = 10, 10
    i, j = 0, 0
    k, l = 9, 9

    bfs(mat, i, j, k, l)