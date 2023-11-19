from bmp_matrix import *
from graph import *

class Init_Graph:
    
    def __init__(self) -> None:

        self.g = Graph()
        self.image_path = "images/matrix.bmp"
        self.final_image_path = "images/output.bmp"
            
    def return_matrix(self, matrix):
            
        matrix_to_bmp(matrix, self.image_path) # optional, u can use a image and converts to a matrix or list of lists, like the function under  
        graph_list = (rgb_image_to_list(self.image_path))
        self.g.add_bpm(graph_list)    
        matrix_to_bmp(self.g.find_short_path_bpm(matrix), self.final_image_path)
        matrix = self.g.find_short_path_bpm(matrix)
        return matrix
    