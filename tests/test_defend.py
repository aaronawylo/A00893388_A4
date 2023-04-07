"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.battle_actions import defend
from unittest.mock import patch
import io


class TestDefend(TestCase):
    def test_defend_return_basic_guard(self):
        test_player = {"level": 1, "def": 2}
        test_enemy = {"hp": 3}
        actual = defend(test_player, test_enemy)
        expected = 2
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_defend_print_output(self, mock_output):
        test_player = {"level": 3, "def": 6}
        test_enemy = {"hp": 20}
        defend(test_player, test_enemy)
        actual = mock_output.getvalue()
        expected = 'You steel yourself for the oncoming attack!\n'
        self.assertEqual(actual, expected)

    def test_defend_return_level_two_guard(self):
        test_player = {"level": 2, "def": 4}
        test_enemy = {"hp": 10}
        actual = defend(test_player, test_enemy)
        expected = 8
        self.assertEqual(actual, expected)

    def test_defend_return_level_three_guard(self):
        test_player = {"level": 3, "def": 6}
        test_enemy = {"hp": 20}
        actual = defend(test_player, test_enemy)
        expected = 18
        self.assertEqual(actual, expected)

    def test_defend_arms_up(self):
        test_player = {"level": 1, "def": 0}
        test_enemy = {"hp": 3}
        actual = defend(test_player, test_enemy)
        expected = 0
        self.assertEqual(actual, expected)

    def test_defend_why_are_you_hitting_yourself(self):
        test_player = {"level": 1, "def": -2}
        test_enemy = {"hp": 16}
        actual = defend(test_player, test_enemy)
        expected = -2
        self.assertEqual(actual, expected)

    def test_defend_how_are_you_negative_level(self):
        test_player = {"level": -3, "def": 4}
        test_enemy = {"hp": 3}
        actual = defend(test_player, test_enemy)
        expected = -12
        self.assertEqual(actual, expected)

    def test_defend_two_negatives_make_a_positive(self):
        test_player = {"level": -4, "def": -5}
        test_enemy = {"hp": 3}
        actual = defend(test_player, test_enemy)
        expected = 20
        self.assertEqual(actual, expected)

    def test_attack_no_level_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"forgot I can get stronger": 2, "def": 3}
            test_enemy = {"hp": 5}
            defend(test_player, test_enemy)

    def test_attack_no_attack_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"level": 2, "Glass Cannon Baby": 3}
            test_enemy = {"hp": 5}
            defend(test_player, test_enemy)
