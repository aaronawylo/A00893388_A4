"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.fight import character_actions


class TestCharacterActions(TestCase):
    def test_character_actions_with_key(self):
        test_player = {"Battle Actions": ['Attack', 'Defend', 'Use Potion', 'Secret Move: Ultimate World Breaker']}
        actual = character_actions(test_player)
        expected = ['Attack', 'Defend', 'Use Potion', 'Secret Move: Ultimate World Breaker']
        self.assertEqual(actual, expected)

    def test_character_actions_without_key(self):
        with self.assertRaises(KeyError):
            test_player = {"Why didn't I make a better character?": "I should be better next time."}
            character_actions(test_player)
