def dfs(graph, node_from, visited=None):
    if visited is None:
        visited = set()

    visited.add(node_from)
    print(node_from)  # Відвідуємо вершину

    for neighbor in graph[node_from]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
