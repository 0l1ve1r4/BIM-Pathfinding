def dijkstra(graph, start, end):

    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()

    # Predecessor dictionary to store the previous node in the shortest path
    predecessors = {node: None for node in graph}

    while len(visited) < len(graph):
        # Select the node with the smallest distance that is not visited
        current_node = min((node for node in graph if node not in visited), key=lambda x: distances[x])

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight

            if distance < distances.get(neighbor, float('infinity')):
                distances[neighbor] = distance
                predecessors[neighbor] = current_node

    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]

    return path

# Example usage
graph = {(0, 0, 'white'): {(1, 0, 'white'): 1, (0, 1, 'white'): 1},
         (1, 0, 'white'): {(0, 0, 'white'): 1, (2, 0, 'white'): 1, (0, 1, 'white'): 1},
         (0, 1, 'white'): {(0, 0, 'white'): 1, (1, 0, 'white'): 1, (0, 2, 'white'): 1}}

start_node = (0, 0, 'white')
end_node = (0, 2, 'white')

shortest_path = dijkstra(graph, start_node, end_node)
print(shortest_path)
