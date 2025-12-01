from entities.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return [User(row["username"], row["elo"]) for row in rows]

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return User(row["username"], row["elo"]) if row else None

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, elo) VALUES (?, ?)",
            (user.username, user.elo)
        )
        self._connection.commit()
        return user

    def update_elo(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE users SET elo = ? WHERE username = ?",
            (user.elo, user.username)
        )
        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()

    def find_top_by_elo(self, limit=20):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users ORDER BY elo DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        return [User(row["username"], row["elo"]) for row in rows]