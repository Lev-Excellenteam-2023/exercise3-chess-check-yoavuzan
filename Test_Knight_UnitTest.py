import unittest
from unittest import TestCase
from unittest.mock import Mock

import Piece as Piece
from enums import Player


class TestKnight(TestCase):
    """ test the Tow functions of the knight """
    def test_get_valid_piece_takes_all_moves(self):
        """ test if the knight can move, all the moves are valid """
        game_state = Mock()
        game_state.get_piece = lambda x, y: Piece.Pawn('p', x, y, Player.PLAYER_2)
        game_state.is_valid_piece = lambda x, y: True
        knight = Piece.Knight('n', 3, 4, Player.PLAYER_1)
        moves_test = knight.get_valid_piece_takes(game_state)
        moves = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)]
        self.assertEqual(len(moves_test), len(moves)) #check if the list of moves is the same
        for move in moves_test:
            self.assertIn(move, moves)

    def test_get_valid_piece_takes_can_not_move(self):
        """ test if the knight can't move """
        game_state = Mock()
        game_state.get_piece = lambda x, y: Piece.Pawn('p', x, y, Player.PLAYER_1)
        game_state.is_valid_piece = lambda x, y: True
        knight = Piece.Knight('n', 3, 4, Player.PLAYER_1)
        moves_test = knight.get_valid_piece_takes(game_state)
        moves = []
        self.assertEqual(len(moves_test), len(moves))

    def test_get_valid_piece_takes_all_not_valid(self):
        """ test if the knight can move, all the moves are not valid """
        game_state = Mock()
        game_state.is_valid_piece = lambda x, y: False
        knight = Piece.Knight('n', 3, 4, Player.PLAYER_1)
        moves_test = knight.get_valid_piece_takes(game_state)
        moves = []
        self.assertEqual(len(moves_test), len(moves))

    def test_get_valid_peaceful_moves_all_moves_(self):
        """ test if the knight can move, all the moves are valid """
        game_state = Mock()
        game_state.get_piece = lambda x, y: Player.EMPTY
        knight = Piece.Knight('n', 3, 4, Player.PLAYER_1)
        peaceful_moves = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)]
        moves_test = knight.get_valid_peaceful_moves(game_state)
        self.assertEqual(len(moves_test), len(peaceful_moves)) #check if the list of moves is the same
        for move in moves_test:
            self.assertIn(move, peaceful_moves) # check if the moves are the same

    def test_get_valid_peaceful_moves_can_not_move(self):
        """ test if the knight can't move """
        game_state = Mock()
        game_state.get_piece = lambda x, y: Player.PLAYER_1
        knight = Piece.Knight('n', 3, 4, Player.PLAYER_1)
        peaceful_moves = []
        moves_test = knight.get_valid_peaceful_moves(game_state)
        self.assertEqual(len(moves_test), len(peaceful_moves)) #check if the list of moves is the same
        for move in moves_test:
            self.assertIn(move, peaceful_moves) # check if the moves are the same

    def test_get_valid_peaseful_moves_can_half_move(self):
        """ test if the knight can move """
        game_state = Mock()
        generator = PieceGenerator(4)
        game_state.get_piece = lambda x, y: generator.generate_Pice(x,y)
        knight = Piece.Knight('n', 3, 4, Player.PLAYER_1)
        peaceful_moves = [(5, 3), (5, 5), (4, 2), (4, 6)] # the knight can move only to the empty places
        moves_test = knight.get_valid_peaceful_moves(game_state)
        self.assertEqual(len(moves_test), len(peaceful_moves)) #check if the list of moves is the same
        for move in moves_test:
            self.assertIn(move, peaceful_moves)

class PieceGenerator:
    """ generate pieces for the test """
    def __init__(self, size):
        self.size = 0
        self.number_of_pieces = size

    def generate_Pice(self,x,y):
        self.size += 1
        if self.size <= self.number_of_pieces:
            return Player.PLAYER_1
        else:
            return Player.EMPTY


if __name__ == '__main__':
    unittest.main()


