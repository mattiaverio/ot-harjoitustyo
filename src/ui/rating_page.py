
import tkinter as tk


class RatingPage(tk.Frame):
    def __init__(self, master, ui):
        super().__init__(master)
        tk.Label(self, text="Rating list", font=("Arial", 24)).pack(pady=20)
        tk.Button(self, text="Back to Menu",
                  command=ui.show_menu).pack(pady=10)
