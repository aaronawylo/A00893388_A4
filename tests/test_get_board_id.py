"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.game_board import get_board_id


class TestGetBoardID(TestCase):
    def test_get_board_id_works(self):
        example_board = {(0, 0): 'empty_room', (1, 0): 'empty_room', (0, 1): 'empty_room', (1, 1): 'empty_room'}
        example_player = {"X-coordinate": 0, "Y-coordinate": 0}
        actual = get_board_id(example_board, example_player)
        expected = 'empty_room'
        self.assertEqual(actual, expected)

    def test_get_board_id_not_on_board(self):
        with self.assertRaises(KeyError):
            example_board = {(0, 0): 'empty_room', (1, 0): 'empty_room', (0, 1): 'empty_room', (1, 1): 'empty_room'}
            example_player = {"X-coordinate": 2, "Y-coordinate": 2}
            get_board_id(example_board, example_player)
