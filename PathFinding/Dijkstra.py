graph = {
    'a': {'b': 3, 'c': 4, 'd': 7},
    'b': {'c': 1, 'f': 5},
    'c': {'f': 6, 'd': 2},
    'd': {'e': 3, 'g': 6},
    'e': {'g': 3, 'h': 4},
    'f': {'e': 1,'h': 8},
    'g': {'h': 2},
    'h': {'g': 2}
}
def dijkstra(graph, start, end):
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph
    infinity = float('inf')
    path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node]< shortest_distance[min_distance_node]:
                min_distance_node = node
        
        path_options = graph[min_distance_node].items()
        for child , weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child]:
                shortest_distance[child] = weight + shortest_distance[min_distance_node]
                track_predecessor[child]= min_distance_node
        unseenNodes.pop(min_distance_node)
    currentNode = end
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print("Path is not reachable:")
            break
    path.insert(0, start)

    if shortest_distance[end] != infinity:
        print("Shortest Distance is: "+ str(shortest_distance[end]))
        print("optimal path is " + str(path) )

if __name__ == '__main__':
    dijkstra(graph, 'a', 'h')