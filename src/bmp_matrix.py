from PIL import Image
import matplotlib.pyplot as plt
import networkx as nx

def matrix_to_bmp(matrix: list, image_path: str) -> None:
    color_mapping = {
        0: (255, 255, 255),  # Branco
        1: (0, 0, 0),  # Preto
        2: (255, 0, 0),  # Vermelho
        3: (0, 255, 0),  # Verde
        9: (0, 0, 255)  # Azul
    }

    img = Image.new('RGB', (len(matrix[0]), len(matrix)))
    for y in range(img.height):
        for x in range(img.width):
            img.putpixel((x, y), color_mapping[matrix[y][x]])

    img.save(image_path)


def rgb_image_to_list(image_path: str) -> list:
    img = Image.open(image_path)
    width, height = img.size

    categorized_pixel_list = []

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))

            if r == 255 and g == 255 and b == 255:  
                color = "white"
            elif r == 0 and g == 255 and b == 0:   
                color = "green"
            elif r == 0 and g == 0 and b == 0:     
                color = "black"
            elif r == 255 and g == 0 and b == 0:    
                color = "red"
            elif r == 0 and g == 0 and b == 255:    
                color = "blue"
            else:
                color = "unknown"

            categorized_pixel_list.append((x, y, color))

    return categorized_pixel_list


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
    node_titles = {node: f'{node[2]}' for node in G.nodes()}

    # Draw the graph
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', labels=node_titles, node_size=1000, font_size=7, font_color='black', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # Show the plot
    plt.show()