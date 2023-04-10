"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from character.character_modules import level_up
from unittest.mock import patch
import io


class TestLevelUp(TestCase):
    def test_level_up_no_level(self):
        test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 1, "exp": 0, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        level_up(test_player)
        actual = test_player
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                    "level": 1, "exp": 0, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual, expected)

    def test_level_up_max_level(self):
        test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 3, "exp": 110, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        level_up(test_player)
        actual = test_player
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                    "level": 3, "exp": 110, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual, expected)

    def test_level_up_values_equal(self):
        test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 1, "exp": 110, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        level_up(test_player)
        actual = test_player
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level":
                    2, "exp": 10, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual, expected)

    def test_level_up_length_equal(self):
        test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 1, "exp": 110, "potions": 3}
        level_up(test_player)
        actual = test_player
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level":
                    2, "exp": 10, "potions": 3}
        self.assertEqual(len(actual), len(expected))

    def test_level_up_max_health_value(self):
        test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 1, "exp": 110, "potions": 3, "Battle Actions": ["Attack", "Defend"]}
        level_up(test_player)
        actual = test_player
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level":
                    2, "exp": 10, "potions": 3, "Battle Actions": ["Attack", "Defend"]}
        self.assertEqual(actual["Max HP"], expected["Max HP"])

    def test_level_up_current_health_value(self):
        test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 1, "exp": 110, "potions": 3, "Battle Actions": ["Attack", "Use Potion"]}
        level_up(test_player)
        actual = test_player
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level":
                    2, "exp": 10, "potions": 3, "Battle Actions": ["Attack", "Use Potion"]}
        self.assertEqual(actual["Current HP"], expected["Current HP"])

    def test_level_up_atk_value(self):
        test_player = {"X-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 1, "exp": 110, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        level_up(test_player)
        actual = test_player
        expected = {"X-coordinate": 0, "Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level": 2, "exp": 10,
                    "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual["atk"], expected["atk"])

    def test_level_up_def_value(self):
        test_player = {"Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 1, "exp": 110, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        level_up(test_player)
        actual = test_player
        expected = {"Y-coordinate": 0, "Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level": 2, "exp": 10,
                    "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        self.assertEqual(actual["def"], expected["def"])

    def test_level_up_level_value(self):
        test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 1, "exp": 110, "potions": 3, "Battle Actions": ["Defend", "Use Potion"]}
        level_up(test_player)
        actual = test_player
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level":
                    2, "exp": 10, "potions": 3, "Battle Actions": ["Defend", "Use Potion"]}
        self.assertEqual(actual["level"], expected["level"])

    def test_level_up_exp_value(self):
        test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 1, "exp": 110, "potions": 3, "Battle Actions": ["Attack"]}
        level_up(test_player)
        actual = test_player
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level":
                    2, "exp": 10, "potions": 3, "Battle Actions": ["Attack"]}
        self.assertEqual(actual["exp"], expected["exp"])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_printout(self, mock_output):
        test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 1, "exp": 110, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
        level_up(test_player)
        actual = mock_output.getvalue()
        expected = "You have gained a level, and you are now level 2!\nYour Max HP is 40!\n""Your Attack is now 5!\n" \
                   "Your Defense is now 4!\n\n"
        self.assertEqual(actual, expected)

    def test_level_up_no_max_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"Maxi HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level": 2, "exp": 10}
            level_up(test_player)

    def test_level_up_no_current_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"Max HP": 40, "Currento HP": 40, "atk": 5, "def": 4, "level": 2, "exp": 10}
            level_up(test_player)

    def test_level_up_no_atk_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"Max HP": 40, "Current HP": 40, "atkk": 5, "def": 4, "level": 2, "exp": 10}
            level_up(test_player)

    def test_level_up_no_def_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"Max HP": 40, "Current HP": 40, "atk": 5, "defi": 4, "level": 2, "exp": 10}
            level_up(test_player)

    def test_level_up_no_level_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "levely": 2, "exp": 10}
            level_up(test_player)

    def test_level_up_no_exp_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level": 2, "experience": 10}
            level_up(test_player)

    def test_level_up_no_value_in_max_in_player(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": "This", "Current HP": 40, "atk": 5, "def": 4, "level": 2, "exp": 10}
            level_up(test_player)

    def test_level_up_no_value_in_current_in_player(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": 40, "Current HP": "Is", "atk": 5, "def": 4, "level": 2, "exp": 10}
            level_up(test_player)

    def test_level_up_no_value_in_atk_in_player(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": 40, "Current HP": 40, "atk": "A", "def": 4, "level": 2, "exp": 10}
            level_up(test_player)

    def test_level_up_no_value_in_def_in_player(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": 40, "Current HP": 40, "atk": 5, "def": "Lot", "level": 2, "exp": 10}
            level_up(test_player)

    def test_level_up_no_value_in_level_in_player(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level": "Of", "exp": 10}
            level_up(test_player)

    def test_level_up_no_value_in_exp_in_player(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": 40, "Current HP": 40, "atk": 5, "def": 4, "level": 2, "exp": "Tests"}
            level_up(test_player)
