class User:
    def __init__(self, username, elo=1200):
        self.username = username
        self.elo = elo

    def __str__(self):
        return f"{self.username} (ELO: {self.elo})"