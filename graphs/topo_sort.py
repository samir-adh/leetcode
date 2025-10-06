def topo_sort(graph: dict[str, list[str]]):
    cycle = set()
    visited = set()

    path = []

    def dfs(node: str) -> bool:
        if node in visited:
            return True
        if node in cycle:
            return False
        cycle.add(node)
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        cycle.remove(node)
        visited.add(node)
        path.insert(0, node)
        return True

    for node in graph:
        if not dfs(node):
            return []
    return path


if __name__ == "__main__":
    # Example 1: Simple DAG
    graph1 = {"A": ["C"], "B": ["C", "D"], "C": ["E"], "D": ["E"], "E": []}

    print("Example 1:")
    result1 = topo_sort(graph1)
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
    result2 = topo_sort(graph2)
    print(f"Course order: {result2}")

    # Example 3: Graph with cycle
    graph3 = {"A": ["B"], "B": ["C"], "C": ["A"]}  # Creates a cycle

    print("\nExample 3 (Cycle):")
    result3 = topo_sort(graph3)
    if result3 is None:
        print("Cycle detected! No topological order exists.")
    else:
        print(f"Topological order: {result3}")
