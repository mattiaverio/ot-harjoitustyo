
import tkinter as tk
from tkinter import simpledialog


class MenuPage(tk.Frame):
    def __init__(self, master, ui):
        super().__init__(master)
        self.ui = ui

        tk.Label(self, text="Chess Menu", font=("Arial", 24)).pack(pady=20)
        tk.Button(self, text="Start Game",
                  command=self.start_game_click).pack(pady=10)
        tk.Button(self, text="Rating list",
                  command=ui.show_rating).pack(pady=10)
        tk.Button(self, text="Exit", command=master.destroy).pack(pady=10)

    def start_game_click(self):
        white_name = simpledialog.askstring(
            "Input", "Username for White pieces:", parent=self)
        if not white_name:
            return

        black_name = simpledialog.askstring(
            "Input", "Username for Black pieces:", parent=self)
        if not black_name:
            return

        self.ui.user_service.create_user(white_name)
        self.ui.user_service.login(white_name)
        white_player = self.ui.user_service.get_current_user()

        self.ui.user_service.create_user(black_name)
        self.ui.user_service.login(black_name)
        black_player = self.ui.user_service.get_current_user()

        self.ui.show_game(white_player, black_player)
