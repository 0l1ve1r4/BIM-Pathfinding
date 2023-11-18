from typing import Any, List, Tuple
class Graph:

  def __init__(self):
    self.num_nodes = 0
    self.num_edges = 0
    self.adj = {}

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
    pass
    
  def neighbors(self, node: Any) -> List[Any]:
    """
    Return a list of neighbor nodes for the given node.

    Parameters:
    - node: The node for which neighbors are to be retrieved.

    Returns:
    A list of neighbor nodes connected to the specified node.
    """
    pass

  def degree_out(self, node: Any) -> int:
    """
    Return the out-degree of the specified node.

    Parameters:
    - node: The node for which the out-degree is to be calculated.

    Returns:
    The out-degree of the specified node.
    """
    pass
  
  def degree_in(self, node: Any) -> int:
    """
    Return the in-degree of the specified node.

    Parameters:
    - node: The node for which the in-degree is to be calculated.

    Returns:
    The in-degree of the specified node.
    """
    pass
 
  def highest_degree_in(self) -> int:
    """
    Return the highest in-degree in the graph.

    Returns:
    The highest in-degree in the graph.
    """
    pass

  def density(self) -> float:
    """
    Return the density of the graph.

    Returns:
    The density of the graph.
    """
    pass
  
  def is_regular(self):
    """
    Check if the graph is regular.

    Returns:
    True if the graph is regular, False otherwise.
    """
    pass

  def is_oriented(self):
    """
    Check if the graph is oriented.

    Returns:
    True if the graph is oriented, False otherwise.
    """
    pass

  def is_complete(self) -> bool:
    """
    Check if the graph is complete.

    Returns:
    True if the graph is complete, False otherwise.
    """
    pass

  def is_subgraph_of(self, g2) -> bool:
    """
    Check if the graph is a subgraph of another graph g2.

    Parameters:
    - g2: The graph to check against.

    Returns:
    True if the graph is a subgraph of g2, False otherwise.
    """
    pass

  def strongest_connection(self) -> Tuple[Any, Any, float]:
    """
    Return the edge having the highest weight in the graph.

    Returns:
    A tuple (u, v, weight) representing the strongest connection in the graph.
    """
    pass
   
  def weakest_connection(self) -> Tuple[Any, Any, float]:
    """
    Return the weakest connection in the graph.

    Returns:
    A tuple (u, v, weight) representing the weakest connection in the graph.
    """
    pass

  def normalize_weights(self) -> None:
    """
    Normalize the edge weights in the graph.

    This function normalizes the edge weights in the graph to a range between 0 and 1.
    If all weights are the same, a warning is printed.
    """
    pass

  def bfs(self, s: Any) -> List[Any]:
    """
    Perform Breadth-First Search (BFS) starting from the specified source node.

    Parameters:
    - s: The source node for the BFS traversal.

    This function explores the graph in breadth-first order starting from the given source node 's'.
    """
    pass

  def dfs(self, s: Any) -> List[Any]:
    """
    Perform Depth-First Search (DFS) starting from the specified source node.

    Parameters:
    - s: The source node for the DFS traversal.

    This function explores the graph in depth-first order starting from the given source node 's'.
    """
    pass

  def dfs_rec(self, s: Any) -> List[Any]:
    """
    Perform Recursive Depth-First Search (DFS) starting from the specified source node.

    Parameters:
    - s: The source node for the recursive DFS traversal.

    This function uses recursion to explore the graph in depth-first order starting from the given source node 's'.
    """
    pass

  def node_with_highest_degree_in(self) -> Any:    
    """
    Find and return the node with the highest in-degree in the graph.

    Returns:
    The node with the highest in-degree in the graph.
    """
    pass

  def node_with_highest_degree_out(self) -> Any:    
    """
    Find and return the node with the highest out-degree in the graph.

    Returns:
    The node with the highest out-degree in the graph.
    """
    pass

  def remove_node(self, node: Any) -> None:    
    """
    Remove the specified node from the graph.

    Parameters:
    - node: The node to be removed from the graph.
    """
    pass

  def remove_directed_edge(self, u: Any, v: Any) -> None:    
    """
    Remove the directed edge from node 'u' to node 'v' in the graph.

    Parameters:
    - u: The source node.
    - v: The target node.
    """
    pass

  def remove_undirected_edge(self, u: Any, v: Any) -> None:    
    """
    Remove the undirected edge between nodes 'u' and 'v' in the graph.

    Parameters:
    - u: One of the nodes.
    - v: The other node.
    """
    pass
