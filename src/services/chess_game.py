from dataclasses import dataclass
import chess


@dataclass
class GameState:
    fen: str
    turn_white: bool
    is_check: bool
    is_game_over: bool
    result: str | None = None
    last_move: chess.Move | None = None


@dataclass
class MoveResult:
    ok: bool
    reason: str | None = None
    san: str | None = None
    state: GameState | None = None


class ChessGame:
    def __init__(self):
        self._board = chess.Board()

    @property
    def state(self):
        return self.get_state()

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

    def is_piece_own(self, piece):
        if piece is None:
            return False
        side_to_move_is_white = self._board.turn == chess.WHITE
        return (piece.color == chess.WHITE) == side_to_move_is_white

    def is_square_own(self, square):
        return self.is_piece_own(self._board.piece_at(square))

    def reset(self):
        self._board = chess.Board()

    def legal_targets_from(self, from_sq):
        targets = set()
        for mv in self._board.legal_moves:
            if mv.from_square == from_sq:
                targets.add(mv.to_square)
        return targets

    def needs_promotion(self, from_sq: int, to_sq: int) -> bool:
        return any(
            mv.from_square == from_sq and mv.to_square == to_sq and mv.promotion
            for mv in self._board.legal_moves
        )

    def allowed_promotions(self, from_sq, to_sq):
        allowed = []
        for pt in (chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT):
            mv = chess.Move(from_sq, to_sq, promotion=pt)
            if mv in self._board.legal_moves:
                allowed.append(pt)
        return allowed

    def move_by_san(self, san: str):
        san = san.strip()
        if not san:
            return self._failed("Empty SAN")
        try:
            mv = self._board.parse_san(san)
        except ValueError:
            return self._failed(f"Invalid SAN: {san}")
        return self._push_and_report(mv)

    def move(self, from_sq, to_sq, promotion=None):
        mv = chess.Move(from_sq, to_sq, promotion=promotion)
        if mv not in self._board.legal_moves:
            if promotion is None and self.allowed_promotions(from_sq, to_sq):
                return self._failed("Promotion required")
            return self._failed("Illegal move")
        return self._push_and_report(mv)

    def move_or_prompt(self, from_sq, to_sq, prompt_callback=None):
        initial = self.move(from_sq, to_sq)
        if initial.ok:
            return initial

        if not self.needs_promotion(from_sq, to_sq):
            return initial

        if prompt_callback is None:

            return self._failed("Promotion required")

        allowed = self.allowed_promotions(from_sq, to_sq)
        if not allowed:

            return self._failed("Promotion required but no options")

        choice = prompt_callback(allowed)

        if choice is None:
            return self._failed("Promotion canceled")

        promoted_result = self.move(from_sq, to_sq, promotion=choice)
        return promoted_result

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
