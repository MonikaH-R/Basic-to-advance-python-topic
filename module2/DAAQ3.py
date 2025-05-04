from collections import defaultdict, deque
def topological_sort_kahn(vertices, edges):
    graph = defaultdict(list)
    in_degree = [0] * vertices

    # Build the graph
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Queue of all vertices with in-degree 0
    queue = deque([v for v in range(vertices) if in_degree[v] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == vertices:
        return topo_order
    else:
        return None  # Graph contains a cycle
# ---- GRAPH 1: 7 vertices, 10 edges ----
vertices_1 = 7
edges_1 = [
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4),
    (2, 4),
    (2, 3),
    (3, 5),
    (4, 5),
    (4, 6),
    (5, 6)
]
print("Topological Sort for Graph with 7 vertices:")
result_1 = topological_sort_kahn(vertices_1, edges_1)
print(" → ".join(map(str, result_1)) if result_1 else "Graph has a cycle.\n")
# ---- GRAPH 2: 10 vertices, 15 edges ----
vertices_2 = 10
edges_2 = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 5),
    (5, 6),
    (6, 7),
    (1, 7),
    (7, 8),
    (8, 9),
    (4, 9),
    (3, 9),
    (6, 9)
]
print("\nTopological Sort for Graph with 10 vertices:")
result_2 = topological_sort_kahn(vertices_2, edges_2)
print(" → ".join(map(str, result_2)) if result_2 else "Graph has a cycle.")
