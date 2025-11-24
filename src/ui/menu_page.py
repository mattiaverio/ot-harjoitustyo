
import tkinter as tk


class MenuPage(tk.Frame):
    def __init__(self, master, ui):
        super().__init__(master)
        tk.Label(self, text="Chess Menu", font=("Arial", 24)).pack(pady=20)
        tk.Button(self, text="Start Game", command=ui.show_game).pack(pady=10)
        tk.Button(self, text="Rating list",
                  command=ui.show_rating).pack(pady=10)
        tk.Button(self, text="Exit", command=master.destroy).pack(pady=10)
