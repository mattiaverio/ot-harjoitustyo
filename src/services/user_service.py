from entities.user import User
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository
        self._current_user = None

    def login(self, username):
        user = self._user_repository.find_by_username(username)
        if not user:
            return False

        self._current_user = user
        return True

    def create_user(self, username):
        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            return False

        user = User(username)
        self._user_repository.create(user)
        return True

    def get_current_user(self):
        return self._current_user

    def logout(self):
        self._current_user = None

    def get_users_by_rating(self):
        return self._user_repository.find_top_by_elo()
