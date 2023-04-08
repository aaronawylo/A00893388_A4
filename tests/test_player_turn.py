"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.normal_fight import player_turn
from unittest.mock import patch
import io


class TestPlayerTurn(TestCase):
    def test_player_turn_attack_function_return(self):
        test_player = {"Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1, "potions": 3}
        test_enemy = {"name": "Slime", "hp": 10, "atk": 2, "exp": 20}
        actual = player_turn(1, test_player, test_enemy)
        expected = 0
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_turn_attack_function_print(self, mock_output):
        test_player = {"Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1, "potions": 3}
        test_enemy = {"name": "Slime", "hp": 10, "atk": 2, "exp": 20}
        player_turn(1, test_player, test_enemy)
        actual = mock_output.getvalue()
        expected = "You have dealt 2 damage!\n"
        self.assertEqual(actual, expected)

    def test_player_turn_defend_function_return(self):
        test_player = {"Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1, "potions": 3}
        test_enemy = {"name": "Slime", "hp": 10, "atk": 2, "exp": 20}
        actual = player_turn(2, test_player, test_enemy)
        expected = 1
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_turn_defend_function_print(self, mock_output):
        test_player = {"Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1, "potions": 3}
        test_enemy = {"name": "Slime", "hp": 10, "atk": 2, "exp": 20}
        player_turn(2, test_player, test_enemy)
        actual = mock_output.getvalue()
        expected = "You steel yourself for the oncoming attack!\n"
        self.assertEqual(actual, expected)

    def test_player_turn_potion_function_return(self):
        test_player = {"Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1, "potions": 3}
        test_enemy = {"name": "Slime", "hp": 10, "atk": 2, "exp": 20}
        actual = player_turn(3, test_player, test_enemy)
        expected = 0
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_turn_potioin_function_print(self, mock_output):
        test_player = {"Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1, "potions": 3}
        test_enemy = {"name": "Slime", "hp": 10, "atk": 2, "exp": 20}
        player_turn(3, test_player, test_enemy)
        actual = mock_output.getvalue()
        expected = "You drank the potion and healed 0 HP!\nYour HP is now 20!\n"
        self.assertEqual(actual, expected)
