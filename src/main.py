from bmp_matrix import *
from get_data_from_image import *
from graph import *
import networkx as nx

# Matriz de entrada
matrix = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #0-> branco, 1-> preto, 2-> vermelho, 3 -> verde
        [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0]
    ]

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
    node_titles = {node: f'{node[0],{node[1]}}' for node in G.nodes()}

    # Draw the graph
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', labels=node_titles, node_size=1000, font_size=4, font_color='black', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # Show the plot
    plt.show()

if __name__ == "__main__":

    g = Graph()
    image_path = "images/output.bmp"
    matrix_to_bmp(matrix, image_path)
    graph_list = (rgb_image_to_list(image_path))
    
    

    
    for i in range(len(graph_list)):
        for j in range(len(graph_list)):
            if i != j and graph_list[i][2] != "black" and graph_list[j][2] != "black":
                x1, y1, color1 = graph_list[i]
                x2, y2, color2 = graph_list[j]

                if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 and (x1 != x2 or y1 != y2):
                    g.add_directed_edge(graph_list[i], graph_list[j], 1)

        else:
            g.add_node(graph_list[i])
            

    draw_oriented_graph(g.adj)