"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.battle_actions import potion
from unittest.mock import patch
import io


class TestPotion(TestCase):
    def test_potion_return_no_guard(self):
        test_player = {"Max HP": 20, "Current HP": 12, "potions": 3}
        test_enemy = {"hp": 3}
        actual = potion(test_player, test_enemy)
        expected = 0
        self.assertEqual(actual, expected)

    def test_potion_health_recovered(self):
        test_player = {"Max HP": 20, "Current HP": 12, "potions": 3}
        test_enemy = {"hp": 3}
        potion(test_player, test_enemy)
        actual = test_player["Current HP"]
        expected = 17
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_potion_print_output(self, mock_output):
        test_player = {"Max HP": 20, "Current HP": 12, "potions": 3}
        test_enemy = {"hp": 20}
        potion(test_player, test_enemy)
        actual = mock_output.getvalue()
        expected = 'You drank the potion and healed 5 HP!\nYour HP is now 17!\n'
        self.assertEqual(actual, expected)

    def test_potion_health_maxed_out(self):
        test_player = {"Max HP": 20, "Current HP": 18, "potions": 2}
        test_enemy = {"hp": 3}
        potion(test_player, test_enemy)
        actual = test_player["Current HP"]
        expected = 20
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_potion_go_to_the_gym_print(self, mock_output):
        test_player = {"Max HP": 20, "Current HP": 18, "potions": 2}
        test_enemy = {"hp": 3}
        potion(test_player, test_enemy)
        actual = mock_output.getvalue()
        expected = 'You drank the potion and healed 2 HP!\nYour HP is now 20!\n'
        self.assertEqual(actual, expected)

    def test_potion_are_you_drinking_air(self):
        test_player = {"Max HP": 15, "Current HP": 10, "potions": -1}
        test_enemy = {"hp": 3}
        potion(test_player, test_enemy)
        actual = test_player["Current HP"]
        expected = 15
        self.assertEqual(actual, expected)

    def test_potion_stop_hacking_my_game(self):
        test_player = {"Max HP": 10, "Current HP": 13, "potions": -4}
        test_enemy = {"hp": 3}
        potion(test_player, test_enemy)
        actual = test_player["Current HP"]
        expected = 10
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_potion_stop_hacking_my_game_print(self, mock_output):
        test_player = {"Max HP": 10, "Current HP": 13, "potions": -4}
        test_enemy = {"hp": 5}
        potion(test_player, test_enemy)
        actual = mock_output.getvalue()
        expected = 'You drank the potion and healed -3 HP!\nYour HP is now 10!\n'
        self.assertEqual(actual, expected)
