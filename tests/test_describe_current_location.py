"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.game_board import describe_current_location
from unittest.mock import patch
import io


class TestDescribeCurrentLocation(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location(self, mock_output):
        example_board = {(0, 0): 'empty_room', (1, 0): 'empty_room', (0, 1): 'empty_room', (1, 1): 'empty_room'}
        example_player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        example_room_list = {"empty_room": ["This is an empty room.", "empty_room", 3]}
        describe_current_location(example_board, example_player, example_room_list)
        actual = mock_output.getvalue()
        expected = "This is an empty room.\nYou are currently at (0, 0)\nYour HP is: 5\n\n"
        self.assertEqual(actual, expected)

    def test_describe_current_location_out_of_bounds_entirely(self):
        with self.assertRaises(KeyError):
            example_board = {(0, 0): 'Example', (1, 0): 'Room', (0, 1): 'For', (1, 1): 'Error Testing'}
            example_player = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}
            example_room_list = {"empty_room": ["This is an empty room.", "empty_room", 3]}
            describe_current_location(example_board, example_player, example_room_list)

    def test_describe_current_location_out_of_bounds_x_coordinate(self):
        with self.assertRaises(KeyError):
            example_board = {(0, 0): 'Example', (1, 0): 'Room', (0, 1): 'For', (1, 1): 'Error Testing'}
            example_player = {"X-coordinate": 2, "Y-coordinate": 1, "Current HP": 5}
            example_room_list = {"empty_room": ["This is an empty room.", "empty_room", 3]}
            describe_current_location(example_board, example_player, example_room_list)

    def test_describe_current_location_out_of_bounds_y_coordinate(self):
        with self.assertRaises(KeyError):
            example_board = {(0, 0): 'Example', (1, 0): 'Room', (0, 1): 'For', (1, 1): 'Error Testing'}
            example_player = {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 5}
            example_room_list = {"empty_room": ["This is an empty room.", "empty_room", 3]}
            describe_current_location(example_board, example_player, example_room_list)

    def test_describe_current_location_room_list_has_no_match(self):
        with self.assertRaises(KeyError):
            example_board = {(0, 0): 'Look', (1, 0): 'Just', (0, 1): 'Changing', (1, 1): 'Code'}
            example_player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
            example_room_list = {"empty_room": ["This is an empty room.", "empty_room", 3]}
            describe_current_location(example_board, example_player, example_room_list)
