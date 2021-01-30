"""
Check if a graph contains cycle or not.

"""

from collections import defaultdict

class Graph:

    def __init__(self, Vlist):
        self.graph = defaultdict(list)
        for v in Vlist:
            self.graph[v]
            
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def addEdges(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1])

    def showGraph(self):
        for item in self.graph.items():
            print(item)

    def isCyclicUtil(self, node, visited, recStack):

        visited[node] = True
        recStack[node] = True

        for neighbour in self.graph[node]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        recStack[node] = False
        return False       

    def isCyclic(self):
        visited = {}
        recStack = {}
        for key in self.graph.keys():
            visited[key] = False
            recStack[key] = False
        for node in visited.keys():
            if visited[node] == False:
                if self.isCyclicUtil(node, visited,recStack) == True:
                    return True
        return False

if __name__ == '__main__':
    edges = [('A','B'),('B','C'),('C','D'),('D','E'),('E','B')]
    V = ['A','B','C','D','E']
    g = Graph(V)
    g.addEdges(edges)
    print(g.isCyclic())