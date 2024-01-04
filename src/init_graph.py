from graph import *
from PIL import Image
import matplotlib.pyplot as plt

class Bitmap:

    def __init__(self) -> None:
        self.color_mapping = {
            0: (255, 255, 255),  # Branco
            1: (0, 0, 0),  # Preto
            2: (255, 0, 0),  # Vermelho
            3: (0, 255, 0),  # Verde
            4: (128, 128, 128),  # Cinza
        }

    def matrix_to_bmp(self, matrix: list, image_path: str) -> None:
        img = Image.new('RGB', (len(matrix[0]), len(matrix)))
        for y in range(img.height):
            for x in range(img.width):
                img.putpixel((x, y), self.color_mapping[matrix[y][x]])
        img.save(image_path)

    def rgb_image_to_list(self, image_path: str) -> list:
        img = Image.open(image_path)
        width, height = img.size
        categorized_pixel_list = []

        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))

                if (r, g, b) == (255, 255, 255):
                    color = "white"
                elif (r, g, b) == (0, 255, 0):
                    color = "green"
                elif (r, g, b) == (0, 0, 0):
                    color = "black"
                elif (r, g, b) == (255, 0, 0):
                    color = "red"
                elif (r, g, b) == (128, 128, 128):
                    color = "gray"
                else:
                    color = "unknown"
                    print(f"Error: Unknown color: {r}, {g}, {b}")

                categorized_pixel_list.append((x, y, color))

        return categorized_pixel_list


    #                                         #
    #                                         #
    #                                         #
    #           class InitGraph               #
    #                                         #
    #                                         #
    #                                         #

class InitGraph:

    def __init__(self) -> None:
        self.graph = Graph()
        self.image_path = "images/matrix.bmp"

    def get_shortest_path(self, matrix):
        bitmap = Bitmap()
        bitmap.matrix_to_bmp(matrix, self.image_path)
        graph_list = bitmap.rgb_image_to_list(self.image_path)
        self.graph.adj.clear()
        self.graph.add_bpm(graph_list)
        
        return (self.graph.find_short_path_bpm(matrix))

    def return_matrix_of_image(self, image_path):
        bitmap = Bitmap()
        graph_list = bitmap.rgb_image_to_list(image_path)
        return self.tuples_to_matrix(graph_list)

    def tuples_to_matrix(self, dataset):
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

        return matrix
