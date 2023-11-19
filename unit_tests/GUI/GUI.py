import tkinter as tk

class MatrixGUI:
    def __init__(self, root, matrix):
        self.root = root
        self.root.title("2D - Building Information Modeling")

        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.row_colors = [tk.StringVar(value="white") for _ in range(self.rows)]

        self.canvas = tk.Canvas(root, width=30*self.cols, height=30*self.rows)
        self.canvas.grid(row=0, column=0, columnspan=self.cols)

        self.create_color_widgets()
        self.draw_matrix()

        # Bind the canvas click event to the update_square_color function
        self.canvas.bind("<Button-1>", self.update_square_color)
        
        # Add a "Get Matrix" button
        get_matrix_button = tk.Button(self.root, text="Get Path", command=self.get_matrix)
        get_matrix_button.grid(row=self.rows + 1, column=self.cols + 1, padx=5, pady=5)

    def create_color_widgets(self):
        for i in range(self.rows):
            label = tk.Label(self.root, text=f"Row {i + 1} Color:")
            label.grid(row=i + 1, column=self.cols, padx=5, pady=5)

            color_entry = tk.Entry(self.root, textvariable=self.row_colors[i])
            color_entry.grid(row=i + 1, column=self.cols + 1, padx=5, pady=5)

            update_button = tk.Button(self.root, text="Update", command=lambda i=i: self.update_row_color(i))
            update_button.grid(row=i + 1, column=self.cols + 2, padx=5, pady=5)

    def update_row_color(self, row_index):
        new_color = self.row_colors[row_index].get()
        try:
            color_index = ["white", "black", "red", "green", "blue"].index(new_color)
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
            new_color = (current_color + 1) % len(self.row_colors)
            self.matrix[row_index][col_index] = new_color
            self.draw_matrix()

    def draw_matrix(self):
        self.canvas.delete("all")
        colors = ["white", "black", "red", "green", "blue"]

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

    def get_matrix(self):
        print("Current Matrix:")
        for row in self.matrix:
            print(row)
    
if __name__ == "__main__":
    matrix = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0]
    ]

    root = tk.Tk()
    app = MatrixGUI(root, matrix)
    root.mainloop()
