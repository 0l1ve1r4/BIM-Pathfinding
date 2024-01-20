from bmp_matrix import *
from graph import *

#
#
# This class is responsible for intermedite the GUI, 
# the graph and the bitmaps functions
# 
#

class Init_Graph:
    
    def __init__(self) -> None: 
        
        #   Constructor
        #   Initialize the graph and the image paths
        #
        self.graph = Graph()
        self.image_path = "images/matrix.bmp"
        self.final_image_path = "images/output.bmp"
            
    def return_matrix(self, matrix:list, gradient:bool) -> list:
        """Given a matrix, find the shortest path in the Graph class."""
            
        matrix_to_bmp(matrix, self.image_path, gradient) # optional, u can use a image and converts to a matrix or list of lists, like the function under  
        graph_list = (rgb_image_to_list(self.image_path)) # graph_list is a list of tuples (x,y,color)
        
        #clear the graph nodes and edges
        self.graph.adj.clear()
        
        #add the nodes and edges from the graph_list
        self.graph.add_nodes_and_edges_from_list(graph_list)    
        matrix = self.graph.find_short_path_bpm(matrix)
        matrix_to_bmp(matrix, self.final_image_path, gradient)
        return matrix
    
    def return_matrix_of_image(self, image_path:str) -> list:
        """Given a image path, convert it to  tuples (x,y,color) and then to a matrix List[List[int]]"""
            
        graph_list = (rgb_image_to_list(image_path))
        
        return tuples_to_matrix(graph_list)
    

    def add_floor(self, matrix:list) -> list:
        """Given a matrix, add a floor to it"""
        print("Test")


def tuples_to_matrix(dataset):
    """Given a list of tuples (x,y,color) convert it to a matrix List[List[int]]"""
    nodes = set()
    for node_tuple in dataset:
        nodes.add(node_tuple[:2])

    max_x = max(node[0] for node in nodes)
    max_y = max(node[1] for node in nodes)
    
    matrix = [[0] * (max_x + 1) for _ in range(max_y + 1)]

    for x, y, color in dataset:
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

