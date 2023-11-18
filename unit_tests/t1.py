import matplotlib.pyplot as plt
import networkx as nx

def draw_oriented_graph(graph_dict):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges to the graph
    for node, neighbors in graph_dict.items():
        G.add_node(node)
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    # Specify node positions for better layout
    pos = {node: (node[0], -node[1]) for node in G.nodes()}

    # Extract edge weights for edge labels
    edge_labels = {(node, neighbor): weight for node, neighbor, weight in G.edges(data='weight')}

    # Draw the graph
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_color='black', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # Show the plot
    plt.show()

# Example usage with the provided graph dictionary
graph_dict = {(0, 0, 'white'): {(1, 0, 'white'): 1, (0, 1, 'white'): 1},
              (1, 0, 'white'): {(0, 0, 'white'): 1, (2, 0, 'white'): 1, (0, 1, 'white'): 1},
              (0, 1, 'white'): {(0, 0, 'white'): 1, (1, 0, 'white'): 1, (0, 2, 'white'): 1}}

draw_oriented_graph(graph_dict)
