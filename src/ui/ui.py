import tkinter as tk
from ui.menu_page import MenuPage
from ui.game_page import GamePage
from ui.rating_page import RatingPage


class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OT-Chess")
        self.root.geometry("720x720")
        self.current_frame = None

    def start(self):
        self.show_menu()
        self.root.mainloop()

    def switch_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self.root, self)
        self.current_frame.pack(fill="both", expand=True)

    def show_menu(self):
        self.switch_frame(MenuPage)

    def show_game(self):
        self.switch_frame(GamePage)

    def show_rating(self):
        self.switch_frame(RatingPage)
