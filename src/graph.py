from typing import Any, List, Tuple
from collections import deque

class Graph:

  def __init__(self):
    self.num_nodes = 0
    self.num_edges = 0
    self.adj = {}
    self.start = ""
    self.end = ""

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
    
    
  def find_short_path_bpm(self,matrix) -> list:
    """
    Using dijkstra algorithm, find the shortest path in the Graph class.
    
    the last red bit is the start, and the last green bit is the end.

    Returns:
    - the nodes path start to end

    """
    
    shortest_path = self.dijkstra(self.start, self.end)   
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
                self.end = graph_list[i]

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
        
    if path[-1] != start:
        print("No path found")
        return []

    return path



  def __repr__(self) -> str:
    str = ""
    for u in self.adj:
      str += f"{u} -> {self.adj[u]}\n"
    return str

  def there_is_edge(self, u, v) -> bool:
    """
    Check if there is a directed edge from node u to node v in the graph.

    Parameters:
    - u: Source node.
    - v: Target node.

    Returns:
    True if there is an edge from u to v, False otherwise.
    """
    try:
      self.adj[u][v]
      return True
    except KeyError:
      return False
    
  def neighbors(self, node: Any) -> List[Any]:
    """
    Return a list of neighbor nodes for the given node.

    Parameters:
    - node: The node for which neighbors are to be retrieved.

    Returns:
    A list of neighbor nodes connected to the specified node.
    """
    return list(self.adj[node].keys())

  def degree_out(self, node: Any) -> int:
    """
    Return the out-degree of the specified node.

    Parameters:
    - node: The node for which the out-degree is to be calculated.

    Returns:
    The out-degree of the specified node.
    """
    return len(self.adj[node])
  
  def degree_in(self, node: Any) -> int:
    """
    Return the in-degree of the specified node.

    Parameters:
    - node: The node for which the in-degree is to be calculated.

    Returns:
    The in-degree of the specified node.
    """
    count = 0
    for key in self.adj:
      if node in self.adj[key]:
        count += 1
    return count  

  def highest_degree_in(self) -> int:
    """
    Return the highest in-degree in the graph.

    Returns:
    The highest in-degree in the graph.
    """
    highest = 0
    for node in self.adj:
      degree_in_node = self.degree_in(node)
      if degree_in_node > highest:
        highest = degree_in_node
    return highest
  
  def density(self) -> float:
    """
    Return the density of the graph.

    Returns:
    The density of the graph.
    """
    return self.num_edges / (self.num_nodes * (self.num_nodes - 1))
  
  def is_regular(self):
    """
    Check if the graph is regular.

    Returns:
    True if the graph is regular, False otherwise.
    """
    first_node = list(self.adj.keys())[0]
    degree_first_node = self.adj[first_node]
    for node in self.adj:
      if len(self.adj[node]) != degree_first_node:
        return False
      
  def is_oriented(self):
    """
    Check if the graph is oriented.

    Returns:
    True if the graph is oriented, False otherwise.
    """
    for u in self.adj:
      for v in self.adj[u]:
        if not self.there_is_edge(v, u):
          return False
    return True

  def is_complete(self) -> bool:
    """
    Check if the graph is complete.

    Returns:
    True if the graph is complete, False otherwise.
    """
    return self.density() == 1
    

  def is_subgraph_of(self, g2) -> bool:
    """
    Check if the graph is a subgraph of another graph g2.

    Parameters:
    - g2: The graph to check against.

    Returns:
    True if the graph is a subgraph of g2, False otherwise.
    """
    if self.num_nodes > g2.num_nodes or self.num_edges > g2.num_edges:
      return False
    for u in self.adj:
      for v in self.adj[u]:
        if not g2.there_is_edge(u, v):
          return False
    return True

  def strongest_connection(self):
    """
    Return the edge having the highest weight in the graph.

    Returns:
    A tuple (u, v, weight) representing the strongest connection in the graph.
    """
    strongest = (None, None, float("-inf"))
    for u in self.adj:
      for v in self.adj[u]:
        if self.adj[u][v] > strongest[2]:
          strongest = (u, v, self.adj[u][v])
    return strongest
   
  def weakest_connection(self):
    """
    Return the edge having the weakest weight in the graph.

    Returns:
    A tuple (u, v, weight) representing the weakest connection in the graph.
    """
    weakest = (None, None, float("inf"))
    for u in self.adj:
      for v in self.adj[u]:
        if self.adj[u][v] < weakest[2]:
          weakest = (u, v, self.adj[u][v])
    return weakest

  def normalize_weights(self) -> None:
    """
    Normalize the edge weights in the graph.

    This function normalizes the edge weights in the graph to a range between 0 and 1.
    If all weights are the same, a warning is printed.
    """
    highest_weight = self.strongest_connection()[2]
    smallest_weight = self.weakest_connection()[2]
    if highest_weight - smallest_weight == 0:
      print("WARN:  all weights are the same")
      return
    for u in self.adj:
      for v in self.adj[u]:
        self.adj[u][v] = (self.adj[u][v] - smallest_weight) / (highest_weight - smallest_weight)
