"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.fight import action_select
from unittest.mock import patch
import io


class TestActionSelect(TestCase):

    @patch('builtins.input', side_effect="2")
    def test_action_select(self, _):
        test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1,
                       "level": 1, "potions": 3, "Battle Actions": ['Attack', 'Defend', 'Use Potion']}
        actual = action_select(test_player)
        expected = "2"
        self.assertEqual(actual, expected)
