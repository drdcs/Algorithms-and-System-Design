"""
Goal: Given a set of people (connected as a graph). Find if it is possible
to partition people into 2 sets such that no person in the set hates 
each other.

Example: [[1,3], [1,4], [2,4]]

1 --- 3
|          This can group intO 2 sets [1,2] , [3,4] => True
4 --- 2

[[1,3], [1,4], [2,4], [1,2]] 
1 --- 3
| \        we can group intO 2 sets [1,2] , [3,4] => False
4 - 2

"""

## What is Bi-Partitite Property ?

'''

1. A Bipartite graph is a graph whose vertices can be divided into 2 disjoint and
   Independent sets U and V such that every edge connects a vertex in U to
   a vertex in V.

2. A bipartite graph can only have a even edge length cycle.

'''

## How to Solve ?

'''
Step 1 : Make adjancency List.
Step 2 : if there is no odd length cycle then graph is Bipartitie.

'''

from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        for v in V:
            self.graph[v]
    def addEdges(self, u, v):
        self.graph[u].append(v)
    
    def addEdgesFromList(self, edges):
        for edge in edges:
            self.addEdges(edge[0], edge[1])
    def showGraph(self):
        for item in self.graph.items():
            print(item)

    def isHateful(self, node):
        color = {}
        for key in self.graph.keys():
            color[key] = -1
        queue = []
        queue.append(node)
        color[node] = 1
        while queue:
            currNode = queue.pop(0)
            for neighbour in self.graph[currNode]:
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[currNode]
                    queue.append(neighbour)
                elif color[neighbour] == color[currNode]:
                    return False
        return True

if __name__ == '__main__':
    edges = [(1,2), (2,3),(2,4),(3,5),(4,5),(1,4)]
    edges_1 = [("A","B"), ("B", "C"), ("C", "D"), ("D", "A"), ("C", "A")]
    V = [1,2,3,4,5]
    V_1 = ["A", "B", "C", "D"]
    g = Graph(V_1)
    g.addEdgesFromList(edges_1)
    g.showGraph()
    print(g.isHateful("A"))

