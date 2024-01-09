from typing import Any, List, Tuple
from collections import deque

class Graph:

  def __init__(self) -> None:
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
    
    
  def find_short_path_bpm(self,matrix, dijkstra=True) -> list:
    """
    Using dijkstra algorithm or bfs, find the shortest path in the Graph class.
    
    the last red bit is the start, and the last green bit is the end.

    Returns:
    - the nodes path start to end

    """
    paths = []
    if dijkstra:
      if len(self.end) > 5:
         print("Too many end nodes, this may take a while") # thats why optimization is a needed workplace
      while self.end != []:
        end = self.end.pop()
        paths.append(self.dijkstra(self.start, end))

    shortest_path = None
    for path in paths:
      if shortest_path is None or len(path) < len(shortest_path):
        shortest_path = path

    for i in range(len(shortest_path)):
        x = shortest_path[i][0]
        y = shortest_path[i][1]
        if shortest_path[i][2] != 'red' and shortest_path[i][2] != 'green':
            matrix[y][x] = 6
    
    return matrix
            
    
  def add_nodes_and_edges_from_list(self, nodes_list):
    """
    Adds nodes and edges to the graph based on a list of tuples representing nodes' positions and colors.

    Parameters:
        nodes_list (List[Tuple[int, int, str]]): A list of tuples representing nodes' positions (x, y) and colors.
    """

    for i in range(len(nodes_list)):
        for j in range(len(nodes_list)):
            if i != j:
                x1, y1, color1 = nodes_list[i]
                x2, y2, color2 = nodes_list[j]

                if color1 != "black" and color2 != "black":
                    node1 = (x1, y1, color1)
                    node2 = (x2, y2, color2)

                    if color1 == "red":
                        self.start = node1
                    elif color1 == "green" and node1 not in self.end:
                        self.end.append(node1)

                    # Check if nodes are adjacent but not diagonal
                    if (abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1) and not (abs(x1 - x2) == 1 and abs(y1 - y2) == 1):
                        if color1 == "white" or color2 == "white":
                            weight = 1
                        
                        elif color1 == "light_gray" or color2 == "light_gray":
                            weight = 1.5

                        elif color1 == "dark_gray" or color2 == "dark_gray":
                            weight = 2

                        self.add_directed_edge(node1, node2, weight)




  def dijkstra(self, start, end):
    """Dijkstra algorithm implementation."""
    
    distances = {node: float('infinity') for node in self.adj}
    distances[start] = 0
    visited = set()
    
    # Predecessor dictionary to store the previous node in the shortest path
    predecessors = {node: None for node in self.adj}

    while len(visited) < len(self.adj):
        # Select the node with the smallest distance that is not visited
        unvisited_nodes = [node for node in distances if node not in visited]
        if not unvisited_nodes:
            break

        current_node = min(unvisited_nodes, key=lambda x: distances[x])

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
        print("No path found")
        return []

    return path


  