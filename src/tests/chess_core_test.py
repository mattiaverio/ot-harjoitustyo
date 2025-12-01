import unittest
import chess
from services.chess_game import ChessGame


class TestChessCore(unittest.TestCase):
    def setUp(self):
        self.game = ChessGame()

    def test_initial_state(self):
        st = self.game.get_state()
        self.assertTrue(st.turn_white)
        self.assertFalse(st.is_game_over)
        self.assertFalse(st.is_check)
        self.assertIsNone(st.last_move)
        self.assertEqual(len(list(self.game.pieces())), 32)

    def test_illegal_move_rejected(self):
        res = self.game.move_by_san("e5")
        self.assertFalse(res.ok)

        res = self.game.move(chess.E2, chess.E5)
        self.assertFalse(res.ok)

    def test_empty_san(self):
        res = self.game.move_by_san("")
        self.assertFalse(res.ok)

    def test_checkmate(self):
        self.assertTrue(self.game.move_by_san("f3").ok)
        self.assertTrue(self.game.move_by_san("e5").ok)
        self.assertTrue(self.game.move_by_san("g4").ok)
        res = self.game.move_by_san("Qh4")
        self.assertTrue(res.ok)

        st = self.game.get_state()
        self.assertTrue(st.is_game_over)
        self.assertEqual(st.result, "0-1")

    def test_reset_clears_board(self):
        self.game.move_by_san("e4")
        self.assertFalse(self.game.state.turn_white)

        self.game.reset()
        st = self.game.state
        
        self.assertTrue(st.turn_white)
        self.assertEqual(st.fen, chess.STARTING_FEN)

    def test_is_square_own_works(self):
        self.assertTrue(self.game.is_square_own(chess.E2))
        self.assertFalse(self.game.is_square_own(chess.E7))
        self.assertFalse(self.game.is_square_own(chess.E4))

    def test_piece_at_works(self):
        piece = self.game.piece_at(chess.E1)
        self.assertIsNotNone(piece)
        self.assertEqual(piece.piece_type, chess.KING)
        self.assertEqual(piece.color, chess.WHITE)
        
        empty = self.game.piece_at(chess.E4)
        self.assertIsNone(empty)

    def test_move_with_coordinates_works(self):
        res = self.game.move(chess.E2, chess.E4)
        self.assertTrue(res.ok)

    def test_legal_targets_works(self):
        targets = self.game.legal_targets_from(chess.G1)
        expected = {chess.F3, chess.H3}
        self.assertEqual(targets, expected)