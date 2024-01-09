import tkinter as tk
from tkinter import messagebox

class ExplanationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Function Explanation")

        explanation_text = (
            "This program demonstrates a graphical user interface for managing a grid of squares.\n"
            "Interaction with the grid is as follows:\n\n"
            " - Left click on a square to change its color.\n"
            " - Right click on a square to delete it.\n"
            " - Click 'Get Path' to find the shortest path between the start and end nodes.\n"
            " - Click 'Delete Path' to delete the shortest path.\n"
            " - Click 'Input Image' to input an image and convert it to a matrix.\n"
            " - Click 'Gradient' to toggle gradient mode where the path is colored based on the weight of the edges sided by black \n"
        )

        explanation_label = tk.Label(root, text=explanation_text, justify=tk.LEFT, padx=20, pady=20)
        explanation_label.pack()

        tk.Button(root, text="Close", command=root.destroy, padx=10, pady=5).pack()

def open_explanation_window():
    root = tk.Tk()
    app = ExplanationGUI(root)
    root.mainloop()


