from typing import Any, List, Tuple
from collections import deque

class Graph:

  def __init__(self):
    self.num_nodes = 0
    self.num_edges = 0
    self.adj = {}
    self.start = ""
    self.end = []

  def add_node(self, node: Any) -> None:
    """
    Adds a node to the graph.

    Parameters:
        node (Any): The node to be added (as a key to a dict)
    """
    try: 
      if self.adj[node] != {}:
        return
    except KeyError:
      self.adj[node] = {}
      self.num_nodes += 1
      
  def add_nodes(self, nodes: List[Any]) -> None:
    """
    Adds a list of nodes to the graph

    Parameters:
        nodes (List[Any]): The list of nodes to be added (as keys to a dict)
    """
    for node in nodes:
      self.add_node(node)
      
  def add_directed_edge(self, u, v, weight):
    """
    Add a directed edge from node 'u' to node 'v' with the specified weight.

    Parameters:
    - u: The source node.
    - v: The target node.
    - weight: The weight of the directed edge.

    If the nodes 'u' and 'v' do not exist in the graph, they are added using the 'add_node' function.
    """
    self.add_node(u)
    self.add_node(v)
    self.adj[u][v] = weight
    self.num_edges += 1

  def add_undirected_edge(self, u, v, weight):
    """
    Add a two-way (undirected) edge between nodes 'u' and 'v' with the specified weight.

    Parameters:
    - u: One of the nodes.
    - v: The other node.
    - weight: The weight of the undirected edge.

    This function calls the 'add_edge' function for both (u, v) and (v, u) to represent the undirected edge.
    """
    self.add_directed_edge(u, v, weight)
    self.add_directed_edge(v, u, weight)
    
    
  def find_short_path_bpm(self, matrix:list) -> list:
    """
    Using dijkstra algorithm, find the shortest path in the Graph class.
    
    the last red bit is the start, and the last green bit is the end.

    Returns:
    - the nodes path start to end

    """
    
    paths = []
    shortest_path = []
    
    while self.end != []:
        current_node = self.end.pop()
        paths.append(self.dijkstra(self.start, current_node))   

    for path in paths:
      if len(path) < len(shortest_path):
        shortest_path = path

    for i in range(len(shortest_path)):
        x = shortest_path[i][0]
        y = shortest_path[i][1]
        if shortest_path[i][2] != 'red' and shortest_path[i][2] != 'green':
            matrix[y][x] = 3
    
    return matrix
            
    
  def add_bpm(self, graph_list):
    """Receives a list of tuples (x, y, color) and adds the nodes and edges to the graph."""
    for i in range(len(graph_list)):
      for j in range(len(graph_list)):
          if i != j and graph_list[i][2] != "black" and graph_list[j][2] != "black":
              x1, y1, color1 = graph_list[i]
              x2, y2, color2 = graph_list[j]

              if graph_list[i][2] == "red":
                self.start = graph_list[i]
              if graph_list[i][2] == "green":
                self.end.append(graph_list[i])

              # Check if nodes are adjacent but not diagonal
              if (abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1) and not (abs(x1 - x2) == 1 and abs(y1 - y2) == 1):
                  self.add_directed_edge(graph_list[i], graph_list[j], 1)
          #else:
              #self.add_node(graph_list[i]) # adiciona o nós pretos
              
  def dijkstra(self, start, end):
    """Dijkstra algorithm implementation."""

    distances = {node: float('infinity') for node in self.adj}
    distances[start] = 0
    visited = set()
    
    # Predecessor dictionary to store the previous node in the shortest path
    predecessors = {node: None for node in self.adj}

    while len(visited) < len(self.adj):
        # Select the node with the smallest distance that is not visited
        current_node = min((node for node in self.adj if node not in visited), key=lambda x: distances[x])

        visited.add(current_node)

        for neighbor, weight in self.adj[current_node].items():
            distance = distances[current_node] + weight

            if distance < distances.get(neighbor, float('infinity')):
                distances[neighbor] = distance
                predecessors[neighbor] = current_node

    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
        
    if path[-1] != end and path[0] != start:
        print("Error: No path found")
        return []
      
    

    return path

  def bfs(self, start, end):
    """Breadth-First Search implementation."""
    
    queue = deque([start])
    visited = set([start])

    # Predecessor dictionary to store the previous node in the shortest path
    predecessors = {node: None for node in self.adj}

    while queue:
        current_node = queue.popleft()

        for neighbor, weight in self.adj[current_node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                predecessors[neighbor] = current_node

    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]

    if path[-1] != end and path[0] != start:
        print("Error: No path found")
        return []

    return path

  def __repr__(self) -> str:
    str = ""
    for u in self.adj:
      str += f"{u} -> {self.adj[u]}\n"
    return str

 