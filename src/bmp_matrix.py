from PIL import Image

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


def rgb_image_to_list(image_path: str) -> list[tuple[int, int, str]]:
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
            elif r == 255 and g == 0 and b == 0:    
                color = "red"
            elif r == 128 and g == 128 and b == 128:
                color = "darkgray"
            elif r == 196 and g == 196 and b == 196:
                color = "lightgray"
            elif r == 255 and g == 255 and b == 0:
                color = "yellow"
            else:
                color = "unknown"

            categorized_pixel_list.append((x, y, color))

    return categorized_pixel_list

