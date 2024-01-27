# ==============================================================================
# Main Graphical User Interface for the Pathfinding Algorithm
# 
# Default values for the matrix are stored in the config.json file
#
# Author: Guilherme Santos
# ==============================================================================

import tkinter as tk
import json

from tkinter import filedialog, messagebox
from bitmap import *
from utilsGUI import *
from utils import *

class MatrixGUI:

    # ==============================================================================
    # Constructor
    # ==============================================================================

    def __init__(self, root, matrix=None, config_file="./src/config.json"):
        self.root = root


        if config_file != None:
            with open(config_file, 'r') as f:
                config_data = json.load(f)

        self.SQUARE_SIZE = config_data["config"]["SQUARE_SIZE"]
        self.colors = config_data["config"]["colors"]
        self.root.title(config_data["config"]["title"])
        root.iconbitmap(config_data["config"]["icon"])
        self.gradient = config_data["config"]["gradient"]

        self.floor_canvases = []  # Store canvases for each floor
        self.all_matrix = []  # Store all matrixes for each floor

        self.intermediate_class = Bitmap()
        self.matrix = self.intermediate_class.return_matrix_of_image(matrix) if matrix else config_data["matrix"]
        self.all_matrix.append(self.matrix)
        self.rows, self.cols = len(self.matrix), len(self.matrix[0])
        self.row_colors = [tk.StringVar(value="white") for _ in range(self.rows)]
        self.last_col_index = self.cols
        self.collum_update = 0
        self.floor_warnings = 0
        self.config_data = config_data

        self.setup_canvas()
        self.setup_commands()
        
        warning_window()
        

    # ==============================================================================
    # Setups and Commands
    # ==============================================================================

    def setup_canvas(self):
        self.canvas = tk.Canvas(self.root, width=self.SQUARE_SIZE * self.cols, height=self.SQUARE_SIZE * self.rows,
                                bg="#f0f0f0", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=self.cols, padx=10, pady=10)
        self.floor_canvases.append(self.canvas)
        self.draw_matrix()

    def setup_commands(self):
        self.canvas.bind("<Button-1>", self.update_square_color)
        self.canvas.bind("<Button-3>", self.delete_square)

        button_style = {
            "bg": "#f0f0f0",      # background color
            "fg": "black",      # text color
            "font": ("Arial", 12),  # modernized font
            "bd": 0,              # border width
            "highlightthickness": 0,  # no focus border
            "highlightbackground": "#f0f0f0",  # background color on focus
            "activebackground": "#e1e1e1",     # background color on click
            "activeforeground": "#4caf50",    # text color on click
            "padx": 12,
            "pady": 6
        }

        self.get_path_button = tk.Button(self.root, text=self.config_data["GUI_config"]["dikjstra_button_text"], command=self.get_matrix, **button_style)
        self.input_image_button = tk.Button(self.root, text=self.config_data["GUI_config"]["new_image_button_text"], command=self.open_file_explorer, **button_style)
        self.clear_matrix_button = tk.Button(self.root, text=self.config_data["GUI_config"]["clear_bitmap_button_text"], command=self.del_matrix, **button_style)
        self.explanation_button = tk.Button(self.root, text=self.config_data["GUI_config"]["help_button_text"], command=open_explanation_window, **button_style)
        self.new_floor_button = tk.Button(self.root, text=self.config_data["GUI_config"]["add_floor_button_text"], command=self.add_new_floor, **button_style)
        self.pop_floor_button = tk.Button(self.root, text=self.config_data["GUI_config"]["remove_floor_button_text"], command=self.pop_floor, **button_style)
        self.clear_path = tk.Button(self.root, text=self.config_data["GUI_config"]["clear_path_button_text"], command=self.del_path, **button_style)
        self.save_bitmap_button = tk.Button(self.root, text=self.config_data["GUI_config"]["save_bitmap_button_text"], command=self.save_bitmap, **button_style)
        self.clear_gradient_button = tk.Button(self.root, text=self.config_data["GUI_config"]["clear_gradient_button_text"], command=self.clear_gradient, **button_style)

        self.gradient_button = tk.Button(self.root, text="Gradient ON", command=self.toggle_gradient,
                                        bg="#4caf50" if self.gradient else "#f44336", fg="white",
                                        font=("Helvetica", 12), padx=10, pady=5)


        self.update_buttons_position()

    def update_buttons_position(self):
        middle_column = (self.last_col_index + 1) // 2 if self.last_col_index > 0 else 0

        self.get_path_button.grid(row=self.rows + 3, column=middle_column, padx=10, pady=10)
        self.input_image_button.grid(row=self.rows + 3, column=middle_column + 1, padx=10, pady=10)
        self.clear_matrix_button.grid(row=self.rows + 3, column=middle_column + 2, padx=10, pady=10)
        self.gradient_button.grid(row=self.rows + 3, column=middle_column + 3, padx=10, pady=10)
        self.explanation_button.grid(row=self.rows + 3, column=middle_column + 4, padx=10, pady=10)
        self.new_floor_button.grid(row=self.rows + 3, column=middle_column + 5, padx=10, pady=10)
        self.pop_floor_button.grid(row=self.rows + 3, column=middle_column + 6, padx=10, pady=10)
        self.clear_path.grid(row=self.rows + 3, column=middle_column + 7, padx=10, pady=10)
        self.save_bitmap_button.grid(row=self.rows + 3, column=middle_column + 8, padx=10, pady=10)
        self.clear_gradient_button.grid(row=self.rows + 3, column=middle_column + 9, padx=10, pady=10)

    def destroy_buttons(self):
        self.get_path_button.destroy()
        self.input_image_button.destroy()
        self.clear_matrix_button.destroy()
        self.gradient_button.destroy()
        self.explanation_button.destroy()
        self.new_floor_button.destroy()
        self.pop_floor_button.destroy()
        self.clear_path.destroy()
        self.save_bitmap_button.destroy()
        self.clear_gradient_button.destroy()
        
    def update_buttons_position(self):
        middle_column = (self.last_col_index + 1) // 2 if self.last_col_index > 0 else 0

        # Group 0: Especial-related buttons
        self.gradient_button.grid(row=self.rows + 1, column=middle_column - 1, padx=10, pady=10)

        # Group 1: Clear-related buttons
        self.clear_matrix_button.grid(row=self.rows + 1, column=middle_column, padx=10, pady=10)
        self.clear_gradient_button.grid(row=self.rows + 2, column=middle_column, padx=10, pady=10)
        self.clear_path.grid(row=self.rows + 3, column=middle_column, padx=10, pady=10)

        # Group 2: Floor-related buttons
        self.explanation_button.grid(row=self.rows + 1, column=middle_column + 1, padx=10, pady=10)
        self.new_floor_button.grid(row=self.rows + 2, column=middle_column + 1, padx=10, pady=10)
        self.pop_floor_button.grid(row=self.rows + 3, column=middle_column + 1, padx=10, pady=10)

        # Group 3: Rest of them
        self.get_path_button.grid(row=self.rows + 1, column=middle_column + 2, padx=10, pady=10)
        self.input_image_button.grid(row=self.rows + 2, column=middle_column + 2, padx=10, pady=10)
        self.save_bitmap_button.grid(row=self.rows + 3, column=middle_column + 2, padx=10, pady=10)



    
    # ==============================================================================
    # Buttons Functions
    # ==============================================================================

    def save_bitmap(self) -> None:
        matrix_to_bmp(self.matrix, "./saved_bitmap.bmp", self.gradient)

    def pop_floor(self) -> None:
        if len(self.floor_canvases) > 1:
            self.floor_canvases[-1].destroy()
            self.floor_canvases.pop()
            self.all_matrix.pop()
            self.last_col_index -= 1
            self.destroy_buttons()
            self.setup_commands()
            self.update_buttons_position()
        else:
            messagebox.showerror("Invalid Action", "You can't delete the only floor")
    
    def add_new_floor(self) -> None:
        floor_path = self.open_file_explorer(floor=True)
        if floor_path is None:
            return
        
        matrix_floor = self.intermediate_class.return_matrix_of_image(floor_path)
        self.all_matrix.append(matrix_floor)

        self.last_col_index += 1    # Increment the last column index

        # Create a new canvas for the new matrix
        new_canvas = tk.Canvas(self.root, width=self.SQUARE_SIZE * len(matrix_floor[0]),
                            height=self.SQUARE_SIZE * len(matrix_floor), bg="#f0f0f0", borderwidth=0, highlightthickness=0)
        new_canvas.grid(row=0, column=self.last_col_index, rowspan=self.rows, padx=10, pady=10)
        self.floor_canvases.append(new_canvas)

        debug("Drawing matrix on floor {}".format(len(self.floor_canvases) - 1), "debug")
        self.draw_matrix(floor_index=len(self.floor_canvases) - 1, matrix=matrix_floor, update_speed=0)

        self.destroy_buttons()
        self.setup_commands()
        self.update_buttons_position()

        if self.floor_warnings == 0:   # Show warning only once
            self.floor_warnings += 1
            new_floor_warning()
            

    def toggle_gradient(self) -> None:
        self.gradient = not self.gradient
        debug("Gradient toggled: {}".format(self.gradient), "debug")
        self.gradient_button.config(bg="#4caf50" if self.gradient else "#f44336")
        self.gradient_button.config(text="Gradient ON" if self.gradient else "Gradient OFF")

    def open_file_explorer(self, floor=False) -> str:

        file_path = filedialog.askopenfilename(initialdir="./Datasets")
        debug(f"File opened: {file_path}", "debug")
        if file_path and not floor:
            self.root.destroy()
            root = tk.Tk()
            app = MatrixGUI(root, file_path)
            root.mainloop()
        return file_path

    def update_row_color(self, row_index: int) -> None:
        new_color = self.row_colors[row_index].get()
        try:
            color_index = self.colors[:-1].index(new_color)
            self.matrix[row_index] = [color_index] * self.cols
            self.draw_matrix(update_speed=0)
        except ValueError:
            messagebox.showerror("Invalid Color", f"Invalid color: {new_color}")

    def del_matrix(self) -> None:
        if len(self.all_matrix) > 1:
            messagebox.showerror("Invalid Action", "You can't delete the matrix when there are multiple floors")
            return
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] >= 0:
                    self.matrix[i][j] = 0
        self.draw_matrix(update_speed=1)
        
    def del_path(self) -> None:
        if len(self.all_matrix) > 1:
            messagebox.showerror("Invalid Action", "You can't delete the path when there are multiple floors")
            return
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 6:
                    self.matrix[i][j] = 0
        self.draw_matrix(update_speed=1)
        
    def clear_gradient(self) -> None:
        if len(self.all_matrix) > 1:
            messagebox.showerror("Invalid Action", "You can't delete the path when there are multiple floors")
            return
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 4 or self.matrix[i][j] == 5:
                    self.matrix[i][j] = 0
        self.draw_matrix(update_speed=1)
        
    
    # ==============================================================================
    # Mouse Functions
    # ==============================================================================

    def update_square_color(self, event: tk) -> None:
        if len(self.all_matrix) > 1:
            messagebox.showerror("Invalid Action", "You can't change the color of a square when there are multiple floors")
            return
        x, y = event.x, event.y
        col_index, row_index = x // self.SQUARE_SIZE, y // self.SQUARE_SIZE

        if 0 <= row_index < self.rows and 0 <= col_index < self.cols:
            current_color = self.matrix[row_index][col_index]
            new_color = (current_color + 1) % len(self.colors[:-1])
            self.matrix[row_index][col_index] = new_color
            self.draw_matrix(update_speed=0)

    def delete_square(self, event: tk) -> None:
        if len(self.all_matrix) > 1:
            messagebox.showerror("Invalid Action", "You can't delete a square when there are multiple floors")
            return
        x, y = event.x, event.y
        col_index, row_index = x // self.SQUARE_SIZE, y // self.SQUARE_SIZE

        if 0 <= row_index < self.rows and 0 <= col_index < self.cols:
            self.matrix[row_index][col_index] = 0
            self.draw_matrix(update_speed=0)
        
        

    # ==============================================================================
    # Main pathfinding function
    # ==============================================================================

    def get_matrix(self) -> None:
        # Open loading window in a separate thread

        self.all_matrix = self.intermediate_class.return_matrix(self.all_matrix, self.gradient)
            

            

        for i in range(len(self.all_matrix)):
            if i == 0:
                self.matrix = self.all_matrix[i]
                self.draw_matrix(update_speed=1)
                if len(self.all_matrix) == 1:
                    return
            
            else:
                self.floor_canvases[i].destroy()
                self.floor_canvases[i] = new_canvas = tk.Canvas(self.root, width=self.SQUARE_SIZE * len(self.all_matrix[i][0]),
                                        height=self.SQUARE_SIZE * len(self.all_matrix[i]), bg="#f0f0f0", borderwidth=0, highlightthickness=0)
                new_canvas.grid(row=0, column=self.last_col_index + i, rowspan=self.rows, padx=10, pady=10)
                
                self.draw_matrix(floor_index=i, matrix=self.all_matrix[i], update_speed=0)
                


                    

    # ==============================================================================
    # Main Rendering Function
    # ==============================================================================

    def draw_matrix(self, floor_index=None, matrix=None, update_speed=5) -> None:
        colors = self.colors
        
        if floor_index is not None:
            canvas = self.floor_canvases[floor_index]
            canvas.delete("all")  # Clear the canvas
            i, j = 0, 0  # Reset i, j for the given canvas
            while 0 <= i < len(matrix):
                while 0 <= j < len(matrix[i]):
                    x0, y0 = j * self.SQUARE_SIZE, i * self.SQUARE_SIZE
                    x1, y1 = x0 + self.SQUARE_SIZE, y0 + self.SQUARE_SIZE
                    color_index = matrix[i][j]

                    try:
                        color = colors[color_index]
                        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                    except IndexError:
                        color = colors[0]
                        canvas.create_rectangle(x0, y0, x1, y1, fill=color)

                    j += 1

                i += 1
                j = 0

            canvas.config(width=self.SQUARE_SIZE * len(matrix[0]), height=self.SQUARE_SIZE * len(matrix))
            self.root.update_idletasks()
            self.root.grid_rowconfigure(0, weight=1)
            self.root.grid_columnconfigure(0, weight=1)
        
        else:
            for canvas in self.floor_canvases:
                canvas.delete("all")  # Clear all canvases
                i, j = 0, 0
                while 0 <= i < len(self.matrix):
                    while 0 <= j < len(self.matrix[i]):
                        x0, y0 = j * self.SQUARE_SIZE, i * self.SQUARE_SIZE
                        x1, y1 = x0 + self.SQUARE_SIZE, y0 + self.SQUARE_SIZE
                        color_index = self.matrix[i][j]

                        try:
                            color = colors[color_index]
                            canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                        except IndexError:
                            color = colors[0]
                            canvas.create_rectangle(x0, y0, x1, y1, fill=color)

                        j += 1

                    i += 1
                    j = 0

                canvas.config(width=self.SQUARE_SIZE * len(self.matrix[0]), height=self.SQUARE_SIZE * len(self.matrix))
                self.root.update_idletasks()
                self.root.grid_rowconfigure(0, weight=1)
                self.root.grid_columnconfigure(0, weight=1)