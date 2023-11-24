import tkinter as tk
from tkinter import filedialog, messagebox
from Init_Graph import *
import os
import subprocess

class MatrixGUI:
    SQUARE_SIZE = 50

    def __init__(self, root, new_matrix=None):
        self.root = root
        self.root.title("2D - Building Information Modeling")
        self.e = Init_Graph()

        try:
            import tkinter
        except ModuleNotFoundError:
            subprocess.run(["pip", "install", "tkinter"])

        if new_matrix is None:
            self.matrix = [
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 0: white square
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1: black square,
                [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],  # 2: red square
                [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],  # 3: green square
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0]
                ]
        else:
            self.matrix = new_matrix

        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

        self.row_colors = [tk.StringVar(value="white") for _ in range(self.rows)]

        self.canvas = tk.Canvas(root, width=self.SQUARE_SIZE * self.cols, height=self.SQUARE_SIZE * self.rows, bg="#f0f0f0", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=self.cols, padx=10, pady=10)

        self.draw_matrix()

        self.canvas.bind("<Button-1>", self.update_square_color)
        self.canvas.bind("<Button-3>", self.delete_square)

        get_matrix_button = tk.Button(self.root, text="Get Path", command=self.get_matrix, bg="#4caf50", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        get_matrix_button.grid(row=self.rows + 1, column=self.cols + 1, padx=10, pady=10)
        
        input_image_button = tk.Button(self.root, text="Input Image", command=self.open_file_explorer, bg="#4caf50", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        input_image_button.grid(row=self.rows + 1, column=self.cols + 2, padx=10, pady=10)

        del_path_button = tk.Button(self.root, text="Delete Path", command=self.del_path, bg="#f44336", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        del_path_button.grid(row=self.rows + 2, column=self.cols + 1, padx=10, pady=10)

    
    def open_file_explorer(self):
        file_path = filedialog.askopenfilename()
        self.matrix = self.e.return_matrix_of_image(file_path)
        self.draw_matrix()
        return file_path

    def update_row_color(self, row_index):
        new_color = self.row_colors[row_index].get()
        try:
            color_index = ["white", "black", "red", "green"].index(new_color)
            for j in range(self.cols):
                self.matrix[row_index][j] = color_index
            self.draw_matrix()
        except ValueError:
            messagebox.showerror("Invalid Color", f"Invalid color: {new_color}")

    def update_square_color(self, event):
        x, y = event.x, event.y
        col_index = x // self.SQUARE_SIZE
        row_index = y // self.SQUARE_SIZE

        if 0 <= row_index < self.rows and 0 <= col_index < self.cols:
            current_color = self.matrix[row_index][col_index]
            new_color = (current_color + 1) % len(["white", "black", "red", "green"])
            self.matrix[row_index][col_index] = new_color
            self.draw_matrix()

    def delete_square(self, event):
        x, y = event.x, event.y
        col_index = x // self.SQUARE_SIZE
        row_index = y // self.SQUARE_SIZE

        if 0 <= row_index < self.rows and 0 <= col_index < self.cols:
            self.matrix[row_index][col_index] = 0
            self.draw_matrix()

    def draw_matrix(self):
        self.canvas.delete("all")
        colors = ["white", "black", "red", "green"]

        for i in range(self.rows):

            if 0 <= i < len(self.matrix):
                for j in range(self.cols):
  
                    if 0 <= j < len(self.matrix[i]):
                        x0, y0 = j * self.SQUARE_SIZE, i * self.SQUARE_SIZE
                        x1, y1 = x0 + self.SQUARE_SIZE, y0 + self.SQUARE_SIZE
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

    def get_matrix(self):
        print("\033[H\033[J")
        for row in self.matrix:
            print(row)
        
        self.draw_matrix()
        self.matrix = self.e.return_matrix(self.matrix)
        self.draw_matrix()

if __name__ == "__main__":
    try:
        print("\033[H\033[J")
        root = tk.Tk()
        app = MatrixGUI(root)
        root.mainloop()
        
    except Exception as e:
        print(f"An error occurred: {e}")