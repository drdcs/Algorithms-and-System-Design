from collections import defaultdict

class Graph:
    

    def __init__(self):
        # default dict to store the graph
        self.graph = defaultdict(list)
        # functions to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def addFromEdges(self, edges):

        """
        Edges should be in List of Tuples.
        ex: [(0,1),(0,2),(0,3),(1,2)]

        """
        for edge in edges:
            self.addEdge(edge[0], edge[1])          

    def DFSUtil(self, currentNode, visitedSet):
        # mark the currentNode as visited.
        visitedSet.add(currentNode)
        print(currentNode, end="->")
        for neighbour in self.graph[currentNode]:
            if neighbour not in visitedSet:
                self.DFSUtil(neighbour, visitedSet)
    
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)


if __name__ == '__main__':

    number_graph = Graph()
    edges = [(0,1), (0,2), (1,2), (2,0), (2,3), (3,3)]
    number_graph.addFromEdges(edges)
    number_graph.DFS(0)