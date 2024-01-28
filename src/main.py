# ==============================================================================
#                       Main file to run the GUI.
# 
#                       If you want to change the default image,
#                       check the .json.
# 
#                       But also, you can open a image from your computer,
#                       just click in "New Image" button on the GUI.
# ==============================================================================

from mainGUI import *
from utils import *

import os
import json

if __name__ == "__main__":
    print("\033[H\033[J")
    
    run_path = os.getcwd()
    config_file = "src/config.json"
    
    if not run_path.split("\\")[-1].startswith("BIM-"): 
        debug("Run the aplication on the ./BIM-Pathfinding folder", "error")
        exit(1)
    
    if config_file == None:
        debug("No json file", "error")
        exit(1)
    else:
        with open(config_file, 'r') as f:
            config_data = json.load(f)

    root = tk.Tk()
    app = MatrixGUI(root, config_data["config"]["default_matrix_path"])
    root.mainloop()