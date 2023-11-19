from bmp_matrix import *
from graph import *
import networkx as nx

# Matriz de entrada
matrix = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #0-> branco, 
        [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0], #1-> preto,  
        [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], #2-> vermelho,
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], #3 -> verde
        [0, 0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0]
    ]

if __name__ == "__main__":

    g = Graph()
    image_path = "images/output.bmp"
    final_image_path = "images/final_output.bmp"
    matrix_to_bmp(matrix, image_path)
    
    graph_list = (rgb_image_to_list(image_path))
    g.add_bpm(graph_list)
    
 
    
    start_node = g.start
    end_node = g.end
    
    
    
    print(start_node)
    print(end_node)
    
    #print(g.adj)
    #draw_oriented_graph(g.adj)

    shortest_path = g.dijkstra(start_node, end_node)
    print(shortest_path)

    
    for i in range(len(shortest_path)):
        x = shortest_path[i][0]
        y = shortest_path[i][1]
        if shortest_path[i][2] != 'red' and shortest_path[i][2] != 'green':
            matrix[y][x] = 9
            
        
    matrix_to_bmp(matrix, final_image_path)