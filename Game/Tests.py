import unittest
from Game.Interface_game import *


class Tester(unittest.TestCase):
    def test_check_winner(self):
        x = Board()
        x.create_empty_board()
        assert InterfaceGame.check_winner(x)

    def test_attack_player(self):
        x = Board()
        x.create_empty_board()
        InterfaceGame.attack_player(x, 1, 1)
        assert x.board[1][1] == "miss"

    def test_place_boat(self):
        x = Board()
        x.create_empty_board()
        boat = InterfaceGame.place_boat(2, 3, 3, "h")
        assert boat.orientation == "h"

    def test_add_boat(self):
        x = Boat(5, "v", [2, 3], [2, 9])
        board = Board()
        board.create_empty_board()
        board.add_boat(x)
        assert board.board[3][2] == 5

    def test_check_winners(self):
        x = Board()
        x.create_empty_board()
        assert InterfaceGame.check_winner(x)

    def test_create_board(self):
        x = Board()
        x.create_empty_board()
        assert len(x.board) == 10

    def test_check_for_boat(self):
        x = Board()
        x.create_empty_board()
        x.board[2][2] = 5
        boat = Boat(5, "v", [2, 1], [2, 6])
        assert x.check_for_boat(boat)

    def test_outside_board(self):
        x = Board()
        assert x.outside_board([11, 12], [11, 14])

    def test_hit_or_miss(self):
        x = Board()
        x.create_empty_board()
        x.board[2][2] = 5
        assert x.hit_or_miss(2, 2)

    def test_boat(self):
        x = Boat(2, "h", [2, 2], [2, 8])
        assert x.orientation == "h"


if __name__ == '__main__':
    Tester()
