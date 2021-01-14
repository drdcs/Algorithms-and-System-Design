# why bfs ? 
# BFS always make sure to give shortest path.
# Condition: Graph must have no cycles and not weighted.

# How we should approach ? 
### queue = startnode , bfs

def find_shortest_path(graph, start_node, end_node):

    if start_node == end_node:
        return ''.join(start_node)
    queue = [[start_node]]
    ## add this section if graph is un-directed
    visited = set()

    while queue:
        path = queue.pop(0)
        parent = path[-1]
        neighbours = graph[parent]
        if parent not in visited:
            for neighbour in neighbours:
                new_path = path + [neighbour]
                queue.append(new_path)
                if neighbour == end_node:
                    return new_path, visited
        visited.add(parent)
    return "no_path"

graph = {
    "a": ["c", "b"],
    "b": "d",
    "c": "e",
    "e": "d",
    "d": ["f", "z"],
    "f": "q",
    "q": "z"
}

print(find_shortest_path(graph, "a", "z"))