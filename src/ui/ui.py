import tkinter as tk
from ui.menu_page import MenuPage
from ui.game_page import GamePage
from ui.rating_page import RatingPage
from database_connection import get_database_connection
from repositories.user_repository import UserRepository
from services.user_service import UserService
from services.game_service import GameService


class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OT-Chess")
        self.root.geometry("720x720")
        self.current_frame = None

        connection = get_database_connection()
        user_repository = UserRepository(connection)
        self.user_service = UserService(user_repository)
        self.game_service = GameService(user_repository)

    def start(self):
        self.show_menu()
        self.root.mainloop()

    def switch_frame(self, frame_class, *args, **kwargs):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self.root, self, *args, **kwargs)
        self.current_frame.pack(fill="both", expand=True)

    def show_menu(self):
        self.switch_frame(MenuPage)

    def show_game(self, white_player=None, black_player=None):
        self.switch_frame(GamePage, white_player, black_player)

    def show_rating(self):
        self.switch_frame(RatingPage)
