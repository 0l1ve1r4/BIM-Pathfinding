from bmp_matrix import *
from get_data_from_image import *
from graph import *

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
                    g.add_undirected_edge(graph_list[i], graph_list[j], 1)

    #print(g.adj)  # Replace with the node you want to check