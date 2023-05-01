import unittest
from ai_engine import chess_ai
from unittest import TestCase
from unittest.mock import Mock

import Piece as Piece
from enums import Player
from chess_engine import game_state


class TestKnightIntegration(TestCase):
    """Test the Knight class"""

    def test_get_valid_piece_moves(self):
        knight = Piece.Knight('n', 3, 4, Player.PLAYER_1)
        knight_mock = Mock(spec=knight)
        knight_mock.get_valid_peaceful_moves.return_value \
            = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)]
        # the knight can move to all these places
        knight_mock.get_valid_piece_takes.return_value = []
        # the knight can't take any piece
        game_state = Mock()
        knight_mock.get_valid_piece_moves(game_state)

    def test_evaluate_board(self):
        """
        Test the evaluate_board function in class chess_ai
        stare: all the bord with Knights of player 2
        """
        game_state = Mock()
        game_state.is_valid_piece.return_value = True
        game_state.get_piece.return_value = Piece.Knight('n', 3, 4, Player.PLAYER_2)
        ai_test = chess_ai()
        score = ai_test.evaluate_board(game_state, Player.PLAYER_2)
        self.assertEqual(score, 1920)  # 8 * 8 * 30

    def test_evaluate_board(self):
        """
        Test the evaluate_board function in class chess_ai
        stare: all the bord is empty
        """
        state = game_state()
        ai_test = chess_ai()
        score = ai_test.evaluate_board(state, Player.PLAYER_2)
        self.assertEqual(score, 0)  # 8 * 8 * 0


if __name__ == '__main__':
    unittest.main()


