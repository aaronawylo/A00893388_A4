
from unittest import TestCase

from character.character import make_character


class TestMakeCharacter(TestCase):
    def test_make_character_values_equal(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level":
                    1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual, expected)

    def test_make_character_length_equal(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level":
                    1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(len(actual), len(expected))

    def test_make_character_x_coordinate_value(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level":
                    1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual["X-coordinate"], expected["X-coordinate"])

    def test_make_character_y_coordinate_value(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level":
                    1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual["Y-coordinate"], expected["Y-coordinate"])

    def test_make_character_max_health_value(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level":
                    1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual["Max HP"], expected["Max HP"])

    def test_make_character_current_health_value(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level":
                    1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual["Current HP"], expected["Current HP"])

    def test_make_character_atk_value(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level":
                    1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual["atk"], expected["atk"])

    def test_make_character_def_value(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level":
                    1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual["def"], expected["def"])

    def test_make_character_level_value(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level":
                    1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual["level"], expected["level"])

    def test_make_character_potions_value(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level":
                    1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual["potions"], expected["potions"])

    def test_make_character_battle_actions_value(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level":
                    1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual["Battle Actions"], expected["Battle Actions"])
