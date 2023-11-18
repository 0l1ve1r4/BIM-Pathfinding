from bmp_matrix import *
from get_data_from_image import *

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


if __name__ == "__main__":

    image_path = "images/output.bmp"
    matrix_to_bmp(matrix, image_path)
    graph_list = rgb_image_to_list(image_path)
    print(graph_list)