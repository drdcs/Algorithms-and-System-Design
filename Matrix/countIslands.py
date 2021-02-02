# Count the number of islands
"""
Given a boolean 2D matrix, find the number of islands. 
A group of connected 1s forms an island. 
For example, the below matrix contains 5 islands.

"""

# How to approach the problem.

"""
1. Let's look at the 2-D matrix as a graph.
2. Traverse the array for all possible connector 
   have 1's.
3. so it's like a BFS call.
4. every point has 8 adjacent cells.left corner, up, right corner etc .. as below.

                    1 0 1
                    1 1 1
                    0 0 0

5. keep a visited array to mark the visited T/F. 
6. 
"""
from collections import deque



def BFS(mat, processed, i, j):
 
    # create an empty queue and enqueue source node
    q = deque()
    q.append((i, j))
 
    # mark source node as processed
    processed[i][j] = True
 
    # loop till queue is empty
    while q:
 
        # pop front node from queue and process it
        x, y = q.popleft()
 
        # check for all 8 possible movements from current cell
        # and enqueue each valid movement
        for k in range(8):
            # Skip if location is invalid or already processed or has water
            if isSafe(mat, x + row[k], y + col[k], processed):
                # skip if location is invalid or it is already
                # processed or consists of water
                processed[x + row[k]][y + col[k]] = True
                q.append((x + row[k], y + col[k]))
 


def isSafe(mat, x, y, processed):
    return (x >= 0) and (x < len(processed)) and \
           (y >= 0) and (y < len(processed[0])) and \
           (mat[x][y] == 1 and not processed[x][y])

           

if __name__ == '__main__':
    mat = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    ]
 
    (M, N) = (len(mat), len(mat[0]))
 
    # stores if cell is processed or not
    processed = [[False for x in range(N)] for y in range(M)]
    row = [-1, -1, -1, 0, 1, 0, 1, 1]
    col = [-1, 1, 0, -1, -1, 1, 0, 1]
    island = 0
    for i in range(M):
        for j in range(N):
            # start BFS from each unprocessed node and increment island count
            if mat[i][j] == 1 and not processed[i][j]:
                BFS(mat, processed, i, j)
                island = island + 1
 
    print("Number of islands are", island)