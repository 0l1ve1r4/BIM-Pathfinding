from PIL import Image
import matplotlib.pyplot as plt

def rgb_image_to_list(image_path: str) -> list:
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
            else:
                color = "unknown"

            categorized_pixel_list.append((x, y, color))

    return categorized_pixel_list




