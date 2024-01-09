from bmp_matrix import *
from graph import *

class Init_Graph:
    
    def __init__(self) -> None:

        self.g = Graph()
        self.image_path = "images/matrix.bmp"
        self.final_image_path = "images/output.bmp"
            
    def return_matrix(self, matrix, gradient):
            
        matrix_to_bmp(matrix, self.image_path, gradient) # optional, u can use a image and converts to a matrix or list of lists, like the function under  
        graph_list = (rgb_image_to_list(self.image_path))
        self.g.adj.clear()
        self.g.add_nodes_and_edges_from_list(graph_list)    
        matrix = self.g.find_short_path_bpm(matrix)
        matrix_to_bmp(matrix, self.final_image_path, gradient)
        return matrix
    
    def return_matrix_of_image(self, image_path):
            
        graph_list = (rgb_image_to_list(image_path))
        
        return tuples_to_matrix(graph_list)


def tuples_to_matrix(dataset):
    nodes = set()
    for node_tuple in dataset:
        nodes.add(node_tuple[:2])

    max_x = max(node[0] for node in nodes)
    max_y = max(node[1] for node in nodes)
    matrix = [[0] * (max_y + 1) for _ in range(max_x + 1)]

    for x, y, color in dataset:
        if color == 'white':
            matrix[x][y] = 0
        elif color == 'black':
            matrix[x][y] = 1
        elif color == 'red':
            matrix[x][y] = 2
        elif color == 'green':
            matrix[x][y] = 3
        elif color == 'gray':
            matrix[x][y] = 4
        elif color == 'yellow':
            matrix[x][y] = 5

    return matrix
