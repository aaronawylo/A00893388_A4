"""
Aaron Lo
A0089388
"""
from unittest import TestCase


from Movement.movement import validate_move

BOARD = {(0, 0): 'Empty Room', (0, 1): 'Empty Room', (0, 2): 'Empty Room',
         (1, 0): 'Empty Room', (1, 1): 'Empty Room', (1, 2): 'Empty Room',
         (2, 0): 'Empty Room', (2, 1): 'Empty Room', (2, 2): 'Empty Room'}


class TestValidateMove(TestCase):
    def test_validate_upper_left_move_east(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        direction = 2
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_upper_left_move_north(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 4}
        direction = 1
        actual = validate_move(BOARD, character, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_upper_left_move_south(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 4}
        direction = 3
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_upper_left_move_west(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 4}
        direction = 4
        actual = validate_move(BOARD, character, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_upper_right_move_east(self):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 5}
        direction = 2
        actual = validate_move(BOARD, character, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_upper_right_move_north(self):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 4}
        direction = 1
        actual = validate_move(BOARD, character, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_upper_right_move_south(self):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 4}
        direction = 3
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_upper_right_move_west(self):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 4}
        direction = 4
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_lower_left_move_east(self):
        character = {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 5}
        direction = 2
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_lower_left_move_north(self):
        character = {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 4}
        direction = 1
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_lower_left_move_south(self):
        character = {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 4}
        direction = 3
        actual = validate_move(BOARD, character, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_lower_left_move_west(self):
        character = {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 4}
        direction = 4
        actual = validate_move(BOARD, character, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_lower_right_move_east(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}
        direction = 2
        actual = validate_move(BOARD, character, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_lower_right_move_north(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 4}
        direction = 1
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_lower_right_move_south(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 4}
        direction = 3
        actual = validate_move(BOARD, character, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_lower_right_move_west(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 4}
        direction = 4
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_center_move_east(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        direction = 2
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_center_move_north(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 4}
        direction = 1
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_center_move_south(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 4}
        direction = 3
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_center_move_west(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 4}
        direction = 4
        actual = validate_move(BOARD, character, direction)
        expected = True
        self.assertEqual(actual, expected)
