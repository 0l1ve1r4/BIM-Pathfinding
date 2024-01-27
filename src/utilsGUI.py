import tkinter as tk

class HelpGUI:
    def __init__(self, root, text, title, animation_speed=20, auto_destroy = False, waiting_time=0):
        self.root = root
        self.root.title(title)
        self.animation_speed = animation_speed
        self.explanation_text = text

        self.explanation_label = tk.Label(root, text="", justify=tk.LEFT, padx=20, pady=20)
        self.explanation_label.pack()

        tk.Button(root, text="Close", command=root.destroy, padx=10, pady=5).pack()

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
    " - Click 'Get Path' to find the shortest path between the start and end nodes.\n"
    " - Click 'Clear Matrix' to delete gray and yellow squares.\n"
    " - Click 'Input Image' to input an image and convert it to a matrix.\n"
    " - Click 'Gradient' to toggle gradient mode where the path is colored based on the weight of the edges sided by black.\n"
    " - Click 'Explanation' to open a window with additional information about the program.\n"
    " - Click 'Add new Floor' to add a new floor with its own matrix.\n\n"
    "Este programa demonstra uma interface gráfica para gerenciar uma grade de quadrados.\n"
    "A interação com a grade é a seguinte:\n\n"
    " - Clique à esquerda em um quadrado para mudar sua cor.\n"
    " - Clique à direita em um quadrado para excluí-lo.\n"
    " - Clique em 'Obter Caminho' para encontrar o caminho mais curto entre os nós de início e fim.\n"
    " - Clique em 'Limpar Matriz' para excluir quadrados cinza e amarelos.\n"
    " - Clique em 'Entrada de Imagem' para inserir uma imagem e convertê-la em uma matriz.\n"
    " - Clique em 'Gradiente' para alternar o modo de gradiente, onde o caminho é colorido com base no peso das arestas ao lado de preto.\n"
    " - Clique em 'Explicação' para abrir uma janela com informações adicionais sobre o programa.\n"
    " - Clique em 'Adicionar novo Andar' para adicionar um novo andar com sua própria matriz.\n"
    )   
    app = HelpGUI(root, explanation_text, title, animation_speed=0)
    root.mainloop()


def new_floor_warning():
    root = tk.Tk()
    title = "Warning"
    explanation_text = (
    "Adding a new floor and drawing may occurs bugs.\n\n"
    "Some function will be disable when you have more than one floor.\n\n"
    "If you want to use these extra functions, please delete the other floors.\n\n"
    )   
    app = HelpGUI(root, explanation_text, title, animation_speed=0)
    root.mainloop()

def loading_window(waiting_time):
    root = tk.Tk()
    title = "Thread"
    text = "Loading djisktra algorithm in another thread, please wait..."
    app = HelpGUI(root, text, title, animation_speed=0, auto_destroy=True, waiting_time=waiting_time)
    root.mainloop()