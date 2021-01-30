from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def addEdges(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1])
    def showGraph(self):
        return self.graph

    def bfs(self, s):
        visited = {}
        for key in self.graph:
            visited[key] = False
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end='->')
            for neighbour in self.graph[s]:
                if visited[neighbour] == False:
                    queue.append(neighbour)
                    visited[neighbour] = True



if __name__ == '__main__':
    number_graph = Graph()
    edges = [(0,1), (0,2), (1,2), (2,0), (2,3), (3,3)]
    edges_c = [('A','B'), ('A','C'), ('B','C'), ('C','A'), ('C','D'), ('D','D')]
    number_graph.addEdges(edges)
    number_graph.bfs(0)
    char_graph = Graph()
    char_graph.addEdges(edges_c)
    char_graph.bfs('A')