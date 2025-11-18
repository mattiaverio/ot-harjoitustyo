import chess

class GameState:
    def __init__(self, fen, turn_white, is_check, is_game_over, result, last_move):
        self.fen = fen
        self.turn_white = turn_white
        self.is_check = is_check
        self.is_game_over = is_game_over
        self.result = result
        self.last_move = last_move

class MoveResult:
    def __init__(self, ok, reason, san, state):
        self.ok = ok
        self.reason = reason
        self.san = san
        self.state = state

class ChessGame:
    def __init__(self):
        self._board = chess.Board()

    def get_state(self):
        if self._board.is_game_over():
            result = self._board.result(claim_draw=True)
        else:
            result = None

        if self._board.move_stack:
            last_move = self._board.peek()
        else:
            last_move = None

        return GameState(
            fen=self._board.fen(),
            turn_white=(self._board.turn == chess.WHITE),
            is_check=self._board.is_check(),
            is_game_over=self._board.is_game_over(),
            result=result,
            last_move=last_move,
        )

    def pieces(self):
        for sq in chess.SQUARES:
            p = self._board.piece_at(sq)
            if p:
                yield (sq, p.piece_type, p.color == chess.WHITE)

    def piece_at(self, square):
        return self._board.piece_at(square)

    def reset(self):
        self._board = chess.Board()

    def legal_targets_from(self, from_sq):
        targets = set()
        for mv in self._board.legal_moves:
            if mv.from_square == from_sq:
                targets.add(mv.to_square)
        return targets

    def allowed_promotions(self, from_sq, to_sq):
        allowed = []
        for pt in (chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT):
            mv = chess.Move(from_sq, to_sq, promotion=pt)
            if mv in self._board.legal_moves:
                allowed.append(pt)
        return allowed

    def move_by_san(self, san):
        try:
            mv = self._board.parse_san(san)
        except Exception as e:
            return self._failed(str(e))
        return self._push_and_report(mv)

    def move(self, from_sq, to_sq, promotion=None):
        mv = chess.Move(from_sq, to_sq, promotion=promotion)
        if mv not in self._board.legal_moves:
            if promotion is None and self.allowed_promotions(from_sq, to_sq):
                return self._failed("Promotion required")
            return self._failed("Illegal move")
        return self._push_and_report(mv)

    def _push_and_report(self, mv):
        san_text = self._board.san(mv)
        self._board.push(mv)
        state = self.get_state()
        return MoveResult(
            ok=True,
            reason=None,
            san=san_text,
            state=state,
        )

    def _failed(self, reason):
        state = self.get_state()
        return MoveResult(
            ok=False, reason=reason, san=None, state=state
        )
