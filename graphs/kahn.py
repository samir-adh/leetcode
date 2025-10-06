def khan(graph: dict[str, list[str]]):
    in_degrees = dict()
    for node in graph:
        in_degrees[node] = 0

    for node in graph:
        for nei in graph[node]:
            in_degrees[nei] += 1

    queue = []
    for node in graph:
        if in_degrees[node] == 0:
            queue.append(node)
    visited = set()
    topo_order = []
    while queue:
        current = queue.pop(0)
        if current in visited:
            return []
        topo_order.append(current)
        for nei in graph[current]:
            in_degrees[nei] -= 1
            if in_degrees[nei] == 0:
                queue.append(nei)
    return topo_order


# Example usage
if __name__ == "__main__":
    # Example 1: Simple DAG
    graph1 = {"A": ["C"], "B": ["C", "D"], "C": ["E"], "D": ["E"], "E": []}

    print("Example 1:")
    result1 = khan(graph1)
    print(f"Topological order: {result1}")

    # Example 2: Course prerequisites
    graph2 = {
        "Math101": ["Math201"],
        "Math201": ["Math301"],
        "Physics101": ["Physics201"],
        "Physics201": [],
        "Math301": [],
    }

    print("\nExample 2 (Courses):")
    result2 = khan(graph2)
    print(f"Course order: {result2}")

    # Example 3: Graph with cycle
    graph3 = {"A": ["B"], "B": ["C"], "C": ["A"]}  # Creates a cycle

    print("\nExample 3 (Cycle):")
    result3 = khan(graph3)
    if result3 is None:
        print("Cycle detected! No topological order exists.")
    else:
        print(f"Topological order: {result3}")
