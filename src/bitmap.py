from PIL import Image
from graph import *

#
#
# This class is responsible for intermedite the GUI, 
# the graph and the bitmaps functions
# 
#

class Bitmap:
    
    def __init__(self) -> None: 
        
        #   Constructor
        #   Initialize the graph and the image paths
        #
        self.graph = Graph()
            
    def return_matrix(self, matrix_list:list, gradient:bool) -> list:
        """Given a matrix, find the shortest path in the Graph class."""
        
        graph_list = [] # list of tuples (x,y,z,color) of each floor
        graph_list_ordered = [] # list of tuples (x,y,z,color) of each floor ordered by z
        self.graph.adj.clear() #clear the graph nodes and edges

        for z in range(len(matrix_list)): # put each floor in a bmp image and then convert it to a list of tuples (x,y,z,color)
            image_path = (f"images/matrix_{z}.bmp")
            matrix_to_bmp(matrix_list[z], image_path, gradient)
            graph_list.extend((rgb_image_to_list(image_path, z))) 
            graph_list_ordered.append((rgb_image_to_list(image_path, z)))
            
        #add the nodes and edges of this floor to the graph
        self.graph.add_nodes_and_edges_from_list(graph_list)    

        # add edges between floors
        self.graph.add_edges_between_floors()
        
        path = self.graph.find_short_path_bpm() # find the shortest path in the Graph class.
        
        print("[Debug]: Path found: {}".format(len(path)))
        matrix_list = [] # clear the matrix list
        
        for i in range(len(graph_list_ordered)): # for each floor
            for j in range(len(graph_list_ordered[i])):
                if graph_list_ordered[i][j] in path:
                    graph_list_ordered[i][j] = (graph_list_ordered[i][j][0], graph_list_ordered[i][j][1], graph_list_ordered[i][j][2], "yellow")
            
        for i in range(len(graph_list_ordered)):
            matrix = tuples_to_matrix(graph_list_ordered[i]) # convert the list of tuples (x,y,z,color) to a matrix
            matrix_list.append(matrix) # add the matrix to the matrix list

        return matrix_list  # return the matrix list
    
    def return_matrix_of_image(self, image_path:str) -> list:
        """Given a image path, convert it to  tuples (x,y,color) and then to a matrix List[List[int]]"""
            
        graph_list = (rgb_image_to_list(image_path, 0))
        
        return tuples_to_matrix(graph_list)
    

    def add_floor(self, matrix:list) -> list:
        """Given a matrix, add a floor to it"""
        print("Test")


def tuples_to_matrix(dataset):
    """Given a list of tuples (x,y,z,color) convert it to a matrix List[List[int]]"""
    nodes = set()
    for node_tuple in dataset:
        nodes.add(node_tuple[:2])

    max_x = max(node[0] for node in nodes)
    max_y = max(node[1] for node in nodes)
    
    matrix = [[0] * (max_x + 1) for _ in range(max_y + 1)]

    for x, y, z, color in dataset:
        if color == 'white':
            matrix[y][x] = 0
        elif color == 'black':
            matrix[y][x] = 1
        elif color == 'red':
            matrix[y][x] = 2
        elif color == 'green':
            matrix[y][x] = 3
        elif color == 'darkgray':
            matrix[y][x] = 4
        elif color == 'lightgray':
            matrix[y][x] = 5
        elif color == 'yellow':
            matrix[y][x] = 6

    return matrix




#
# Some useful functions
# to convert a matrix to a bmp image and vice versa
#
#
#

def matrix_to_bmp(matrix: list, image_path: str, gradient) -> None:
    """Save a matrix as a bmp image"""

    if gradient:

        def get_neighbors(x, y):
            neighbors = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < len(matrix) and 0 <= y + j < len(matrix[0]) and (i != 0 or j != 0):
                        neighbors.append(matrix[x + i][y + j])
            return neighbors

        def adjust_color(x, y):
            current_color = matrix[x][y]
            neighbor_colors = get_neighbors(x, y)

            if current_color == 0:  # White
                if 1 in neighbor_colors:  # Sided by black
                    matrix[x][y] = 4  # Dark grey
                elif 4 in neighbor_colors:  # Sided by darkgrey
                    matrix[x][y] = 5  # Lightgrey

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                adjust_color(i, j)

    color_mapping = {
        0: (255, 255, 255),  # White
        1: (0, 0, 0),        # Black
        2: (255, 0, 0),      # Red
        3: (0, 255, 0),      # Green
        4: (128, 128, 128),  # Dark grey
        5: (196, 196, 196),  # Light grey
        6: (255, 255, 0)     # Yellow
    }
            
    img = Image.new('RGB', (len(matrix[0]), len(matrix)))
    for y in range(img.height):
        for x in range(img.width):
            img.putpixel((x, y), color_mapping[matrix[y][x]])

    img.save(image_path)


def rgb_image_to_list(image_path: str, z: int) -> list[tuple[int, int, str]]:
    """
    Recieved a bpm image, convert its to a categorized list of tuples (x,y,color)
    """
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
            elif r == 255 and g == 0 and b == 0 or r == 237 and g == 28 and b == 36: # Isso aqui foi uma sacanagem hein   
                color = "red"
            elif r == 128 and g == 128 and b == 128:
                color = "darkgray"
            elif r == 196 and g == 196 and b == 196:
                color = "lightgray"
            elif r == 255 and g == 255 and b == 0:
                color = "yellow"
            else:
                color = "unknown"

            categorized_pixel_list.append((x, y, z, color))

    return categorized_pixel_list

