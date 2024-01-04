from tkinter_graph import Interface
import tkinter as tk


    #                                         #
    #                                         #
    #                                         #
    #               Main loop                 #
    #                                         #
    #                                         #
    #                                         #

if __name__ == "__main__":

    print("\033[H\033[J")

    root = tk.Tk()
    app = Interface(root)
    root.mainloop()