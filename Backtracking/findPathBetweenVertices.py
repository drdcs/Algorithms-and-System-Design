
"""
           0 <- 1 -> 2
           |    |    |
           3 <->4    |
           |    |    |
           5 -> 6 -> 7

Find path between 0 to 7 ?

=> 0 -> 3 -> 4 -> 6 -> 7 !!

"""

from collections import deque

class Graph:

    def __init__(self, edges, N):

        self.adjList = [[] for _ in range(N)]

        for (src, dst) in edges:
            self.adjList[src].append(dst)

    def get_graph(self):
        for x in range(N):
            print(x ,":", self.adjList[x])

def connected_path(graph, src, dest, discovered, path):

    # mark the src node as discovered ... 

    discovered[src] = dest

    # include the current node in the path ...

    path.append(src)

    # if destination is found then return the path ...

    if src == dest:
        return True

    # travese through the neighbour ... 

    for neighbour in graph.adjList[src]:
        # if neighbour is not yet discovered .. 
        if not discovered[neighbour]:
            if connected_path(graph, neighbour, dest, discovered, path):
                return True
    
    # backtrac: remove the current node from the graph .. 

    path.pop()

    # return false if desination vertext is not yet reachable .. 

    return False

if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [
        (0, 3), (1, 0), (1, 2), (1, 4), (2, 7), (3, 4),
        (3, 5), (4, 3), (4, 6), (5, 6), (6, 7)
    ]
    N = 8
    graph = Graph(edges, N)
    
    print("graph: ")
    print(graph.get_graph())
    discovered = [False] * N

    # src , dst vertex

    src, dest = 0, 7
    path = []

    if connected_path(graph, src, dest, discovered, path):
        print("complete path is : ", path)
    else:
        print("Path not found .. ")
# find path between 0 -> 7 

# class Graph:
#     def __init__(self, edges, N):
#         self.adjList = [[] for _ in range(N)]
#         for (src, dst) in edges:
#             self.adjList[src].append(dst)

# # function to perform BFS
# # determine if dest vertext is reached..
# def isConnected(graph, src, dst, discovered):
#     q = deque()
#     discovered[src] =  True
#     q.append(src)
    
#     while q:
#         v = q.popleft()
#         if v == dst:
#             return True
#         for neighbour in graph.adjList[v]:
#             if not discovered[neighbour]:
#                 discovered[neighbour] = True
#                 q.append(neighbour)
#     return True



# if __name__ == '__main__':
 
#     # List of graph edges as per the above diagram
#     edges = [
#         (0, 3), (1, 0), (1, 2), (1, 4), (2, 7), (3, 4),
#         (3, 5), (4, 3), (4, 6), (5, 6), (6, 7)
#     ]
#     N = 8
#     graph = Graph(edges, N)
#     discovered = [False] * N
#     (src, dst) = (0, 7)
#     print(isConnected(graph, src, dst, discovered))
#     print(discovered)