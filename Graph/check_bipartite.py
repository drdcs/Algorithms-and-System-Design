'''
1. find the neighbour of a tree.
2. color the node and it's neighbour should have different color.
'''
graph = {
    "a": "b",
    "b": "c",
    "c": "d",
    "d": "a"
}


def is_bipartite(graph, node, color={}):
    color[node] = 1
    queue = []
    queue.append(node)
    while queue:
        parent = queue.pop(0)
        neighbours = graph[parent]
        for neighbour in neighbours:
            if color.get(neighbour) is None:
                color[neighbour] = 1 - color[parent]
                queue.append(neighbour)
            elif color[neighbour] == color[parent]:
                return False
    return True


# def generate_edges(graph):
#     edges = []
#     for node in graph:
#         for neighbour in graph[node]:
#             edges.append((node, neighbour))
#     return edges


# print(generate_edges(graph))

graph_1 = {
    1: [2],
    2: [3],
    3: [4, 5],
    4: [5],
    5: [6],
    6: [1]
} 

graph_2 = {
    "a": "b",
    "b": "c",
    "c": "d",
    "d": "a"
}

print(is_bipartite(graph_1, 1))
print(is_bipartite(graph_2,"a"))