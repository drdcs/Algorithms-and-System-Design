def find_all_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(graph, node, end, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths

graph = {
    "a": "b",
    "b": "c",
    "c": "d",
    "d": "a"
}

print(find_all_path(graph, 'a', 'd'))