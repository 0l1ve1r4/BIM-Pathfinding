import tkinter as tk
from tkinter import filedialog, messagebox
from Init_Graph import *
from ExplanationGUI import *

class MatrixGUI:
    

    def __init__(self, root, matrix=None, SQUARE_SIZE = 10):
 
        #                           
        # Some useful variables:    
        #                           

        self.SQUARE_SIZE = SQUARE_SIZE                        # The size of each square in the grid
        self.root = root                                      # The root window
        self.root.title("2D - Building Information Modeling") # The title of the root window
        self.colors = ["white", "black", "red", "green", "darkgray", "lightgray" , "yellow"] # The colors of the squares
        self.gradient = True                                  # The gradient mode flag for the dijkstra algorithm weights 

        #
        # Initialize the matrix: 
        #
        self.intermediate_class = Init_Graph()
        self.matrix = self.intermediate_class.return_matrix_of_image(matrix) if matrix else [[0] * 15 for _ in range(10)]
        self.rows, self.cols = len(self.matrix), len(self.matrix[0])
        self.row_colors = [tk.StringVar(value="white") for _ in range(self.rows)]

        self.canvas = tk.Canvas(root, width=self.SQUARE_SIZE * self.cols, height=self.SQUARE_SIZE * self.rows, bg="#f0f0f0", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=self.cols, padx=10, pady=10)

        self.draw_matrix() # Draw the matrix on the canvas with the default update speed

        #
        # Commands:
        #
        self.canvas.bind("<Button-1>", self.update_square_color) # Left click on a square to change its color
        self.canvas.bind("<Button-3>", self.delete_square)       # Right click on a square to delete it

        #
        # TK Buttons:
        #
        tk.Button(self.root, text="Get Path", command=self.get_matrix, bg="#4caf50", fg="white", font=("Helvetica", 12), padx=10, pady=5).grid(row=self.rows + 1, column=self.cols + 1, padx=10, pady=10)
        tk.Button(self.root, text="Input Image", command=self.open_file_explorer, bg="#4caf50", fg="white", font=("Helvetica", 12), padx=10, pady=5).grid(row=self.rows + 1, column=self.cols + 2, padx=10, pady=10)
        tk.Button(self.root, text="Clear Matrix", command=self.del_path, bg="#f44336", fg="white", font=("Helvetica", 12), padx=10, pady=5).grid(row=self.rows + 2, column=self.cols + 1, padx=10, pady=10)
        self.gradient_button = tk.Button(self.root,text="Gradient ON",command=self.toggle_gradient,bg="#4caf50" if self.gradient else "#f44336",fg="white",font=("Helvetica", 12),padx=10,pady=5)
        self.gradient_button.grid(row=self.rows + 2, column=self.cols + 2, padx=10, pady=10)
        tk.Button(self.root, text="Explanation", command=open_explanation_window, bg="#4caf50", fg="white", font=("Helvetica", 12), padx=10, pady=5).grid(row=self.rows + 3, column=self.cols + 1, padx=10, pady=10)
        tk.Button(self.root, text="Add new Floor", command=self.add_new_floor, bg="#4caf50", fg="white", font=("Helvetica", 12), padx=10, pady=5).grid(row=self.rows + 3, column=self.cols + 2, padx=10, pady=10)

    #
    #
    # Some useful functions:
    #
    #

    def add_new_floor(self) -> None:
        """Add a new floor to the Graph"""

        floor_path = self.open_file_explorer(floor=True)
        matrix_floor = self.intermediate_class.return_matrix_of_image(floor_path)
        self.intermediate_class.add_floor(floor_path)
        self.matrix.extend(matrix_floor)

        self.rows, self.cols = len(self.matrix), len(self.matrix[0])
        self.draw_matrix(update_speed=0)

    def toggle_gradient(self) -> None:
        """Change the self.gradient flag and update the gradient button accordingly."""
        self.gradient = not self.gradient
        print(f'Gradient toggled: {self.gradient}')
        self.gradient_button.config(bg="#4caf50" if self.gradient else "#f44336")
        self.gradient_button.config(text="Gradient ON" if self.gradient else "Gradient OFF")


    def open_file_explorer(self, floor = False) -> str:
        """Open a file explorer window to select a image file."""
        file_path = filedialog.askopenfilename()
        print(f'File path: {file_path}')
        if file_path and not floor:
            self.root.destroy()  # Close the current window
            root = tk.Tk()
            app = MatrixGUI(root, file_path, SQUARE_SIZE=self.SQUARE_SIZE)
            root.mainloop()

        return file_path

    def update_row_color(self, row_index:int) -> None:
        """Update the color of a row in the matrix"""
        new_color = self.row_colors[row_index].get()
        try:
            color_index = self.colors[:-1].index(new_color)
            self.matrix[row_index] = [color_index] * self.cols
            self.draw_matrix(update_speed=0)
        except ValueError:
            messagebox.showerror("Invalid Color", f"Invalid color: {new_color}")

    def update_square_color(self, event:tk) -> None:
        """Update the color of a square in the matrix, based on the mouse click event"""
        x, y = event.x, event.y
        col_index, row_index = x // self.SQUARE_SIZE, y // self.SQUARE_SIZE

        if 0 <= row_index < self.rows and 0 <= col_index < self.cols:
            current_color = self.matrix[row_index][col_index]
            new_color = (current_color + 1) % len(self.colors[:-1])
            self.matrix[row_index][col_index] = new_color
            self.draw_matrix(update_speed=0)

    def delete_square(self, event:tk) -> None:
        """Delete a square in the matrix, based on the mouse click event"""
        x, y = event.x, event.y
        col_index, row_index = x // self.SQUARE_SIZE, y // self.SQUARE_SIZE

        if 0 <= row_index < self.rows and 0 <= col_index < self.cols:
            self.matrix[row_index][col_index] = 0
            self.draw_matrix(update_speed=0)

    def draw_matrix(self, index=(0, 0), update_speed=5) -> None:
        """Draw the matrix on the canvas"""
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

    def del_path(self) -> None:
        """Delete the yellow and gray squares in the matrix"""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] >= 4:
                    self.matrix[i][j] = 0

        self.draw_matrix(update_speed=1)

    def get_matrix(self) -> None:
        """Get the shortest path between the start and end nodes"""
        self.matrix = self.intermediate_class.return_matrix(self.matrix, self.gradient)
        self.draw_matrix(update_speed=2)

