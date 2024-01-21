from typing import Any, List, Tuple
from collections import deque
from utils import *
import json

class Graph:

  def __init__(self, config_file="./src/config.json") -> None:
    self.num_nodes = 0
    self.num_edges = 0
    self.adj = {}
    self.start = ""
    self.end = []

    if config_file != None:
              with open(config_file, 'r') as f:
                  self.config_data = json.load(f)


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
 
  def find_short_path_bpm(self, dijkstra=True) -> list:
    """
    Using dijkstra algorithm or bfs, find the shortest path in the Graph class.
    
    the last red bit is the start, and the last green bit is the end.

    Returns:
    - the nodes path start to end

    """
    paths = []
    if dijkstra:
      if len(self.end) > 5:
         debug("Too many end nodes, may take a while.", "warning")
      while self.end != []:
        end = self.end.pop()
        paths.append(self.dijkstra(self.start, end))
        
    shortest_path = 0
    for path in paths:
      if path[1] < shortest_path or shortest_path == 0:
        shortest_path = path[1]
        shortest_path_nodes = path[0]
            
    return shortest_path_nodes
    
  def add_nodes_and_edges_from_list(self, nodes_list):
    """
    Adds nodes and edges to the graph based on a list of tuples representing nodes' positions and colors.

    Parameters:
        nodes_list (List[Tuple[int, int, str]]): A list of tuples representing nodes' positions (x, y) and colors.
    """

    for i in range(len(nodes_list)):
        for j in range(len(nodes_list)):
            if i != j:
                x1, y1, z1, color1 = nodes_list[i]
                x2, y2, z2, color2 = nodes_list[j]

                if color1 != "black" and color2 != "black":
                    node1 = (x1, y1, z1, color1)
                    node2 = (x2, y2, z2, color2)

                    if color1 == "red":
                        self.start = node1
                    elif color1 == "green" and node1 not in self.end:
                        self.end.append(node1)

                    # Check if nodes are adjacent but not diagonal
                    if (abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1) and not (abs(x1 - x2) == 1 and abs(y1 - y2) == 1):
                        if color1 == "white" or color2 == "white":
                            weight = 1
                        
                        elif color1 == "lightgray" or color2 == "lightgray":
                            weight = self.config_data["graph_config"]["lightgray_weight"]

                        elif color1 == "darkgray" or color2 == "darkgray":
                            weight = self.config_data["graph_config"]["darkgray_weight"]

                        self.add_directed_edge(node1, node2, weight)

  def add_edges_between_floors(self):
    nodes_added = []
    for node1, neighbors in self.adj.items():
        x1, y1, z1, color1 = node1
        if z1 == 1 or z1 == -1:  # Check if Z coordinate is one unit above or below
            for node2 in neighbors:
                x2, y2, z2, color2 = node2
                if z2 == z1 + 1 or z2 == z1 - 1:  # Check if Z coordinate is one unit above or below
                    weight = neighbors[node2]
                    self.add_directed_edge(node1, node2, self.config_data["graph_config"]["between_floors_weight"])
                    nodes_added.append((node1, node2))
    debug("Added {} edges between floors".format(len(nodes_added)), "debug")

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
        debug("No path found", "warning")
        return [], 0

    # Calculate the sum of weights along the path
    total_weight = sum(self.adj[path[i]][path[i + 1]] for i in range(len(path) - 1))

    return path, total_weight



  