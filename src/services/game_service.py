class GameService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def record_game_result(self, white_player, black_player, result_string):
        score_white = 0.5
        if result_string == "1-0":
            score_white = 1.0
        elif result_string == "0-1":
            score_white = 0.0
        
        score_black = 1.0 - score_white

        self._update_elo(white_player, black_player, score_white, score_black)

    def _update_elo(self, white_player, black_player, score_white, score_black):
        new_white_elo = self._calculate_new_rating(white_player.elo, black_player.elo, score_white)
        new_black_elo = self._calculate_new_rating(black_player.elo, white_player.elo, score_black)

        white_player.elo = new_white_elo
        black_player.elo = new_black_elo

        self._user_repository.update_elo(white_player)
        self._user_repository.update_elo(black_player)

    def _calculate_new_rating(self, rating_a, rating_b, actual_score_a):
        K = 32
        expected_score_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
        new_rating_a = rating_a + K * (actual_score_a - expected_score_a)
        return int(round(new_rating_a))