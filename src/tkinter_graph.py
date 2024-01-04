import tkinter as tk
from tkinter import filedialog, messagebox
from init_graph import InitGraph

class Interface:

    def __init__(self, root, square_size=50, default_matrix_len=10):
        self.SQUARE_SIZE = square_size

        self.root = root
        self.root.title("2D - Building Information Modeling")
        self.bitmap = InitGraph()

        self.matrix = [[0] * default_matrix_len for _ in range(10)]
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

        self.row_colors = [tk.StringVar(value="white") for _ in range(self.rows)]

        self.canvas = tk.Canvas(root, width=self.SQUARE_SIZE * self.cols, height=self.SQUARE_SIZE * self.rows,
                                bg="#f0f0f0", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=self.cols, padx=10, pady=10)

        self.draw_matrix()

        self.canvas.bind("<Button-1>", self.update_square_color) # Left click
        self.canvas.bind("<Button-3>", self.delete_square) # Right click

        get_matrix_button = tk.Button(self.root, text="Get Path", command=self.get_matrix, bg="#4caf50", fg="white",
                                      font=("Helvetica", 12), padx=10, pady=5)
        get_matrix_button.grid(row=self.rows + 1, column=self.cols + 1, padx=10, pady=10)

        input_image_button = tk.Button(self.root, text="Input Image", command=self.open_file_explorer, bg="#4caf50",
                                       fg="white", font=("Helvetica", 12), padx=10, pady=5)
        input_image_button.grid(row=self.rows + 1, column=self.cols + 2, padx=10, pady=10)

        del_path_button = tk.Button(self.root, text="Delete Path", command=self.del_path, bg="#f44336", fg="white",
                                    font=("Helvetica", 12), padx=10, pady=5)
        del_path_button.grid(row=self.rows + 2, column=self.cols + 1, padx=10, pady=10)



    #                                         #
    #                                         #
    #                                         #
    #           TkWindow Functions            #
    #                                         #
    #                                         #
    #                                         #





    def update_row_color(self, row_index):
        new_color = self.row_colors[row_index].get()
        colors = ["white", "black", "red", "green"]
        try:
            color_index = colors.index(new_color)
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



    #                                         #
    #                                         #
    #                                         #
    #           Buttons Functions             #
    #                                         #
    #                                         #
    #                                         #


    def open_file_explorer(self):
        file_path = filedialog.askopenfilename()
        self.matrix = self.bitmap.return_matrix_of_image(file_path)
        self.draw_matrix()
        return file_path

    def del_path(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 3 or self.matrix[i][j] == 2:
                    self.matrix[i][j] = 0

        self.draw_matrix()

    def get_matrix(self):
        self.matrix = self.bitmap.get_shortest_path(self.matrix)
        self.draw_matrix()

        