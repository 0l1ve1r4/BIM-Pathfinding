import tkinter as tk
from tkinter import filedialog, messagebox
from Init_Graph import *
from ExplanationGUI import *

# This class is responsible for the GUI of the program.
# The main GUI is a grid of squares, each square representing a node in the graph.
#  - Left click on a square to change its color
#  - Right click on a square to delete it
#  - Click "Get Path" to find the shortest path between the start and end nodes
#  - Click "Delete Path" to delete the shortest path
#  - Click "Input Image" to input a image and convert it to a matrix
#  - Click "Gradient" to toggle gradient mode where the path is colored based on the weight of the edges (white -> black -> dark gray -> light gray -> yellow)
#  
#  - The colors are:
#    - [0] White: Empty square 
#    - [1] Black: Wall 
#    - [2] Red: Start node 
#    - [3] Green: End node(s) 
#    - [4] darkgray: Bad path (weight = 2))
#    - [5] light_gray: Good path (weight = 1.5)
#    - [6] Yellow: Shortest path output (weight = 1) 
#
#

class MatrixGUI:
    

    def __init__(self, root, matrix=None, SQUARE_SIZE = 10):
        self.SQUARE_SIZE = SQUARE_SIZE
        self.root = root
        self.root.title("2D - Building Information Modeling")
        self.colors = ["white", "black", "red", "green", "darkgray", "lightgray" , "yellow"]

        self.intermediate_class = Init_Graph()

        self.matrix = self.intermediate_class.return_matrix_of_image(matrix) if matrix else [[0] * 10 for _ in range(10)]

        self.rows, self.cols = len(self.matrix), len(self.matrix[0])

        self.row_colors = [tk.StringVar(value="white") for _ in range(self.rows)]

        self.canvas = tk.Canvas(root, width=self.SQUARE_SIZE * self.cols, height=self.SQUARE_SIZE * self.rows, bg="#f0f0f0", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=self.cols, padx=10, pady=10)

        self.draw_matrix()

        self.canvas.bind("<Button-1>", self.update_square_color)
        self.canvas.bind("<Button-3>", self.delete_square)
        self.gradient = True


        tk.Button(self.root, text="Get Path", command=self.get_matrix, bg="#4caf50", fg="white", font=("Helvetica", 12), padx=10, pady=5).grid(row=self.rows + 1, column=self.cols + 1, padx=10, pady=10)
        tk.Button(self.root, text="Input Image", command=self.open_file_explorer, bg="#4caf50", fg="white", font=("Helvetica", 12), padx=10, pady=5).grid(row=self.rows + 1, column=self.cols + 2, padx=10, pady=10)
        tk.Button(self.root, text="Clear Matrix", command=self.del_path, bg="#f44336", fg="white", font=("Helvetica", 12), padx=10, pady=5).grid(row=self.rows + 2, column=self.cols + 1, padx=10, pady=10)
        self.gradient_button = tk.Button(self.root,text="Gradient ON",command=self.toggle_gradient,bg="#4caf50" if self.gradient else "#f44336",fg="white",font=("Helvetica", 12),padx=10,pady=5)
        self.gradient_button.grid(row=self.rows + 2, column=self.cols + 2, padx=10, pady=10)


    def toggle_gradient(self):
        self.gradient = not self.gradient
        print(f'Gradient toggled: {self.gradient}')
        self.gradient_button.config(bg="#4caf50" if self.gradient else "#f44336")
        self.gradient_button.config(text="Gradient ON" if self.gradient else "Gradient OFF")


    def open_file_explorer(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.root.destroy()  # Close the current window
            root = tk.Tk()
            app = MatrixGUI(root, self.intermediate_class.return_matrix_of_image(file_path))
            root.mainloop()
        return file_path

    def update_row_color(self, row_index):
        new_color = self.row_colors[row_index].get()
        try:
            color_index = self.colors[:-1].index(new_color)
            self.matrix[row_index] = [color_index] * self.cols
            self.draw_matrix(update_speed=0)
        except ValueError:
            messagebox.showerror("Invalid Color", f"Invalid color: {new_color}")

    def update_square_color(self, event):
        x, y = event.x, event.y
        col_index, row_index = x // self.SQUARE_SIZE, y // self.SQUARE_SIZE

        if 0 <= row_index < self.rows and 0 <= col_index < self.cols:
            current_color = self.matrix[row_index][col_index]
            new_color = (current_color + 1) % len(self.colors[:-1])
            self.matrix[row_index][col_index] = new_color
            self.draw_matrix(update_speed=0)

    def delete_square(self, event):
        x, y = event.x, event.y
        col_index, row_index = x // self.SQUARE_SIZE, y // self.SQUARE_SIZE

        if 0 <= row_index < self.rows and 0 <= col_index < self.cols:
            self.matrix[row_index][col_index] = 0
            self.draw_matrix(update_speed=0)

    def draw_matrix(self, index=(0, 0), update_speed=5):
        colors = self.colors
        i, j = index


        if 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[i]):
            x0, y0 = j * self.SQUARE_SIZE, i * self.SQUARE_SIZE
            x1, y1 = x0 + self.SQUARE_SIZE, y0 + self.SQUARE_SIZE
            color_index = self.matrix[i][j]

            try:
                color = colors[color_index]
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            except IndexError:
                color = colors[0]
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

            if j + 1 < self.cols:
                self.root.after(update_speed, lambda: self.draw_matrix((i, j + 1), update_speed))
            elif i + 1 < self.rows:
                self.root.after(update_speed, lambda: self.draw_matrix((i + 1, 0), update_speed))
            else:
                # Adjust canvas size after drawing completes
                self.canvas.config(width=self.SQUARE_SIZE * self.cols, height=self.SQUARE_SIZE * self.rows)
                self.root.update_idletasks()  # Update the Tkinter event loop
                self.root.grid_rowconfigure(0, weight=1)
                self.root.grid_columnconfigure(0, weight=1)

    def del_path(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] >= 4:
                    self.matrix[i][j] = 0

        self.draw_matrix(update_speed=1)

    def get_matrix(self):
        self.matrix = self.intermediate_class.return_matrix(self.matrix, self.gradient)
        self.draw_matrix(update_speed=10)

