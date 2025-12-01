def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    1: [3, 2],
    2: [4],
    3: [5, 4],
    4: [],
    5: []
}

dfs(graph, 1)