from PIL import Image

def matrix_to_bmp(matrix: list, image_path: str) -> None:
    color_mapping = {
        0: (255, 255, 255),  # Branco
        1: (0, 0, 0),  # Preto
        2: (255, 0, 0),  # Vermelho
        3: (0, 255, 0)  # Verde
    }

    img = Image.new('RGB', (len(matrix[0]), len(matrix)))
    for y in range(img.height):
        for x in range(img.width):
            img.putpixel((x, y), color_mapping[matrix[y][x]])

    img.save(image_path)