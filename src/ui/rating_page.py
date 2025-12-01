import tkinter as tk
from tkinter import ttk

class RatingPage(tk.Frame):
    def __init__(self, master, ui):
        super().__init__(master)
        self.ui = ui
        
        self._build_ui()
        self._populate_data()

    def _build_ui(self):
        tk.Label(self, text="Top Players", font=("Arial", 24)).pack(pady=20)

        columns = ("rank", "username", "elo")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)
        
        self.tree.heading("rank", text="#")
        self.tree.column("rank", width=50, anchor="center")
        
        self.tree.heading("username", text="Player")
        self.tree.column("username", width=200, anchor="center")
        
        self.tree.heading("elo", text="ELO")
        self.tree.column("elo", width=100, anchor="center")
        
        self.tree.pack(pady=10, padx=20)

        tk.Button(self, text="Back to Menu", command=self.ui.show_menu).pack(pady=10)

    def _populate_data(self):
        users = self.ui.user_service.get_users_by_rating()
        
        for i, user in enumerate(users, start=1):
            self.tree.insert("", "end", values=(i, user.username, user.elo))