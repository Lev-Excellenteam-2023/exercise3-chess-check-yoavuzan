from unittest import TestCase
import unittest
from chess_engine import game_state


class MyTestCase(TestCase):
    def test_something(self):
        state = game_state()
        state.move_piece((1, 2), (2, 2), False)#move white pawn
        state.move_piece((6, 3), (4, 3), False)#move black pawn
        state.move_piece((1, 1), (3, 1), False)#move white pawn
        state.move_piece((7, 4), (3, 0), False)#move black Queen
        # check if the white king is in checkmate
        self.assertEqual(state.checkmate_stalemate_checker(), 0)


if __name__ == '__main__':
    unittest.main()
