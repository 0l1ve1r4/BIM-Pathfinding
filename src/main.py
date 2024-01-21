# ==============================================================================
# Main file to run the GUI.
# 
# If you want to change the default image,
# change the matrix_path variable below.
# 
# But also, you can open a image from your computer,
# just click in "Input Image" button on the GUI.
# ==============================================================================


from mainGUI import *
from utils import *
import os

if __name__ == "__main__":
    
    print("\033[H\033[J")
    debug("Running on {}".format(os.system('pwd')), "debug")
    matrix_path = "./Datasets/toyFloors/toy_0.bmp" # default image

    root = tk.Tk()
    app = MatrixGUI(root, matrix_path)
    root.mainloop()