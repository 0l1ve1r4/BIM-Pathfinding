import tkinter as tk

import tkinter as tk
from tkinter import Label, Button

class HelpGUI:
    def __init__(self, root, text, title, animation_speed=20, auto_destroy=False, waiting_time=0):
        self.root = root
        self.root.title(title)
        self.animation_speed = animation_speed
        self.explanation_text = text

        self.explanation_label = Label(root, text="", justify=tk.LEFT, padx=20, pady=20)
        self.explanation_label.pack()

        Button(root, text="Close", command=root.destroy, padx=10, pady=5).pack()

        # Start the animation
        self.animate_text()

        if auto_destroy:
            self.root.after(waiting_time, root.destroy)

    def animate_text(self):
        self.index = 0
        self.root.after(0, self.add_next_character)

    def add_next_character(self):
        if self.index < len(self.explanation_text):
            current_text = self.explanation_label.cget("text")
            current_text += self.explanation_text[self.index]
            self.explanation_label.config(text=current_text)
            self.index += 1
            self.root.after(self.animation_speed, self.add_next_character)

def open_explanation_window():
    root = tk.Tk()
    title = "Help"

    explanation_text = (
        "This program demonstrates a graphical user interface for managing a grid of squares.\n"
        "Interaction with the grid is as follows:\n\n"
        " - Left click on a square to change its color.\n"
        " - Right click on a square to delete it.\n"
        " - Click 'Run Dijkstra' to find the shortest path between the start and end nodes.\n"
        " - Click 'Clear Bitmap' to delete all squares.\n"
        " - Click 'Upload Image' to input an image and convert it to a matrix.\n"
        " - Click 'Toggle Gradient' to switch gradient mode where the path is colored based on the weight of the edges sided by black.\n"
        " - Click 'How to use' to open a window with additional information about the program.\n"
        " - Click 'Add new Floor' to add a new floor with its own matrix.\n\n"
        "\n\n Source code: [GitHub](https://github.com/iyksh/BIM-Pathfinding)"
    )

    HelpGUI(root, explanation_text, title)
    root.mainloop()


def new_floor_warning():
    root = tk.Tk()
    title = "Warning"
    explanation_text = (
    "Adding a new floor and drawing may occurs bugs due to the grids managment.\n\n"
    "Some function will be disable when you have more than one floor.\n\n"
    "** 3D STILL WORKS WITH MULTIPLE FLOORS. **\n\n"
    "If you want to use these extra functions, please delete the other floors.\n\n"
    )   
    app = HelpGUI(root, explanation_text, title, animation_speed=0)
    root.mainloop()

def warning_window(waiting_time = 5000):
    root = tk.Tk()
    title = "Warning"
    text = ("This program runs with threads, cafeul with the number of threads you use.\n\n"
            "This can be ajusted in the graph.py file.\n\n"
            )
    
    app = HelpGUI(root, text, title, animation_speed=0, auto_destroy=True, waiting_time=waiting_time)
    root.mainloop()