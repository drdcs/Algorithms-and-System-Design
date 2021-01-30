from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        for v in vertices:
            self.graph[v]
    
    def addEdge(self, s, d):
        self.graph[s].append(d)
        self.graph[d].append(s)
    
    def addFromEdges(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1])
    
    def showGraph(self):
        for item in self.graph.items():
            print(item)
    # a recursive function that uses visited 
    # and parent to dected cycle.

    def isCyclicUtil(self, node, visited, parent):
        visited[node] = True
        
        for neighbour in self.graph[node]:
            if visited[neighbour] == False:
                if(self.isCyclicUtil(neighbour, visited, node)):
                    return True
            elif neighbour != parent:
                return True
        return False


    def isCyclic(self):
        visited = {}
        for key in self.graph.keys():
            visited[key] = False

        for node in self.graph.keys():
            if visited[node] == False:
                if(self.isCyclicUtil(node, visited, -1)==True):
                    return True
        return False
        

if __name__ == '__main__':
    v = [0,1,2,3,4]
    edges = [(1, 0) , (1, 2), (2, 0), (0, 3) , (3, 4) ]
    g = Graph(v) 
    g.addFromEdges(edges)
    g.showGraph()
    print(g.isCyclic())

    print("#####################")
    edges = [(0,1),(1,2)]
    v = [0,1,2]
    g = Graph(v)
    g.addFromEdges(edges)
    g.showGraph()
    print(g.isCyclic())
