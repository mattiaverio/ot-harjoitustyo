import unittest
from chess_core import ChessGame

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

    def test_checkmate(self):
        self.assertTrue(self.game.move_by_san("f3").ok)
        self.assertTrue(self.game.move_by_san("e5").ok)
        self.assertTrue(self.game.move_by_san("g4").ok)
        res = self.game.move_by_san("Qh4")
        self.assertTrue(res.ok)

        st = self.game.get_state()
        self.assertTrue(st.is_game_over)
        self.assertEqual(st.result, "0-1")
