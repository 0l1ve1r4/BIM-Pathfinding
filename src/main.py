from bmp_matrix import *
from graph import *

# imagem respectiva em ./docs/trabalho.pdf
matrix = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #0-> branco, 
        [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0], #1-> preto,  
        [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], #2-> vermelho,
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], #3 -> verde
        [0, 0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0]  #9 -> azul
    ]

if __name__ == "__main__":

    g = Graph()
    image_path = "images/matrix.bmp"
    final_image_path = "images/output.bmp"
    
    matrix_to_bmp(matrix, image_path) # optional, u can use a image and converts to a matrix or list of lists, like the function under
    
    graph_list = (rgb_image_to_list(image_path))
    g.add_bpm(graph_list)    
    matrix_to_bmp(g.find_short_path_bpm(matrix), final_image_path)
    