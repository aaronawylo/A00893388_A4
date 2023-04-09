"""
Aaron Lo
A0089388
"""
from unittest import TestCase

from utilities.miscellaneous import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    def test_check_if_goal_attained_two_by_two_start(self):
        board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room'}
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        actual = check_if_goal_attained(board, character)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_two_by_two_end(self):
        board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room'}
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        actual = check_if_goal_attained(board, character)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_x_coordinate_met_y_coordinate_not_met(self):
        board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room'}
        character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        actual = check_if_goal_attained(board, character)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_x_coordinate_not_met_y_coordinate_met(self):
        board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room'}
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        actual = check_if_goal_attained(board, character)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_two_by_two_out_of_bounds(self):
        board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room'}
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}
        actual = check_if_goal_attained(board, character)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_three_by_three_start(self):
        board = {(0, 0): 'Puppies About', (0, 1): 'Empty Room', (0, 2): 'Empty Room', (0, 3): 'Empty Room',
                 (1, 0): 'Empty Room', (1, 1): 'Empty Room', (1, 2): 'Empty Room', (1, 3): 'Empty Room',
                 (2, 0): 'Empty Room', (2, 1): 'Empty Room', (2, 2): 'Empty Room', (2, 3): 'Empty Room'}
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 3}
        actual = check_if_goal_attained(board, character)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_three_by_three_end(self):
        board = {(0, 0): 'Puppies About', (0, 1): 'Puppies Still here', (0, 2): 'Empty Room', (1, 0): 'Empty Room',
                 (1, 1): 'Empty Room', (1, 2): 'Empty Room', (2, 0): 'Empty Room', (2, 1): 'Empty Room',
                 (2, 2): 'Empty Room'}
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 2}
        actual = check_if_goal_attained(board, character)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_six_by_six_start(self):
        board = {(0, 0): 'This', (0, 1): 'Is', (0, 2): 'Very', (0, 3): 'Annoying',
                 (0, 4): 'Empty Room', (0, 5): 'Empty Room', (1, 0): 'Empty Room', (1, 1): 'Empty Room',
                 (1, 2): 'Empty Room', (1, 3): 'Empty Room', (1, 4): 'Empty Room', (1, 5): 'Empty Room',
                 (2, 0): 'Empty Room', (2, 1): 'Empty Room', (2, 2): 'Empty Room', (2, 3): 'Empty Room',
                 (2, 4): 'Empty Room', (2, 5): 'Empty Room', (3, 0): 'Empty Room', (3, 1): 'Empty Room',
                 (3, 2): 'Empty Room', (3, 3): 'Empty Room', (3, 4): 'Empty Room', (3, 5): 'Empty Room',
                 (4, 0): 'Empty Room', (4, 1): 'Empty Room', (4, 2): 'Empty Room', (4, 3): 'Empty Room',
                 (4, 4): 'Empty Room', (4, 5): 'Empty Room', (5, 0): 'Empty Room', (5, 1): 'Empty Room',
                 (5, 2): 'Empty Room', (5, 3): 'Empty Room', (5, 4): 'Empty Room', (5, 5): 'Empty Room'}
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 6}
        actual = check_if_goal_attained(board, character)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_six_by_six_end(self):
        board = {(0, 0): 'This', (0, 1): 'Is', (0, 2): 'Very', (0, 3): 'Annoying',
                 (0, 4): 'Please', (0, 5): 'Stop', (1, 0): 'Saying', (1, 1): 'It',
                 (1, 2): 'Is', (1, 3): 'A', (1, 4): 'Duplicate', (1, 5): 'Empty Room',
                 (2, 0): 'Empty Room', (2, 1): 'Empty Room', (2, 2): 'Empty Room', (2, 3): 'Empty Room',
                 (2, 4): 'Empty Room', (2, 5): 'Empty Room', (3, 0): 'Empty Room', (3, 1): 'Empty Room',
                 (3, 2): 'Empty Room', (3, 3): 'Empty Room', (3, 4): 'Empty Room', (3, 5): 'Empty Room',
                 (4, 0): 'Empty Room', (4, 1): 'Empty Room', (4, 2): 'Empty Room', (4, 3): 'Empty Room',
                 (4, 4): 'Empty Room', (4, 5): 'Empty Room', (5, 0): 'Empty Room', (5, 1): 'Empty Room',
                 (5, 2): 'Empty Room', (5, 3): 'Empty Room', (5, 4): 'Empty Room', (5, 5): 'Empty Room'}
        character = {"X-coordinate": 5, "Y-coordinate": 5, "Current HP": 8}
        actual = check_if_goal_attained(board, character)
        expected = True
        self.assertEqual(actual, expected)
