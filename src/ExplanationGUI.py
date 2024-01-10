import tkinter as tk
from tkinter import messagebox

class ExplanationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Functions Explanation")

        self.explanation_text = (
            "This program demonstrates a graphical user interface for managing a grid of squares.\n"
            "Interaction with the grid is as follows:\n\n"
            " - Left click on a square to change its color.\n"
            " - Right click on a square to delete it.\n"
            " - Click 'Get Path' to find the shortest path between the start and end nodes.\n"
            " - Click 'Clear Matrix' to delete gray and yellow squares.\n"
            " - Click 'Input Image' to input an image and convert it to a matrix.\n"
            " - Click 'Gradient' to toggle gradient mode where the path is colored based on the weight of the edges sided by black \n"
        )

        self.explanation_label = tk.Label(root, text="", justify=tk.LEFT, padx=20, pady=20)
        self.explanation_label.pack()

        tk.Button(root, text="Close", command=root.destroy, padx=10, pady=5).pack()

        # Start the animation
        self.animate_text()

    def animate_text(self):
        self.index = 0
        self.root.after(50, self.add_next_character)

    def add_next_character(self):
        if self.index < len(self.explanation_text):
            current_text = self.explanation_label.cget("text")
            current_text += self.explanation_text[self.index]
            self.explanation_label.config(text=current_text)
            self.index += 1
            self.root.after(10, self.add_next_character)

def open_explanation_window():
    root = tk.Tk()
    app = ExplanationGUI(root)
    root.mainloop()

