import tkinter as tk
from Init_Graph import *
import os 

class MatrixGUI:
    def __init__(self, root, new_matrix=None):
        self.root = root
        self.root.title("2D - Building Information Modeling")
        self.e = Init_Graph()

        if new_matrix is None:
            self.matrix = [
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 0: white square
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],  # 1: black square,
                [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],  # 2: red square
                [1, 1, 1, 9, 0, 1, 0, 0, 1, 0, 0, 0],  # 3: green square
                [0, 0, 0, 9, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0]
                ]
        else:
            self.matrix = new_matrix

        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

        self.row_colors = [tk.StringVar(value="white") for _ in range(self.rows)]

        self.canvas = tk.Canvas(root, width=30 * self.cols, height=30 * self.rows, bg="#f0f0f0", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=self.cols, padx=10, pady=10)

        self.draw_matrix()

        self.canvas.bind("<Button-1>", self.update_square_color)

        get_matrix_button = tk.Button(self.root, text="Get Matrix", command=self.get_matrix, bg="#4caf50", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        get_matrix_button.grid(row=self.rows + 1, column=self.cols + 1, padx=10, pady=10)

        del_path_button = tk.Button(self.root, text="Delete Path", command=self.del_path, bg="#f44336", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        del_path_button.grid(row=self.rows + 2, column=self.cols + 1, padx=10, pady=10)

        text = tk.Label(self.root, text="Red: Start\nGreen: End\n", font=("Helvetica", 12), padx=10, pady=10)
        text.grid(row=self.rows + 3, column=self.cols + 1)
        
    def update_row_color(self, row_index):
        new_color = self.row_colors[row_index].get()
        try:
            color_index = ["white", "black", "red", "green"].index(new_color)
            for j in range(self.cols):
                self.matrix[row_index][j] = color_index
            self.draw_matrix()
        except ValueError:
            print(f"Invalid color: {new_color}")

    def update_square_color(self, event):
        x, y = event.x, event.y
        col_index = x // 30
        row_index = y // 30

        if 0 <= row_index < self.rows and 0 <= col_index < self.cols:
            current_color = self.matrix[row_index][col_index]
            new_color = (current_color + 1) % len(["white", "black", "red", "green"])
            self.matrix[row_index][col_index] = new_color
            self.draw_matrix()

    def draw_matrix(self):
        self.canvas.delete("all")
        colors = ["white", "black", "red", "green"]

        for i in range(self.rows):
            for j in range(self.cols):
                x0, y0 = j * 30, i * 30
                x1, y1 = x0 + 30, y0 + 30
                color_index = self.matrix[i][j]

                try:
                    color = colors[color_index]
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                except IndexError:
                    color = colors[0]
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                    
                    
    def del_path(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 3 or self.matrix[i][j] == 2:
                    self.matrix[i][j] = 0

        self.draw_matrix()

    def get_matrix(self): # This is the function that calls the Init_Graph.py and will use graphs to find the shortest path
        self.matrix = self.e.return_matrix(self.matrix)
        self.draw_matrix()

if __name__ == "__main__":
    try:
        print("\033[H\033[J")
        root = tk.Tk()
        app = MatrixGUI(root)
        root.mainloop()
        
    except Exception as e:
        os.system("pip install tk")
        root = tk.Tk()
        app = MatrixGUI(root)
        root.mainloop()

        