"""
Aaron Lo
A0089388
"""
from unittest import TestCase

from Movement.movement import move_character


class TestMoveCharacter(TestCase):

    def test_move_character_north(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2}
        expected = {"X-coordinate": 2, "Y-coordinate": 1}
        move_character(character, 1)
        actual = character
        self.assertEqual(expected, actual)

    def test_move_character_east(self):
        character = {"X-coordinate": 4, "Y-coordinate": 5}
        expected = {"X-coordinate": 5, "Y-coordinate": 5}
        move_character(character, 2)
        actual = character
        self.assertEqual(expected, actual)

    def test_move_character_south(self):
        character = {"X-coordinate": 3, "Y-coordinate": -1}
        expected = {"X-coordinate": 3, "Y-coordinate": 0}
        move_character(character, 3)
        actual = character
        self.assertEqual(expected, actual)

    def test_move_character_west(self):
        character = {"X-coordinate": 0, "Y-coordinate": 2}
        expected = {"X-coordinate": -1, "Y-coordinate": 2}
        move_character(character, 4)
        actual = character
        self.assertEqual(expected, actual)
